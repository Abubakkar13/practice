#Zero Converter - Python
"""
You are given a number n. The number n can be negative or positive. If n is negative, print numbers from n to 0 by adding 1 to n. If positive, print numbers from n-1 to 0 by subtracting 1 from n.

#Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains a single line of input containing n.

#Output Format:
For each testcase, in a new line, print the output.

#Your Task:
This is a function problem. You don't need to take input of testcases. Just complete the functions pos and neg

#Constraints:
1 <= T <= 100

#Example:
Input:
3
0
4
-3
Output:
already Zero
3 2 1 0
-3 -2 -1 0
"""

#solution.py
def pos(n):

    ## Write the code

    for i in range(n-1,-1,-1):

        print(i, end=" ")




def neg(n):

    ##Write the code

    for i in range(n,1):
 
        print(i,end=" ")
