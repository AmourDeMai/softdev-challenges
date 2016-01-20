    -----------====== The Story  ======--------------
 
CommandLineFu (http://www.commandlinefu.com) is a website in which, on a
daily basis, users post useful shell commands. Other users can then vote on
each command to express the fact that they find it useful, or down-vote it
if they find it useless.  The file "command_line_fu.example.html" in the
current directory contains a dump of the webpage.

  -----------====== The Challenge  ======--------------

The goal of this assignment is to parse the example file and print only
those commands with a number of votes >= 5 (the votes are expressed in the
html in a <div class="num-votes"> tag).  
You can use any command-line tools you want for this assignment, but you
cannot use python.

   -----------====== Submission  ======--------------

Write your commands in a file called "solution.sh" 
Then test if it works by running:
 > cat command_line_fu.example.html | sh solution.sh
The output should look like the one saved in the file "solution.example" in
the current directory.
If so, you can proceed and submit your solution file 



