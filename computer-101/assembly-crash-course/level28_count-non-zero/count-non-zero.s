.intel_syntax noprefix
.global _start
_start:
    xor rax, rax # clear counter of consecutive non-zero bytes
    cmp rdi, 0   # check if rdi is 0
    je done      # if rdi is 0, jump to done

loop:
    movq rdx, [rdi + rax] # load 1st byte
    cmp rdx, 0   # compare if each byte is 0
    je done      # if byte is 0, jump to done
    add rax, 1   # increment counter
    jmp loop     # continue loop

done: