import pwn
pwn.context.update(arch="amd64", os="linux")
code = pwn.asm("""
.intel_syntax noprefix
.global _start
_start:
jmp label
.rept 0x51
nop
.endr
label :
mov rax, 0x1
""" )
process = pwn.process("/challenge/run")
process.send(code)
print(process.recvall().decode())