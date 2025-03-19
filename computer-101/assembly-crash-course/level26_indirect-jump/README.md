# Level Description
```
hacker@assembly-crash-course~indirect-jump:~/asm_courses$ /challenge/run indirect-jump.elf 

In this level you will be working with control flow manipulation. This involves using instructions
to both indirectly and directly control the special register `rip`, the instruction pointer.
You will use instructions such as: jmp, call, cmp, and their alternatives to implement the requested behavior.

We will be testing your code multiple times in this level with dynamic values! This means we will
be running your code in a variety of random ways to verify that the logic is robust enough to
survive normal use.


The last jump type is the indirect jump, which is often used for switch statements in the real world.

Switch statements are a special case of if-statements that use only numbers to determine where the control flow will go.

Here is an example:
  switch(number):
    0: jmp do_thing_0
    1: jmp do_thing_1
    2: jmp do_thing_2
    default: jmp do_default_thing

The switch in this example is working on `number`, which can either be 0, 1, or 2.

In the case that `number` is not one of those numbers, the default triggers.

You can consider this a reduced else-if type structure.

In x86, you are already used to using numbers, so it should be no suprise that you can make if statements based on something being an exact number.

In addition, if you know the range of the numbers, a switch statement works very well.

Take for instance the existence of a jump table.

A jump table is a contiguous section of memory that holds addresses of places to jump.

In the above example, the jump table could look like:
  [0x1337] = address of do_thing_0
  [0x1337+0x8] = address of do_thing_1
  [0x1337+0x10] = address of do_thing_2
  [0x1337+0x18] = address of do_default_thing

Using the jump table, we can greatly reduce the amount of cmps we use.

Now all we need to check is if `number` is greater than 2.

If it is, always do:
  jmp [0x1337+0x18]
Otherwise:
  jmp [jump_table_address + number * 8]

Using the above knowledge, implement the following logic:
  if rdi is 0:
    jmp 0x403030
  else if rdi is 1:
    jmp 0x4030c8
  else if rdi is 2:
    jmp 0x4031b5
  else if rdi is 3:
    jmp 0x403284
  else:
    jmp 0x40334a

Please do the above with the following constraints:
  Assume rdi will NOT be negative
  Use no more than 1 cmp instruction
  Use no more than 3 jumps (of any variant)
  We will provide you with the number to 'switch' on in rdi.
  We will provide you with a jump table base address in rsi.

Here is an example table:
  [0x404066] = 0x403030 (addrs will change)
  [0x40406e] = 0x4030c8
  [0x404076] = 0x4031b5
  [0x40407e] = 0x403284
  [0x404086] = 0x40334a

Executing your code...
---------------- CODE ----------------
0x400000:    cmp       rdi, 3
0x400004:    ja        0x400009
0x400006:    jmp       qword ptr [rsi + rdi*8]
0x400009:    jmp       qword ptr [rsi + 0x20]
--------------------------------------
Completed test 10
Completed test 20
Completed test 30
Completed test 40
Completed test 50
Completed test 60
Completed test 70
Completed test 80
Completed test 90
Completed test 100
```

# Solution
```
python indirect-jump.py
```
OR 

```
as indirect-jump.s -o indirect-jump.o; ld indirect-jump.o -o indirect-jump.elf; /challenge/run indirect-jump.elf
```

# Flag
`pwn.college{gZn4kc8gQb7UdCDHrWTztu-AcTV.0lMxIDL5YTNzEzW}`


