mov rdx, 0x0 ; set rdx to 0
mov rax, [rsp]
add rax, [rsp+2]
add rax, [rsp+4]
add rax, [rsp+6]
mov rbx, 0x4 ; set the rbx to the divisor (here 4)             
div rbx
push rax ; push the result into the stack