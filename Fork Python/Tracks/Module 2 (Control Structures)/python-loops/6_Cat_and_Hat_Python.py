#Cat and Hat - Python
"""
You are given a string str, you need to print True if cat and hat appear same number of times in str, otherwise print False.

Note: str contains only lowercase characters.

Hint: You may use len(str) to get length of string. Also, you can obtain a certain part of the string using string slicing- str[startindex:endindex]

#Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains a single line of input containing str.

#Output Format:
For each testcase, in a new line, print the output.

#Your Task:
This is a function problem. You don't need to take input of testcases. Just complete the function stringJumper that takes str as input.

#Constraints:
1 <= T <= 100

#Example:
Input:
2
catinahat
bazingaa
Output:
True
True

#Explanation:
Testcase1: cat and hat both are present 1 number of times.
Testcase2: cat and hat both are present 0 number of times.
"""

#solution.py
def cat_hat(str):

    hat=str.count("hat")

    cat=str.count("cat")
 
    if hat==cat:

        return "True"

    else:

        return "False"