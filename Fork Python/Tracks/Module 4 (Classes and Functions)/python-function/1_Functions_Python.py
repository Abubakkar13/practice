#Functions - Python
"""
This whole module deals with functions and methods in Python. Python functions are identified by the def keyword. You've been completing functions for quite a while now, so this time let's try to write a function from scratch.

In this questions, you'll be given a function isPrime to create. The function should take a number n as parameter and return True if n is prime. Return False in other cases.

#Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains 1 line of input n.

#Output Format:
For each testcase, in a new line, you need to print True if n is prime; else print False

#Your Task:
This is a function problem. You don't need to take inputs. Create a function isPrime that takes n as input and returns True for prime n, and False in other cases.

#Constraints:
1 <= T <= 100
1 <= n <= 108

#Example:
Input:
1
5
Output:
True
"""

#solution.py
def isPrime(n):

    for i in range(2,int(n**0.5)+1):

        if n%i==0:

            return False


    return True