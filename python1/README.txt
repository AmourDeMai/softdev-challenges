       -----------====== CHALLENGE ======-----------

From the history of your browswer you extracted a simple log
file that contains each URL your visited with the corresponding
referer (i.e., the page you came from).
An example of this output is saved in the test.log file.

The goal of this exercise is to write a little python script
that parses this log file and prints the sequence of pages
you visited to reach a certain destination (if more than
one sequence exists, it is enough to print one).

The python script should read the log entries from the standard input
and receive the target page as first and only parameter.

For example, this is what the output of your program should look like:

> cat test.log | python solution.py https://tools.ietf.org/html/rfc7231

1. https://www.google.fr/
2. https://en.wikipedia.org/wiki/Main_Page
3. https://en.wikipedia.org/wiki/HTTP_referer
4. https://tools.ietf.org/html/rfc7231


         -----------====== SUBMISSION ======-----------

Make sure that you tested the previous command and that you get EXACTLY
the same output. If so, submit your python file. 
