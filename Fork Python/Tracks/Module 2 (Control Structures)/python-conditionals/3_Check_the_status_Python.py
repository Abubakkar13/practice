# Check the status - Python
"""
Given two integer variables a and b, and a flag which is boolean. The task is to check the status and return accordingly.
Return "True" if either a or b (one of them) is positive. Except if the flag is True, then return True only if both of the variables a and b are negative.

# Input Format:
First line of input contains number of testcases T. For each testcase, first line of input contains integer a and next line contains integer b, and last line contains status of flag either True or False.

# Output Format:
For each testcase, print True or False accordingly.

# Your Task:
This is a function problem. Complete the function checkStatus() and return True or False according to the parameters.

# Constraints:
1 <= T <= 100
-106 <= a, b <= 106

# Example:
Input:
1
1
-1
False

# Output:
True

# Explanation:
Testcase 1: Since a and b are positive and negative respectively and parameter is False, so return True.
"""
#solution.py

def check_status(a, b, status):
    
##Your code here
    
##Either True or False is returned
    
    if status==True:
        
        return (a<0 and b<0)
    
    else:
        
        if (a>0 and b>0):
            
            return False
       
    else:
            
        return (a>0 or b>0)