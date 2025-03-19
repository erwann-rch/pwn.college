import pwn
pwn.context.update(arch="amd64", os="linux")
code = pwn.asm("""
.intel_syntax noprefix
.global _start
_start:
    cmp dword ptr [rdi], 0x7f454c46
    je first_ok
    cmp dword ptr [rdi], 0x00005A4D
    je two_ok
    jmp first_not_ok

first_ok:
    mov eax, [rdi+4]
    add eax, [rdi+8]
    add eax, [rdi+12]
    jmp done

two_ok:
    mov eax, [rdi+4]
    sub eax, [rdi+8]
    sub eax, [rdi+12]
    jmp done
             
first_not_ok:
    mov eax, [rdi+4]
    imul eax, [rdi+8]
    imul eax, [rdi+12]
    jmp done

done:
"""
)
process = pwn.process("/challenge/run")
process.send(code)
print(process.recvall().decode())