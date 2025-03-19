.intel_syntax noprefix
.global _start
_start:
# Socket
# socket(AF_INET, SOCK_STREAM, 0)
mov rax, 41 # syscall number for socket
mov rdi, 2  # AF_INET
mov rsi, 1  # SOCK_STREAM
mov rdx, 0  # Protocol (0 for default)
syscall              

mov rbx, rax # Save file descritptor (FD) into rbx

# prepare struct sockaddr_in in registers
# struct sockaddr_in {
#     sa_family_t    sin_family; /* address family: AF_INET */
#     in_port_t      sin_port;   /* port in network byte order */
#     struct in_addr sin_addr;   /* internet address */
# };

sub rsp, 16 # Stack alignment to avoid SEGFAULT on syscall (only 16-multiple are able to call syscall)

mov WORD PTR [rsp], 2          # sin_family = AF_INET (0x02)
mov WORD PTR [rsp + 2], 0x5000 # sin_port = 80 (in network byte order: 0x5000)
mov DWORD PTR [rsp + 4], 0     # sin_addr.s_addr = INADDR_ANY (0.0.0.0)


y# bind(sockfd, &sockaddr, sizeof(sockaddr))
mov rax, 49          # syscall number for bind
mov rdi, rbx         # socket FD
mov rsi, rsp         # sockaddr pointer (pushed on stack)
mov rdx, 16          # sizeof(sockaddr)
syscall

# Exit
mov rdi, 0
mov rax, 60
syscall