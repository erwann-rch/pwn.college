# Level Description
```
hacker@assembly-crash-course~relative-jump:~/asm_courses$ /challenge/run relative-jump.elf 

We will now set some values in memory dynamically before each run. On each run
the values will change. This means you will need to do some type of formulaic
operation with registers. We will tell you which registers are set beforehand
and where you should put the result. In most cases, its rax.

In this level you will be working with control flow manipulation. This involves using instructions
to both indirectly and directly control the special register `rip`, the instruction pointer.
You will use instructions such as: jmp, call, cmp, and their alternatives to implement the requested behavior.


Recall that for all jumps, there are three types:
  Relative jumps
  Absolute jumps
  Indirect jumps

In this level we will ask you to do a relative jump.

You will need to fill space in your code with something to make this relative jump possible.

We suggest using the `nop` instruction. It's 1 byte long and very predictable.

In fact, the as assembler that we're using has a handy .rept directive that you can use to
repeat assembly instructions some number of times:
  https://ftp.gnu.org/old-gnu/Manuals/gas-2.9.1/html_chapter/as_7.html

Useful instructions for this level:
  jmp (reg1 | addr | offset) ; nop

Hint: for the relative jump, lookup how to use `labels` in x86.

Using the above knowledge, perform the following:
  Make the first instruction in your code a jmp
  Make that jmp a relative jump to 0x51 bytes from the current position
  At the code location where the relative jump will redirect control flow set rax to 0x1

We will now set the following in preparation for your code:
  Loading your given code at: 0x4000a7

Executing your code...
---------------- CODE ----------------
0x4000a7:    jmp       0x4000fa
0x4000a9:    nop       
0x4000aa:    nop       
0x4000ab:    nop       
0x4000ac:    nop       
0x4000ad:    nop       
0x4000ae:    nop       
0x4000af:    nop       
0x4000b0:    nop       
0x4000b1:    nop       
0x4000b2:    nop       
0x4000b3:    nop       
0x4000b4:    nop       
0x4000b5:    nop       
0x4000b6:    nop       
0x4000b7:    nop       
0x4000b8:    nop       
0x4000b9:    nop       
0x4000ba:    nop       
0x4000bb:    nop       
0x4000bc:    nop       
0x4000bd:    nop       
0x4000be:    nop       
0x4000bf:    nop       
0x4000c0:    nop       
0x4000c1:    nop       
0x4000c2:    nop       
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
0x4000fa:    mov       rax, 1
--------------------------------------
```

# Solution
```
python relative-jump.py
```
OR 

```
as relative-jump.s -o relative-jump.o; ld relative-jump.o -o relative-jump.elf; /challenge/run relative-jump.elf
```

# Flag
`pwn.college{8okYNNJbqmcxV235Z18XWRpkPsJ.dZTM4MDL5YTNzEzW}`


