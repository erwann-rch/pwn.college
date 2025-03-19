# Level Description
```
hacker@assembly-crash-course~jump-trampoline:~/asm_courses$ /challenge/run jump-trampoline.elf 

We will now set some values in memory dynamically before each run. On each run
the values will change. This means you will need to do some type of formulaic
operation with registers. We will tell you which registers are set beforehand
and where you should put the result. In most cases, its rax.

In this level you will be working with control flow manipulation. This involves using instructions
to both indirectly and directly control the special register `rip`, the instruction pointer.
You will use instructions such as: jmp, call, cmp, and their alternatives to implement the requested behavior.


Now, we will combine the two prior levels and perform the following:
  Create a two jump trampoline:
    Make the first instruction in your code a jmp
    Make that jmp a relative jump to 0x51 bytes from its current position
    At 0x51 write the following code:
      Place the top value on the stack into register rdi
      jmp to the absolute address 0x403000

We will now set the following in preparation for your code:
  Loading your given code at: 0x4000c1
  (stack) [0x7fffff1ffff8] = 0x3a

Executing your code...
---------------- CODE ----------------
0x4000c1:    jmp       0x400114
0x4000c3:    nop       
0x4000c4:    nop       
0x4000c5:    nop       
0x4000c6:    nop       
0x4000c7:    nop       
0x4000c8:    nop       
0x4000c9:    nop       
0x4000ca:    nop       
0x4000cb:    nop       
0x4000cc:    nop       
0x4000cd:    nop       
0x4000ce:    nop       
0x4000cf:    nop       
0x4000d0:    nop       
0x4000d1:    nop       
0x4000d2:    nop       
0x4000d3:    nop       
0x4000d4:    nop       
0x4000d5:    nop       
0x4000d6:    nop       
0x4000d7:    nop       
0x4000d8:    nop       
0x4000d9:    nop       
0x4000da:    nop       
0x4000db:    nop       
0x4000dc:    nop       
0x4000dd:    nop       
0x4000de:    nop       
0x4000df:    nop       
0x4000e0:    nop       
0x4000e1:    nop       
0x4000e2:    nop       
0x4000e3:    nop       
0x4000e4:    nop       
0x4000e5:    nop       
0x4000e6:    nop       
0x4000e7:    nop       
0x4000e8:    nop       
0x4000e9:    nop       
0x4000ea:    nop       
0x4000eb:    nop       
0x4000ec:    nop       
0x4000ed:    nop       
0x4000ee:    nop       
0x4000ef:    nop       
0x4000f0:    nop       
0x4000f1:    nop       
0x4000f2:    nop       
0x4000f3:    nop       
0x4000f4:    nop       
0x4000f5:    nop       
0x4000f6:    nop       
0x4000f7:    nop       
0x4000f8:    nop       
0x4000f9:    nop       
0x4000fa:    nop       
0x4000fb:    nop       
0x4000fc:    nop       
0x4000fd:    nop       
0x4000fe:    nop       
0x4000ff:    nop       
0x400100:    nop       
0x400101:    nop       
0x400102:    nop       
0x400103:    nop       
0x400104:    nop       
0x400105:    nop       
0x400106:    nop       
0x400107:    nop       
0x400108:    nop       
0x400109:    nop       
0x40010a:    nop       
0x40010b:    nop       
0x40010c:    nop       
0x40010d:    nop       
0x40010e:    nop       
0x40010f:    nop       
0x400110:    nop       
0x400111:    nop       
0x400112:    nop       
0x400113:    nop       
0x400114:    pop       rdi
0x400115:    mov       rax, 0x403000
0x40011c:    jmp       rax
--------------------------------------
```

# Solution
```
python jump-trampoline.py
```
OR 

```
as jump-trampoline.s -o jump-trampoline.o; ld jump-trampoline.o -o jump-trampoline.elf; /challenge/run jump-trampoline.elf
```

# Flag
`pwn.college{UWRX9OLtFVgyfSTPJ21S_CWwrpe.0FMxIDL5YTNzEzW}`


