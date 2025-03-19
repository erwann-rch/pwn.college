from pwn import *
context.update(arch="amd64", os="linux")
code = asm("""
.intel_syntax noprefix
.global _start
_start:
mov al, dil
mov bx, si
""" )
process = process("/challenge/run")
process.send(code)
print(process.recvall().decode())