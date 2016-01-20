      -----------====== CHALLENGE ======-----------
      
The goal of this assignment is to add one command to gdb named "pstruct"
that prints an area of memory according to the fields specified by the user.
The command (that has to be written in python) should take two parameters, 
the first representing the memory address and the second the format string 
specifying the fields. 
The supported fields should include:
 i = integer (4 bytes)
 l = long (8 bytes)
 f = float (4 bytes)
 s = pointer to a null-terminated string
 p = pointer
 n = a pointer to another element of the same type 
 . = skip one word

In case the format string contains an "n", and it is value is different
from 0, then the command needs to follow the pointer and also print
the same information for that address, recursively.

       -----------====== EXAMPLE ======-----------

Compile the test.c program.
Then save your code in a file called solution.py and execute
the following test:

   $ gdb test
   (gdb) source solution.py
   (gdb) b 40
   Breakpoint 1 at 0x4006c2: file test.c, line 40.
   (gdb) run
   ....
   (gdb) p &b
   $1 = (big *) 0x7fffffffe8c0
   (gdb) p head
   $2 = (elem *) 0x602030
   (gdb) pstruct 0x7fffffffe8c0 i.ifps
   -------------
   > 2
   > 1000
   > 3.1400001049
   > 0x7fffffffe8c4
   > "Saturn"
   -------------
   
   (gdb) pstruct 0x602030 ni
   -------------
   > 2
   -------------
   > 4
   -------------
   > 8
   -------------

Note that the pointer values can be different in your case.




