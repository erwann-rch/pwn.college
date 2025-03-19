import pwn
pwn.context.update(arch="amd64", os="linux")
code = pwn.asm("""
.intel_syntax noprefix
.global _start
_start:
push rdi
push rsi
pop rdi
pop rsi
""" )
process = pwn.process("/challenge/run")
process.send(code)
print(process.recvall().decode())