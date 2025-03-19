# Level Description
```
hacker@assembly-crash-course~memory-sum:~/asm_courses$ /challenge/run memory-sum.elf 

We will now set some values in memory dynamically before each run. On each run
the values will change. This means you will need to do some type of formulaic
operation with registers. We will tell you which registers are set beforehand
and where you should put the result. In most cases, its rax.

In this level you will be working with memory. This will require you to read or write
to things stored linearly in memory. If you are confused, go look at the linear
addressing module in 'ike. You may also be asked to dereference things, possibly multiple
times, to things we dynamically put in memory for your use.


Recall that memory is stored linearly.

What does that mean?

Say we access the quad word at 0x1337:
  [0x1337] = 0x00000000deadbeef

The real way memory is layed out is byte by byte, little endian:
  [0x1337] = 0xef
  [0x1337 + 1] = 0xbe
  [0x1337 + 2] = 0xad
  ...
  [0x1337 + 7] = 0x00

What does this do for us?

Well, it means that we can access things next to each other using offsets,
similar to what was shown above.

Say you want the 5th *byte* from an address, you can access it like:
  mov al, [address+4]

Remember, offsets start at 0.

Perform the following:
  Load two consecutive quad words from the address stored in rdi
  Calculate the sum of the previous steps quad words.
  Store the sum at the address in rsi

We will now set the following in preparation for your code:
  [0x404208] = 0xef089
  [0x404210] = 0x97be4
  rdi = 0x404208
  rsi = 0x404740

Executing your code...
---------------- CODE ----------------
0x400000:    mov       eax, dword ptr [rdi]
0x400002:    add       eax, dword ptr [rdi + 8]
0x400005:    mov       qword ptr [rsi], rax
--------------------------------------
```

# Solution
```
python memory-sum.py
```
OR 

```
as memory-sum.s -o memory-sum.o; ld memory-sum.o -o memory-sum.elf; /challenge/run memory-sum.elf
```

# Flag
`pwn.college{Qn2woEmQsl1T5f2C6pH1lHxavDN.0lNwIDL5YTNzEzW}`


