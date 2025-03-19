# Level Description
```
hacker@assembly-crash-course~absolute-jump:~/asm_courses$ /challenge/run absolute-jump.elf 

We will now set some values in memory dynamically before each run. On each run
the values will change. This means you will need to do some type of formulaic
operation with registers. We will tell you which registers are set beforehand
and where you should put the result. In most cases, its rax.

In this level you will be working with control flow manipulation. This involves using instructions
to both indirectly and directly control the special register `rip`, the instruction pointer.
You will use instructions such as: jmp, call, cmp, and their alternatives to implement the requested behavior.


Earlier, you learned how to manipulate data in a pseudo-control way, but x86 gives us actual
instructions to manipulate control flow directly.

There are two major ways to manipulate control flow:
 through a jump;
 through a call.

In this level, you will work with jumps.

There are two types of jumps:
  Unconditional jumps
  Conditional jumps

Unconditional jumps always trigger and are not based on the results of earlier instructions.

As you know, memory locations can store data and instructions.

Your code will be stored at 0x40003b (this will change each run).

For all jumps, there are three types:
  Relative jumps: jump + or - the next instruction.
  Absolute jumps: jump to a specific address.
  Indirect jumps: jump to the memory address specified in a register.

In x86, absolute jumps (jump to a specific address) are accomplished by first putting the target address in a register reg, then doing jmp reg.

In this level we will ask you to do an absolute jump.

Perform the following:
  Jump to the absolute address 0x403000

We will now set the following in preparation for your code:
  Loading your given code at: 0x40003b

You ran me without an argument. You can re-run with `/challenge/run /path/to/your/elf` to input an ELF file, or just give me your assembled and extracted code in bytes (up to 0x1000 bytes): 
Executing your code...
---------------- CODE ----------------
0x40003b:    mov       rax, 0x403000
0x400042:    jmp       rax
--------------------------------------
```

# Solution
```
python absolute-jump.py
```
OR 

```
as absolute-jump.s -o absolute-jump.o; ld absolute-jump.o -o absolute-jump.elf; /challenge/run absolute-jump.elf
```

# Flag
`pwn.college{snht4nFrv6gjWwPx6_9F20bW6G0.dVTM4MDL5YTNzEzW}`


