#Operators in Python
"""
Your are familiar with input, output and data types in Python. Let us move on to play with operators in Python. Operators used widely in Python are '+', '-', '*', '/', '**', '//'.

Now, given two integer value X and Y, the task is to perform some arithematic operations (given below) on these two values.
Arithmetic Operations:
a. Add ("+"): Adding X and Y.
b. Subtract ("-"): Subtracting X and Y.
c. Multiply ("*"): Multiply X and Y.
d. Divide ("/"): Divide X by Y.
e. Multiplying X, Y times ("**"): X raised to power Y.
f. Divide and floor the result ("//"): Divide and result is in integer form.

#Input Format:
First line of input contains number of testcases T. For each testcase, there will be one line of input containing X and Y.

#Output Format:
For each test case, in a new line, perform all the arithematic operation on given X and Y and print their output in seperate line.

#Example:
Input:
1
10 5

#Output:
15
5
50
2
100000
2

#Explanation:
Testcase 1: 
Adding X and Y: 15
Subtracting Y from X: 5
Multiplying X and Y: 50
Divide Y from X: 2.0
X raised to power Y: 100000
Divide Y from X and taking floor value as int: 2
"""

#solution.py

def do_operation(x, y):

    # Your code here

    sum=x+y

    print(sum)

    sub=x-y

    print(sub)

    mul=x*y

    print(mul)

    div=x/y

    print(div)

    su=x**y

    print(su)

    divw=x//y

    print(divw)
