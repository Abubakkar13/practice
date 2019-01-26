#Jumping through While - Python
"""
Given a positive integer x, the task is to print the numbers from 1 to x in the order as 12, 22, 32, 42, 52, ... (in increasing order).

Input Format:
First line of input contains number of testcase T. For each testcase, there will be a single line of input containing a positive integer x.

Output Format:
For each testcase, in a new line, print the numbers in increasing order seperated be space.

Your Task:
This is a function problem. You need to complete the function printIncreasingPower.

Constraints:
1 <= T <= 100
2 <= x <= 103

Example:
Input:
1
10

Output:
1 4 9

Explanation:
From  to 10, numbers in powers of 2 are, 1^2, 2^2, 3^2 as 1, 4 and 9.
"""

#solution.py
def printIncreasingPower(x):

    i=1
    # Loop to jump in powers of 2

    while((i*i)<=x):
        ##Your code here

        
print ((i*i), end = " ")

    i=i+1
