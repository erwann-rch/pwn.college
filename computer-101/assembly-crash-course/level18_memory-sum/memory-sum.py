import pwn
pwn.context.update(arch="amd64", os="linux")
code = pwn.asm("""
.intel_syntax noprefix
.global _start
_start:
mov eax, [rdi]
mov ebx, [rdi+8]
add eax, ebx
mov [rsi], rax
""" )
process = pwn.process("/challenge/run")
process.send(code)
print(process.recvall().decode())