.intel_syntax noprefix
.global _start
_start:
# read
mov rdi, 0
mov rsi, 1337000
mov rdx, 8
mov rax, 0
syscall
# write
mov rdi, 1
mov rsi, 1337000
mov rdx, 8
mov rax, 1
syscall
# exit
mov rdi, 42
mov rax, 60
syscall