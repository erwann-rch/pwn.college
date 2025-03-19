import pwn
pwn.context.update(arch="amd64", os="linux")
code = pwn.asm("""
.intel_syntax noprefix
.global _start
_start:
mov rax, 0xdeadbeef00001337  ; store it into a register to be able to load into the memory
mov [rdi], rax
mov rax, 0xc0ffee0000  ; store it into a register to be able to load into the memory
mov [rsi], rax
""" )
process = pwn.process("/challenge/run")
process.send(code)
print(process.recvall().decode())