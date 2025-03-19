.intel_syntax noprefix
.global _start
_start:
mov eax, [rdi]
mov ebx, [rdi+8]
add eax, ebx
mov [rsi], rax