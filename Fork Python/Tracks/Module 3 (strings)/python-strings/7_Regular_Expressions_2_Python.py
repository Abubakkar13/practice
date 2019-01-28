#Regular Expressions 2 - Python
"""
In this question, we'll use Regex to validate a password. You will be provided a string str which you have to validate.

The validation rules are as follows:

The string is valid only if it starts with lowercase characters, followed by special characters !@#$% followed by numbers.
In any other case the string is not valid.
#Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains one line of input containing str.

#Output Format:
For each testcase, in a new line, print True or False.

#Your Task:
This is a function problem. Do not take input. Complete the function validate that takes str as input.

#Constraints:
1 <= T <= 100

#Example:
Input:
1
asdsab@!@234
Output:
True

#Explanation:
Testcase1: The string is valid as characters are followed by special case characters which are then followed by numbers.
"""

#solution.py
def validate(str):

    pat= r"[a-z]+[!@#$%]+[1-9]+"

    match=re.search(pat,str)

    if(match):

        return True

    else:

        return False