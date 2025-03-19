.intel_syntax noprefix
.global _start
_start:
mov rbx, [rax]
mov rcx, [rbx]
mov rdi, [rcx]
mov rax, 60
syscall