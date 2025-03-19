from pwn import *
context.update(arch="amd64", os="linux")
code = asm("""
.intel_syntax noprefix
.global _start
_start:
mov rax, [0x404000]
""" )
process = process("/challenge/run")
process.send(code)
print(process.recvall().decode())