# v86 source and retained bootstrap runtime

The upstream engine history and source at cc37f35c43bf14865d74ad76879ecf9410f69eb1 are retained. The separately filtered Desktop-Preview runtime history adds7 exact original file blobs/modes: JS/WASM, firmware, notices and a historical runtime note. Linux kernel/base-image/build-source ownership is apps/linux in the assembly, not a second emulator copy. The old note records its original relative paths and does not select the new build layout.

These retained v860.5.472 inputs let the existing guest start without the old private download cache. Their original hash pins remain recorded in the historical note. A retained compiled runtime is not an independently reproduced engine build. Upstream Makefile/source/native project structure is unchanged; no engine behavior patch or new deployment occurred. Use an explicit build/review branch for future engine work.
