import pwn
pwn.context.update(arch="amd64", os="linux")
code = pwn.asm("""
.intel_syntax noprefix
.global _start
_start:
mov 0x404000, [rax]
""" )
process = pwn.process("/challenge/run")
process.send(code)
print(process.recvall().decode())