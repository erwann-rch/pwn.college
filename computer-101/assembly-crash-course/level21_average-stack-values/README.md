# Level Description
```
hacker@assembly-crash-course~average-stack-values:~/asm_courses$ /challenge/run average-stack-values.elf 

We will now set some values in memory dynamically before each run. On each run
the values will change. This means you will need to do some type of formulaic
operation with registers. We will tell you which registers are set beforehand
and where you should put the result. In most cases, its rax.

In this level you will be working with the stack, the memory region that dynamically expands
and shrinks. You will be required to read and write to the stack, which may require you to use
the pop and push instructions. You may also need to use the stack pointer register (rsp) to know
where the stack is pointing.


In the previous levels you used push and pop to store and load data from the stack.

However you can also access the stack directly using the stack pointer.

On x86, the stack pointer is stored in the special register, rsp.
rsp always stores the memory address of the top of the stack,
i.e. the memory address of the last value pushed.

Similar to the memory levels, we can use [rsp] to access the value at the memory address in rsp.

Without using pop, please calculate the average of 4 consecutive quad words stored on the stack.

Push the average on the stack.

Hint:
  RSP+0x?? Quad Word A
  RSP+0x?? Quad Word B
  RSP+0x?? Quad Word C
  RSP      Quad Word D

We will now set the following in preparation for your code:
  (stack) [0x7fffff200000:0x7fffff1fffe0] = ['0xd474ec4', '0x1fbaf765', '0x231e9c69', '0x2cb22b60'] (list of things)

Executing your code...
---------------- CODE ----------------
0x400000:    mov       rdx, 0
0x400007:    mov       rax, qword ptr [rsp]
0x40000b:    add       rax, qword ptr [rsp + 8]
0x400010:    add       rax, qword ptr [rsp + 0x10]
0x400015:    add       rax, qword ptr [rsp + 0x18]
0x40001a:    mov       rbx, 4
0x400021:    div       rbx
0x400024:    push      rax
--------------------------------------
```

# Solution
```
python average-stack-values.py
```
OR 

```
as average-stack-values.s -o average-stack-values.o; ld average-stack-values.o -o average-stack-values.elf; /challenge/run average-stack-values.elf
```

# Flag
`pwn.college{I6ww1S0YL1CsKqL4fIsAHWBvifc.0VOwIDL5YTNzEzW}`


