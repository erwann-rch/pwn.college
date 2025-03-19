import pwn

pwn.context.update(arch="amd64", os="linux")
code = pwn.asm("""
.intel_syntax noprefix
.global _start
_start:
    mov rax, 0  # reset counter
    mov rsi,rdi # move the input source into the arg (of foo)
    cmp rsi,0 # first check : if the arg is 0
    je exit

while_loop:
    mov rbx, [rsi]  # load string into rbx
    cmp rbx, 0 # second check : if the string is 0
    je exit

    cmp rbx,0x5a # third check : if the arg is lower than 0x5a
    jg skip

    mov rdi,rbx # set the arg for foo function

    mov rdx,rax # save the counter into rdx
    mov rcx,0x403000 # call foo
    call rcx
    mov [rsi],rax # stock return into [rsi]
    mov rax,rdx # get back the counter

    inc rax
    jmp skip


skip:
    inc rsi # next byte
    jmp while_loop

exit:
    ret
""")

process = pwn.process("/challenge/run")
process.send(code)
print(process.recvall().decode())
