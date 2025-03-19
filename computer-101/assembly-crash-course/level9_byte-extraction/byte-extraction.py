from pwn import *
context.update(arch="amd64", os="linux")
code = asm("""
.intel_syntax noprefix
.global _start
_start:
shl rdi, 24
shr rdi, 56
mov rax, rdi
""" )
process = process("/challenge/run")
process.send(code)
print(process.recvall().decode())