.intel_syntax noprefix
.global _start
_start:
mov rax, [0x404000]
addq rax, 0x1337 ;The 'q' suffix means that the operation is performed on 64-bit values (quadword).