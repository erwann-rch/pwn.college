# Level Description
```
hacker@assembly-crash-course~stack-substraction:~/asm_courses$ /challenge/run stack-substraction.elf 

We will now set some values in memory dynamically before each run. On each run
the values will change. This means you will need to do some type of formulaic
operation with registers. We will tell you which registers are set beforehand
and where you should put the result. In most cases, its rax.

In this level you will be working with the stack, the memory region that dynamically expands
and shrinks. You will be required to read and write to the stack, which may require you to use
the pop and push instructions. You may also need to use the stack pointer register (rsp) to know
where the stack is pointing.


In these levels we are going to introduce the stack.

The stack is a region of memory that can store values for later.

To store a value on the stack we use the push instruction, and to retrieve a value we use pop.

The stack is a last in first out (LIFO) memory structure, and this means
the last value pushed in the first value popped.

Imagine unloading plates from the dishwasher let's say there are 1 red, 1 green, and 1 blue.
First we place the red one in the cabinet, then the green on top of the red, then the blue.

Our stack of plates would look like:
  Top ----> Blue
            Green
  Bottom -> Red

Now, if we wanted a plate to make a sandwich we would retrieve the top plate from the stack
which would be the blue one that was last into the cabinet, ergo the first one out.

On x86, the pop instruction will take the value from the top of the stack and put it into a register.

Similarly, the push instruction will take the value in a register and push it onto the top of the stack.

Using these instructions, take the top value of the stack, subtract rdi from it, then put it back.

We will now set the following in preparation for your code:
  rdi = 0x4811
  (stack) [0x7fffff1ffff8] = 0x148c4e34

Executing your code...
---------------- CODE ----------------
0x400000:    pop       rax
0x400001:    sub       rax, rdi
0x400004:    push      rax
--------------------------------------
```

# Solution
```
python stack-substraction.py
```
OR 

```
as stack-substraction.s -o stack-substraction.o; ld stack-substraction.o -o stack-substraction.elf; /challenge/run stack-substraction.elf
```

# Flag
`pwn.college{ID-icujT833FTjnCtDnVB4CdxQp.01NwIDL5YTNzEzW}`


