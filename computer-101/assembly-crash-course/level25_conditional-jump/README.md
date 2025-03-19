# Level Description
```
hacker@assembly-crash-course~conditional-jump:~/asm_courses$ /challenge/run conditional-jump.elf 

In this level you will be working with control flow manipulation. This involves using instructions
to both indirectly and directly control the special register `rip`, the instruction pointer.
You will use instructions such as: jmp, call, cmp, and their alternatives to implement the requested behavior.

We will be testing your code multiple times in this level with dynamic values! This means we will
be running your code in a variety of random ways to verify that the logic is robust enough to
survive normal use.


We will now introduce you to conditional jumps--one of the most valuable instructions in x86.
In higher level programming languages, an if-else structure exists to do things like:
  if x is even:
    is_even = 1
  else:
   is_even = 0

This should look familiar, since it is implementable in only bit-logic, which you've done in a prior level.

In these structures, we can control the program's control flow based on dynamic values provided to the program.

Implementing the above logic with jmps can be done like so:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
; assume rdi = x, rax is output
; rdx = rdi mod 2
mov rax, rdi
mov rsi, 2
div rsi
; remainder is 0 if even
cmp rdx, 0
; jump to not_even code is its not 0
jne not_even
; fall through to even code
mov rbx, 1
jmp done
; jump to this only when not_even
not_even:
mov rbx, 0
done:
mov rax, rbx
; more instructions here
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Often though, you want more than just a single 'if-else'.

Sometimes you want two if checks, followed by an else.

To do this, you need to make sure that you have control flow that 'falls-through' to the next `if` after it fails.

All must jump to the same `done` after execution to avoid the else.

There are many jump types in x86, it will help to learn how they can be used.

Nearly all of them rely on something called the ZF, the Zero Flag.

The ZF is set to 1 when a cmp is equal. 0 otherwise.

Using the above knowledge, implement the following:
  if [x] is 0x7f454c46:
    y = [x+4] + [x+8] + [x+12]
  else if [x] is 0x00005A4D:
    y = [x+4] - [x+8] - [x+12]
  else:
    y = [x+4] * [x+8] * [x+12]

where:
  x = rdi, y = rax.

Assume each dereferenced value is a signed dword.
This means the values can start as a negative value at each memory position.

A valid solution will use the following at least once:
  jmp (any variant), cmp

We will now run multiple tests on your code, here is an example run:
  (data) [0x404000] = {4 random dwords}
  rdi = 0x404000

Executing your code...
---------------- CODE ----------------
0x400000:    cmp       dword ptr [rdi], 0x7f454c46
0x400006:    je        0x40001d
0x400008:    cmp       dword ptr [rdi], 0x5a4d
0x40000e:    je        0x400012
0x400010:    jmp       0x400028
0x400012:    mov       eax, dword ptr [rdi + 4]
0x400015:    sub       eax, dword ptr [rdi + 8]
0x400018:    sub       eax, dword ptr [rdi + 0xc]
0x40001b:    jmp       0x400035
0x40001d:    mov       eax, dword ptr [rdi + 4]
0x400020:    add       eax, dword ptr [rdi + 8]
0x400023:    add       eax, dword ptr [rdi + 0xc]
0x400026:    jmp       0x400035
0x400028:    mov       eax, dword ptr [rdi + 4]
0x40002b:    imul      eax, dword ptr [rdi + 8]
0x40002f:    imul      eax, dword ptr [rdi + 0xc]
0x400033:    jmp       0x400035
--------------------------------------
```

# Solution
```
python conditional-jump.py
```
OR 

```
as conditional-jump.s -o conditional-jump.o; ld conditional-jump.o -o conditional-jump.elf; /challenge/run conditional-jump.elf
```

# Flag
`pwn.college{Ai1wsRSbkVH0E3e7VyFJAqhMG1x.0VMxIDL5YTNzEzW}`


