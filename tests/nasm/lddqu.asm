global _start

%include "header.inc"

    sub esp, 32
    mov dword [esp + 1], 0x01234567
    mov dword [esp + 5], 0x89abcdef
    mov dword [esp + 9], 0x10203040
    mov dword [esp + 13], 0xfedcba98
    lddqu xmm3, [esp + 1]
    add esp, 32

%include "footer.inc"
