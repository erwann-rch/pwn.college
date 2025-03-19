# Level Description
```
hacker@assembly-crash-course~memory-size-access:~/asm_courses$ /challenge/run memory-size-access.elf 

We will now set some values in memory dynamically before each run. On each run
the values will change. This means you will need to do some type of formulaic
operation with registers. We will tell you which registers are set beforehand
and where you should put the result. In most cases, its rax.

In this level you will be working with memory. This will require you to read or write
to things stored linearly in memory. If you are confused, go look at the linear
addressing module in 'ike. You may also be asked to dereference things, possibly multiple
times, to things we dynamically put in memory for your use.


Recall the following:
  The breakdown of the names of memory sizes:
    Quad Word   = 8 Bytes = 64 bits
    Double Word = 4 bytes = 32 bits
    Word        = 2 bytes = 16 bits
    Byte        = 1 byte  = 8 bits

In x86_64, you can access each of these sizes when dereferencing an address, just like using
bigger or smaller register accesses:
  mov al, [address]        <=>        moves the least significant byte from address to rax
  mov ax, [address]        <=>        moves the least significant word from address to rax
  mov eax, [address]       <=>        moves the least significant double word from address to rax
  mov rax, [address]       <=>        moves the full quad word from address to rax

Please perform the following:
  Set rax to the byte at 0x404000
  Set rbx to the word at 0x404000
  Set rcx to the double word at 0x404000
  Set rdx to the quad word at 0x404000

We will now set the following in preparation for your code:
  [0x404000] = 0x8a887e80cc265703

---------------- CODE ----------------
0x400000:    mov       al, byte ptr [0x404000]
0x400007:    mov       bx, word ptr [0x404000]
0x40000f:    mov       ecx, dword ptr [0x404000]
0x400016:    mov       rdx, qword ptr [0x404000]
--------------------------------------
```

# Solution
```
python memory-size-access.py
```
OR 

```
as memory-size-access.s -o memory-size-access.o; ld memory-size-access.o -o memory-size-access.elf; /challenge/run memory-size-access.elf
```

# Flag
`pwn.college{kS7ulnGoJuQBt-SIRFdi1kc4x-m.dRTM4MDL5YTNzEzW}`


