       -----------====== CHALLENGE ======-----------

Makefiles are used to automate the build process of (traditionally) 
executable files. Unfortunately, sometimes the programs have weird
requirements... 

In this exercise, you have to automate the building process of 
a strange application that contains a different C file
every month. For example, to build the app in January you would run:
 > gcc -c January.c -o January.o
 > gcc strange_app.c January.o -o strange_app

If instead you build it again in March, the command becomes
 > gcc -c March.c -o March.o
 > gcc strange_app.c March.o -o strange_app

Write a simple makefile to build the application.
Note that the .o file has to be re-generated only when the
corresponding .c file changed, and the strange_app binary 
has to be regenerated only when either the .o file or the 
strange_app.c file changed.

          -----------======  HELP ======-----------

Check out the "date" command to get the name of the current month

         -----------====== SUBMISSION ======-----------

Submit your make file. It will be tested by running "make" from
the same directory where the makefile and the sources are located.
