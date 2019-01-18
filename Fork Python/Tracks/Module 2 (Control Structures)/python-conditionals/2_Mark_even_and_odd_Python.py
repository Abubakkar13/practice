# Mark Even and Odd - Python
"""
# Given a positive integer x. The task is to check if it is even or odd (Any number that given zero as remainder when divided by 2 is an even number)

# Input Format: First line of input contains number of testcases T. For each testcase, there will be a single line containing positive integer x.

# Output Format: For each testcase, output "Odd" if the number is Odd, else "Even".

# Your Task:
The task is to complete the function checkEvenOdd(), which returns True (In python, True starts with caps T) if the number is even, else return False (In Python, False starts with caps F).

# Note: Python functions, just like variables, don't have a datatype keyword preceeding the identifier.

# Constraints:
1 <= T <= 100
1 <= x <= 106

# Example:
Input:
2
4
5

# Output:
Even
Odd

"""
# solution.py
def checkOddEven(x):
    
    if(x % 2 is 0):
          
        return 1
    
    else:
           
        return 0