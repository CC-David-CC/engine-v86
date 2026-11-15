# Checked-in browser Linux runtime

These are the exact v86 runtime and firmware files used by the current
Simplified preview. They are intentionally checked in so another machine can
run the guest without this workstation's private download cache. The guest
image itself is the single image named in `../../assets/terminal/v2/image.json`.
Older images and intermediate builds are not part of this runtime.

`scripts/serve-connected.py` uses these files when a complete locally rebuilt
`active-system/.build/v86` is absent. A complete local rebuild takes precedence
for development. The checked-in `image.json` selects the guest image separately.
Linux home remains temporary and separate from the account-backed My files.

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
