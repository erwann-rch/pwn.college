import pwn
pwn.context.update(arch="amd64", os="linux")
code = pwn.asm("""
.intel_syntax noprefix
.global _start
_start:
mov al, [0x404000]
mov bx, [0x404000]
mov ecx, [0x404000]
mov rdx, [0x404000]
""" )
process = pwn.process("/challenge/run")
process.send(code)
print(process.recvall().decode())