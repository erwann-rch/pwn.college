# Level Description
```
hacker@assembly-crash-course~swap-stack-value:~/asm_courses$ /challenge/run swap-stack-value.elf 

We will now set some values in memory dynamically before each run. On each run
the values will change. This means you will need to do some type of formulaic
operation with registers. We will tell you which registers are set beforehand
and where you should put the result. In most cases, its rax.

In this level you will be working with the stack, the memory region that dynamically expands
and shrinks. You will be required to read and write to the stack, which may require you to use
the pop and push instructions. You may also need to use the stack pointer register (rsp) to know
where the stack is pointing.


In this level we are going to explore the last in first out (LIFO) property of the stack.

Using only following instructions:
  push, pop

Swap values in rdi and rsi.
i.e.
If to start rdi = 2 and rsi = 5
Then to end rdi = 5 and rsi = 2

We will now set the following in preparation for your code:
  rdi = 0x3af250f5
  rsi = 0x324a8d11

Executing your code...
---------------- CODE ----------------
0x400000:    push      rdi
0x400001:    push      rsi
0x400002:    pop       rdi
0x400003:    pop       rsi
--------------------------------------
```

# Solution
```
python swap-stack-value.py
```
OR 

```
as swap-stack-value.s -o swap-stack-value.o; ld swap-stack-value.o -o swap-stack-value.elf; /challenge/run swap-stack-value.elf
```

# Flag
`pwn.college{IC28X3DAxS0Ql3MeYKPoLy3PI0p.0FOwIDL5YTNzEzW}`


