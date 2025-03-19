# Level Description
```
hacker@assembly-crash-course~bitwise-and:~/asm_courses$ /challenge/run bitwise-and.elf 

In this level you will be working with registers. You will be asked to modify
or read from registers.

We will now set some values in memory dynamically before each run. On each run
the values will change. This means you will need to do some type of formulaic
operation with registers. We will tell you which registers are set beforehand
and where you should put the result. In most cases, its rax.

In this level you will be working with bit logic and operations. This will involve heavy use of
directly interacting with bits stored in a register or memory location. You will also likely
need to make use of the logic instructions in x86: and, or, not, xor.


Bitwise logic in assembly is yet another interesting concept!
x86 allows you to perform logic operations bit by bit on registers.

For the sake of this example say registers only store 8 bits.

The values in rax and rbx are:
  rax = 10101010
  rbx = 00110011

If we were to perform a bitwise AND of rax and rbx using the
"and rax, rbx" instruction, the result would be calculated by
ANDing each bit pair 1 by 1 hence why it's called a bitwise
logic.

So from left to right:
  1 AND 0 = 0
  0 AND 0 = 0
  1 AND 1 = 1
  0 AND 1 = 0
  ...

Finally we combine the results together to get:
  rax = 00100010

Here are some truth tables for reference:
      AND          OR           XOR
   A | B | X    A | B | X    A | B | X
  ---+---+---  ---+---+---  ---+---+---
   0 | 0 | 0    0 | 0 | 0    0 | 0 | 0
   0 | 1 | 0    0 | 1 | 1    0 | 1 | 1
   1 | 0 | 0    1 | 0 | 1    1 | 0 | 1
   1 | 1 | 1    1 | 1 | 1    1 | 1 | 0

Without using the following instructions:
  mov, xchg

Please perform the following:
  rax = rdi AND rsi

i.e. Set rax to the value of (rdi AND rsi)

We will now set the following in preparation for your code:
  rdi = 0x56fc9e60fa091ab9
  rsi = 0x7e84c9e13a75ca9c

You ran me without an argument. You can re-run with `/challenge/run /path/to/your/elf` to input an ELF file, or just give me your assembled and extracted code in bytes (up to 0x1000 bytes): 
Executing your code...
---------------- CODE ----------------
0x400000:    and       rax, rdi
0x400003:    and       rax, rsi
--------------------------------------
```

# Solution
```
python bitwise-and.py
```
OR 

```
as bitwise-and.s -o bitwise-and.o; ld bitwise-and.o -o bitwise-and.elf; /challenge/run bitwise-and.elf
```

# Flag
`pwn.college{Ago8tdYX66jzlb9TjHiSDpcRw7f.0VMwIDL5YTNzEzW}`
