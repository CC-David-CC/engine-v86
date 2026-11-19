# Optional WebOS v86 runtime

Prepare an upstream v86 checkout containing
`cc37f35c43bf14865d74ad76879ecf9410f69eb1` from the official
[copy/v86 repository](https://github.com/copy/v86). From the WebOS integration
checkout, run:

```sh
python3 webos/prepare-runtime.py output-directory --upstream-source /path/to/upstream/v86
```

Use a new output directory. The script verifies the v86 0.5.472 npm archive and
restores its JavaScript and WASM along with the two firmware files from that
exact upstream revision. The generated directory stays outside Git. The
source checkout includes the firmware license notice.

The optional Linux guest requires a separate kernel and initramfs. See the
WebOS Linux component for the guest image source and the historical image pin.
The normal WebOS viewer can be built without the Linux guest.

The emulator files come from v86 0.5.472, with source revision
`cc37f35c43bf14865d74ad76879ecf9410f69eb1`; BIOS files were taken from that
revision. The kernel came from Debian's `linux-image-6.1.0-54-686`; the guest
image was built with `scripts/build-browser-initramfs.py` and the guest sources
in `scripts/`. The original preparation script records the input pins and the
local build procedure. Notices for v86, BIOS, BusyBox and the kernel are under
`notices/`; the guest image also contains package notices. This record does not
claim a reproducible build or a complete corresponding-source audit.

SHA-256 of the checked-in runtime:

```text
1b41074f7a5604f528dac6842baf7afccd79d7370b97ea3241944c275b67bec1  libv86.js
2f0c4150f266415b754a84a32e6f8e4c975a1d3abb94c78b047fa30027db1ef1  v86.wasm
73e3f359102e3a9982c35fce98eb7cd08f18303ac7f1ba6ebfbe6cdc1c244d98  seabios.bin
a4bc0d80cc3ca028c73dafa8fee396b8d054ce87ebd8abfbd31b06b437607880  vgabios.bin
3d0c734693b5614c665529413aeb339ededd54112c38c463602db932ec43ceae  vmlinuz
e571ca17c12f1b392851b1cc1144aa14abc185c3bac7380d7c24821073e6e389  ../../assets/terminal/v2/e571ca17c12f1b392851b1cc1144aa14abc185c3bac7380d7c24821073e6e389.cpio.gz
```
