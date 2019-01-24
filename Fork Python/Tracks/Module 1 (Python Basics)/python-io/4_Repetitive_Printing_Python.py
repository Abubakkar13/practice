#Repetitive Printing - Python
"""
Now you are familiar with printing single output. But, there may be times when you need to print the same string multiple times. In other languages, this task can be solved using Loops, however, Python provides us a special functionality to achieve this. We use the '*' operator to multiply a string by a positive integer 'x' to print it x number of times.

Hint: Use "*" to print any string multiple times. "geek" * 2 = geek geek

#Input Format:
1
Geeks
5

#Output Format:
Geeks Geeks Geeks Geeks Geeks

#Explanation:
Testcase 1: The word "Geeks " is printed 5 times without loops.
"""

#solution.py
def print_fun(string, x):
    

    print(string * x,sep=' ')
