.intel_syntax noprefix
.global _start
_start:
mov rbx, [567800]
mov rdi, [rbx]
mov rax, 60
syscall