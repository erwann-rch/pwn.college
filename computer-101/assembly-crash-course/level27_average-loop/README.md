# Level Description
```
hacker@assembly-crash-course~average-loop:~/asm_courses$ /challenge/run average-loop.elf 

We will now set some values in memory dynamically before each run. On each run
the values will change. This means you will need to do some type of formulaic
operation with registers. We will tell you which registers are set beforehand
and where you should put the result. In most cases, its rax.

In this level you will be working with control flow manipulation. This involves using instructions
to both indirectly and directly control the special register `rip`, the instruction pointer.
You will use instructions such as: jmp, call, cmp, and their alternatives to implement the requested behavior.


In a previous level you computed the average of 4 integer quad words, which
was a fixed amount of things to compute, but how do you work with sizes you get when
the program is running?

In most programming languages a structure exists called the
for-loop, which allows you to do a set of instructions for a bounded amount of times.
The bounded amount can be either known before or during the programs run, during meaning
the value is given to you dynamically.

As an example, a for-loop can be used to compute the sum of the numbers 1 to n:
  sum = 0
  i = 1
  while i <= n:
    sum += i
    i += 1

Please compute the average of n consecutive quad words, where:
  rdi = memory address of the 1st quad word
  rsi = n (amount to loop for)
  rax = average computed

We will now set the following in preparation for your code:
  [0x4040c0:0x404360] = {n qwords}
  rdi = 0x4040c0
  rsi = 84

Executing your code...
---------------- CODE ----------------
0x400000:    xor       rcx, rcx
0x400003:    xor       rax, rax
0x400006:    mov       rdx, qword ptr [rdi + rcx*8]
0x40000a:    add       rax, rdx
0x40000d:    add       rcx, 1
0x400011:    cmp       rcx, rsi
0x400014:    jb        0x400006
0x400016:    jmp       0x400018
0x400018:    mov       rbx, rsi
0x40001b:    xor       rdx, rdx
0x40001e:    div       rbx
--------------------------------------
```

# Solution
```
python average-loop.py
```
OR 

```
as average-loop.s -o average-loop.o; ld average-loop.o -o average-loop.elf; /challenge/run average-loop.elf
```

# Flag
`pwn.college{4lXKzyxNt1hCCg2EIFNfCsYG4_6.01MxIDL5YTNzEzW}`


