#While loop in Python
"""
While loop in Python is same as like in CPP and Java, but, here you have to use ':' to end while statement (used to end any statement). While loop is used to iterate same as for loop, except that in while loop you can customize jump of steps in coupling with variable used to loop, after every iteration, unlike in for loop (you cannot customize jump according to the variable you are using to loop through).

Let's get it more clearly through this question. Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line (use comma seperator).

#Input Format:
First line of input contains number of testcases T. For each testcase, there will be a single line containing the number x.

#Output Format:
For each testcase, print the numbers in decreasing order from x to 0.

#Your Task:
This is a function problem. You need to complete the printInDecreasing function and print the x from x to 0 in a single line.

#Constraints:
1 <= T <= 100
1 <= x <= 106

#Example:
Input:
1
3

Output:
3 2 1 0

#Explanation:
Testcase 1: Numbers in decreasing order from 3 are 3, 2, 1, 0.
"""

#solution.py
def printInDecreasing(x):

   while(x >= 0):

        print(x,end=" ")


        x -= 1
