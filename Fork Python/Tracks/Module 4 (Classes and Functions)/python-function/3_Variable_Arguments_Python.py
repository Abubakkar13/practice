#Variable Arguments - Python
"""
Python functions allow us to take variable arguments. The parameter that takes variable argument has a * as prefix.

In this question we will summ the elements taken as variable arguments and print the result.

#Input Fomat:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains 1 line of input containing n.

#Output Format:
For each testcase, in a new line, print the sum of n with elements of variable argument.

#Your Task:
This is a function problem. You don't need to take any input. Just complete the function multivar.

#Constraints:
1 <= T <= 100

#Examples:
Input:
1
6
Output:
28
"""

#solution.py
def multivar(a, *var):
 
    print(a+sum(var))
