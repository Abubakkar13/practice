#Taking input and typecasting - Python
"""
You have learned to take string input in python. Now, you'll learn how to take input of int, float, and bool.

In Python, we use the input() function and put this function in either int(), float(), or bool() to typecast the input into required data type. Also, integers, floating-points and boolean variables don't have any range in Python. As long as you have enough memory, you can work with them.

In this question, you will take input of 4 variables that are in separate lines. The first variable is an integer, the second is a string(single/multiple words possible), the third is a floating number, the fourth is a boolean value.
You need to take the inputs and print the outputs.

#Input Format:
The first line of testcase contains T denoting the number of testcases. T testcases follow. Each testcase contains 4 lines of input.

#Output Format:
For each testcase, in a new line, print the inputs and the class of the input.

#Your Task:
Your task is to complete the function inPut().

#Constraints:
1 <= T <= 100

#Example:
Input:
1
56
fdg fgdf
3.43534
True
Output:
56 <class 'int'>
fdg fgdf <class 'str'>
3.43534 <class 'float'>
True <class 'bool'>
"""

#solution.py
def inPut():
    
#Take input and assign the input to a,b,c,d. 
Please also typecast as type() will produce wrong answer without it
    
    a= int(input(""))
    
    b= input("")
    
    c= float(input(""))
    
    d= bool(input(""))
    
    
    print(a, type(a))
    
    print(b, type(b))
    
    print(c, type(c))
    
    print(d, type(d))

