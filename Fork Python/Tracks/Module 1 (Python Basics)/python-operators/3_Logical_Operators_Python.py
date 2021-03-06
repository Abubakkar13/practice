#Logical Operators - Python
"""
Logical operators are and, or, not. They are used in condition checking.
Example: a and b checks if both a and b are True. First a is checked then b.
a or b checks if either of a or b is True. If one is True; it doesn't check for other.
not a complements the boolean value of a
Note: 0 and empty string are False and all other values are True.

In this question, you will take two integers as input and print out the output of various logical operations between them.

#Input Format:
The first line of testcase contains T denoting the number of testcases. T testcases follow. Each testcase contains 2 lines of input.

#Output Format:
For each testcase, in a new line, Output the answer.

#Your Task:
Your task is to complete the function logical().

#Constraints:
1 <= T <= 100

#Example:
Input:
1
5
6
Output:
6
5
False
"""

#solution.py
def logical(a,b):

    print(a and b) ## do a and b

    print(a or b) ## do a or b

    print(not a) ## do not a