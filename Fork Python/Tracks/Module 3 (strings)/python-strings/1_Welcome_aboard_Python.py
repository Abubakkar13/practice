#Welcome aboard - Python
"""
This module talks about Strings in Python. String in Python is immutable (cannot be edited). You have learnt about seperators in Python. Let's start String with first question given below:

Given name of a person, the task is to welcome the person by printing the name with "Welcome". If name is "John", you should print "Welcome John".

#Input Format:
First line of input contains number of testcases T. For each testcase, there will be a single line containing name of the person.

#Output Format:
For each testcase, in a new line, print Welcome Name.

#Your Task:
This is a function problem. You need to complete the function welcomeAboard and print the required string.

#Constraints:
1 <= T <= 100
1 <= |Name| <= 100

#Example:
Input:
John
Python

Output:
Welcome John
Welcome Python
"""

#solution.py
def welcomeAboard(name):

    print ("Welcome " +name)
