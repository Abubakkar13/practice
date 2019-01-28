#Repeat the Strings - Python
"""
Given two strings a and b. The task is to make a new string where the string with longer length should be in between and the one with shorter length should be outside on front and end. New string should be like shorter+longer+shorter.

#Input Format:
First line of input contains number of testcases T. For each testcase, there will be a single line of input containing strings a and b.

#Output Format:
For each testcase, in a new line, print the new concatenated string.

#Constraints:
1 <= T <= 100
1 <= |a, b| <= 103

#Your Task:
The task is to complete the function combo_string(), which joins short+long+short and returns this new string.

#Example:
Input:
1
Hi There
Output:
HiThereHi

Explanation:
After joining short+long+short, we have new string as "HiThereHi".
"""

#solution.py
def combo_string(a, b):

  
  if len(a) > len (b):

      return b+a+b
# your code here

  else:

      return a+b+a
