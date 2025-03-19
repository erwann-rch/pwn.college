.intel_syntax noprefix
.global _start
_start:
    xor rcx, rcx ; clear counter
    xor rax, rax
               
loop:
    movq rdx, [rdi + rcx*8] ; load temp data to a register
    add rax, rdx
               
    add rcx, 1 ; add 1 to counter
               
    cmp rcx, rsi
    jb loop
    jmp done

done:   
    mov rbx, rsi ; divide rax by rsi
    xor rdx, rdx ; clear rdx for division
    div rbx