import pwn
pwn.context.update(arch="amd64", os="linux")
code = pwn.asm("""
.intel_syntax noprefix
.global _start
_start:
    cmp rdi, 3
    jnbe default
    jmp [rsi + rdi * 8]
 default:
    jmp [rsi + 4 * 8]
"""
)
process = pwn.process("/challenge/run")
process.send(code)
print(process.recvall().decode())