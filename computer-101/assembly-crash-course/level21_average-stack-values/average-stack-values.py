import pwn
pwn.context.update(arch="amd64", os="linux")
code = pwn.asm("""
.intel_syntax noprefix
.global _start
_start:
mov rdx, 0x0 ; set rdx to 0
mov rax, [rsp]
add rax, [rsp+2]
add rax, [rsp+4]
add rax, [rsp+6]
mov rbx, 0x4 ; set the rbx to the divisor (here 4)             
div rbx
push rax ; push the result into the stack
""" )
process = pwn.process("/challenge/run")
process.send(code)
print(process.recvall().decode())