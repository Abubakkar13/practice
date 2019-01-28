#Regex - Python
"""
Regular expressions are extremely helpful in extracting useful information from loads of text. Regular expressions work on pattern-matching techniques. Extracting phone-number, validating passwords, and extracting images from web-pages are but a few examples of regex usage.

In this question, we'll learn the use of Regex in Python. You will be provided a string str in which you have to find all the numbers and print them.

Note: In Python, you need to import re module to use regex

#Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains one line of input containing str.

#Output Format:
For each testcase, in a new line, print the numbers (separated by spaces) extracted from str. If there are no numbers then print -1.

#Your Task:
This is a function problem. Do not take input. Complete the function numberMatcher that takes str as input.

#Constraints:
1 <= T <= 100

#Example:
Input:
1
asdasd123asmdasdk34234kfdsd34sdfk5
Output:
123 34234 34 5
"""

#solution.py
def numberMatcher(str):

    pat=r"[0-9]+"

    match=re.findall(pat,str)
 ##find all finds all the matched texts and returns a list

    if(match):
 
        for i in match:

            print(i, end=" ")

    else:

        print(-1,end=" ")
