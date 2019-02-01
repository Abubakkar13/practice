#Anonymous Functions - Python
"""
Python functions allows us to create anonymous functions using the lambda keyword. These functions are small one line functions that don't use the def keyword.

In this question we will create an anonymous function to print a to power b.

#Input Fomat:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains 2 lines of input containing a and then b.

#Output Format:
For each testcase, in a new line, print ab.

#Your Task:
This is a function problem. You don't need to take any input. Just complete the anonymous function power.

#Constraints:
1 <= T <= 100

#Examples:
Input:
1
6
2
Output:
36
"""

#solution.py

power = lambda a, b : a ** b