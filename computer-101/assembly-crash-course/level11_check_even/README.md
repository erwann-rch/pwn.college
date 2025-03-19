# Level Description
```
hacker@assembly-crash-course~check_even:~/asm_courses$ /challenge/run check_even.elf 

In this level you will be working with registers. You will be asked to modify
or read from registers.

We will now set some values in memory dynamically before each run. On each run
the values will change. This means you will need to do some type of formulaic
operation with registers. We will tell you which registers are set beforehand
and where you should put the result. In most cases, its rax.

In this level you will be working with bit logic and operations. This will involve heavy use of
directly interacting with bits stored in a register or memory location. You will also likely
need to make use of the logic instructions in x86: and, or, not, xor.


Using only the following instructions:
  and, or, xor

Implement the following logic:
  if x is even then
    y = 1
  else
    y = 0

where:
  x = rdi
  y = rax

We will now set the following in preparation for your code:
  rdi = 0x2abf2764

Executing your code...
---------------- CODE ----------------
0x400000:    and       rdi, 1
0x400004:    xor       rax, rax
0x400007:    xor       rdi, 1
0x40000b:    xor       rax, rdi
--------------------------------------
```

# Solution
```
python check_even.py
```
OR 

```
as check_even.s -o check_even.o; ld check_even.o -o check_even.elf; /challenge/run check_even.elf
```

# Flag
`pwn.college{U5pNSs_L26zd3-QvKljOvL0F-jy.0lMwIDL5YTNzEzW}`
