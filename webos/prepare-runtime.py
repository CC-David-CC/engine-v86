"""Recover the original WebOS v86 runtime from the pinned upstream npm release."""

import argparse
import hashlib
import io
import subprocess
from pathlib import Path
import tarfile
from urllib.request import urlopen


FIRMWARE_REV = 'cc37f35c43bf14865d74ad76879ecf9410f69eb1'
PACKAGE = 'https://registry.npmjs.org/v86/-/v86-0.5.472.tgz'
PACKAGE_SHA256 = '4698fae3f518ad0a6f78d31e8f6f8802ff272a86f07b603b95f6c9fdd428e4fc'
MAX_PACKAGE_BYTES = 12 * 1024 * 1024
RUNTIME_FILES = {
    'libv86.js': '1b41074f7a5604f528dac6842baf7afccd79d7370b97ea3241944c275b67bec1',
    'v86.wasm': '2f0c4150f266415b754a84a32e6f8e4c975a1d3abb94c78b047fa30027db1ef1',
}
FIRMWARE_FILES = {
    'seabios.bin': '73e3f359102e3a9982c35fce98eb7cd08f18303ac7f1ba6ebfbe6cdc1c244d98',
    'vgabios.bin': 'a4bc0d80cc3ca028c73dafa8fee396b8d054ce87ebd8abfbd31b06b437607880',
}


def verify(name, data, expected):
    if hashlib.sha256(data).hexdigest() != expected:
        raise ValueError(f'SHA-256 mismatch for {name}')
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path, help='New runtime output directory')
    parser.add_argument('--upstream-source', required=True, type=Path,
                        help='Git checkout containing the pinned upstream firmware revision')
    args = parser.parse_args()
    if args.output.exists() or args.output.is_symlink():
        parser.error('choose an output directory that does not exist')

    with urlopen(PACKAGE, timeout=30) as response:
        if response.geturl() != PACKAGE:
            raise ValueError('Unexpected npm package redirect')
        archive = response.read(MAX_PACKAGE_BYTES + 1)
    if len(archive) > MAX_PACKAGE_BYTES:
        raise ValueError('Exceeded the npm package size limit')
    verify('npm package', archive, PACKAGE_SHA256)

    files = {}
    with tarfile.open(fileobj=io.BytesIO(archive), mode='r:gz') as package:
        for name, expected in RUNTIME_FILES.items():
            member = package.getmember(f'package/build/{name}')
            if not member.isfile():
                raise ValueError(f'Unexpected tar member type for {name}')
            with package.extractfile(member) as source:
                files[name] = verify(name, source.read(), expected)

    git = ['git', '-C', args.upstream_source.resolve(strict=True)]
    for name, expected in FIRMWARE_FILES.items():
        data = subprocess.check_output([*git, 'show', f'{FIRMWARE_REV}:bios/{name}'])
        files[name] = verify(name, data, expected)

    args.output.mkdir()
    for name, data in files.items():
        (args.output / name).write_bytes(data)


if __name__ == '__main__':
    main()
