#Bitwise Operators - Python
"""
Bitwise operators are useful when we want to work with bits. Here, we'll take a look at them.
Given three positive integers a, b and c. Your task is to perform some bitwise operations on them as given below:
1. d = a ^ a
2. e = c ^ b
3. f = a & b
4. g = c | (a ^ a)
5. e = ~e
Note: ^ is for xor.

#Input Format:
First line of input contains number of testcases. For each testcase, there will be 3 line containing a, b and c.

#Output Format:
For each testcase, output the result of operations performed in all the above given 5 steps in new lines.

#Your Task:
This is a function problem. You don't need to take input. Just complete the function bitwise that takes a b c as input.

#Constraints:
1 <= T <= 100
1 <= a, b, c <= 106

#Example:
Input:
1
4
8
2

#Output:
0
10
0
2
-11
"""

#solution.py

def bitwise(a,b, c):

    print(a ^ a)

    print(c ^ b)

    print(a & b)

    print(c|(a^a))

    print(~(c^b))