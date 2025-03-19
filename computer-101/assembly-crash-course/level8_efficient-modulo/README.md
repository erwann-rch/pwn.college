# Level Description
```
hacker@assembly-crash-course~efficient-modulo:~/asm_courses$ /challenge/run efficient-modulo.elf 

In this level you will be working with registers. You will be asked to modify
or read from registers.

We will now set some values in memory dynamically before each run. On each run
the values will change. This means you will need to do some type of formulaic
operation with registers. We will tell you which registers are set beforehand
and where you should put the result. In most cases, its rax.


It turns out that using the div operator to compute the modulo operation is slow!

We can use a math trick to optimize the modulo operator (%). Compilers use this trick a lot.

If we have "x % y", and y is a power of 2, such as 2^n, the result will be the lower n bits of x.

Therefore, we can use the lower register byte access to efficiently implement modulo!

Using only the following instruction(s):
  mov

Please compute the following:
  rax = rdi % 256
  rbx = rsi % 65536

We will now set the following in preparation for your code:
  rdi = 0xb437
  rsi = 0x9079e1b5

Extracting binary code from provided ELF file...
Executing your code...
---------------- CODE ----------------
0x400000:       mov     al, dil
0x400003:       mov     bx, si
--------------------------------------
```

# Blocking point
![register parts](register-parts.png)

# Solution
```
python efficient-modulo.py
```
OR 

```
as efficient-modulo.s -o efficient-modulo.o; ld efficient-modulo.o -o efficient-modulo.elf; /challenge/run efficient-modulo.elf
```

# Flag
`pwn.college{M3CNpBNrwBZJrQnCQyQJmz_YwQn.0VO5EDL5YTNzEzW}`
