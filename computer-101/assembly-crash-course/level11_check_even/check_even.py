from pwn import *
context.update(arch="amd64", os="linux")
code = asm("""
.intel_syntax noprefix
.global _start
_start:
and rdi,1       ; check if LSB (meaning rdi is odd)
xor rax, rax    ; clear rax (rax = 0 after this)
xor rdi, 1      ; set rdi to opposite 
xor rax, rdi    ; set rax to rdi
""" )
process = process("/challenge/run")
process.send(code)
print(process.recvall().decode())