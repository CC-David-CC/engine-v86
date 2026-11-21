global _start

%include "header.inc"

    movapd xmm1, [double_values]
    movapd xmm2, [double_operands]
    addsubpd xmm1, xmm2
    addsubpd xmm2, [double_values]

    movaps xmm3, [single_values]
    movaps xmm4, [single_operands]
    addsubps xmm3, xmm4
    addsubps xmm4, [single_values]

%include "footer.inc"

section .data
align 16
double_values: dq 8.0, -3.0
double_operands: dq 2.0, 4.0
single_values: dd 8.0, -3.0, 5.0, 1.0
single_operands: dd 2.0, 4.0, -7.0, -6.0
