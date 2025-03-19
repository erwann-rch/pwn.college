.intel_syntax noprefix
.global _start
_start:
mov rbx, [rax]
mov rdi, [rbx]
mov rax, 60
syscall