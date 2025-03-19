.intel_syntax noprefix
.global _start
_start:
# Socket
# socket(AF_INET, SOCK_STREAM, 0)
mov rax, 41 # syscall number for socket (x86_64 Linux)
mov rdi, 2  # AF_INET
mov rsi, 1  # SOCK_STREAM
mov rdx, 0  # Protocol (0 for default)
syscall             

# Exit
mov rdi, 0 
mov rax, 60
syscall