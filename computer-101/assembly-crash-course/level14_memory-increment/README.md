# Level Description
```
hacker@assembly-crash-course~memory-increment:~/asm_courses$ /challenge/run memory-increment.elf 

We will now set some values in memory dynamically before each run. On each run
the values will change. This means you will need to do some type of formulaic
operation with registers. We will tell you which registers are set beforehand
and where you should put the result. In most cases, its rax.

In this level you will be working with memory. This will require you to read or write
to things stored linearly in memory. If you are confused, go look at the linear
addressing module in 'ike. You may also be asked to dereference things, possibly multiple
times, to things we dynamically put in memory for your use.


Please perform the following:
  Place the value stored at 0x404000 into rax
  Increment the value stored at the address 0x404000 by 0x1337

Make sure the value in rax is the original value stored at 0x404000 and make sure
that [0x404000] now has the incremented value.

We will now set the following in preparation for your code:
  [0x404000] = 0x178733

Executing your code...
---------------- CODE ----------------
0x400000:    mov       rax, qword ptr [0x404000]
0x400008:    add       qword ptr [0x404000], 0x1337
--------------------------------------
```

# Solution
```
python memory-increment.py
```
OR 

```
as memory-increment.s -o memory-increment.o; ld memory-increment.o -o memory-increment.elf; /challenge/run memory-increment.elf
```

# Flag
`pwn.college{gFbUZZKcNAa-Z6fy_LEAYTIqdk0.01MwIDL5YTNzEzW}`


