#Taking input - Python
"""
In Python, we use the input() function to take input and assign the input to a variable. In Python, a variable name is not preceeded by its data-type, instead we just use the variable name and python changes its data-type according to the input type.

In this question, you will take input of 3 strings. The strings are in separate lines. You need to take the inputs and print the outputs.

#Input Format:
The first line of testcase contains T denoting the number of testcases. T testcases follow. Each testcase contains 3 lines of input.

#Output Format:
For each testcase, in a new line, Output the strings in a single line after concatenating.

#Your Task:
Your task is to complete the function inPutCat().

#Constraints:
1 <= T <= 100

#Example:
Input:
1
Geeks
For
Geeks
Output:
Geeks For Geeks
"""

#solution.py

def inPutCat():
    
    a=input("") 
    
    b=input("") 
    
    c=input("") 
    
    print(a,b,c) 