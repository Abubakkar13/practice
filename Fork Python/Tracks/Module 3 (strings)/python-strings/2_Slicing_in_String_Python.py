#Slicing in String - Python
"""
Here we'll talk about the novel and perhaps tantalizing concept of slicing. Slicing is the process through which you can extract some continuous part of a string. For example: string is "python", let's use slicing in this. Slicing can be done as:

a. string[0:2] = py (Slicing till index 1)
b. string[0:] = python (Slicing till last index)
c. string[0:4] = pyth (Slicing till index 3)
d. string[0:-2] = pyth (Slicing till index -3(which is index 3)).
Note: -1 indexing starts from last of any string.

Now, lets look into this through a question. Given a string of braces named bound_by, and a string named tag_name. The task is to print a new string such that tag_name is in the middle of bound_by. For example, bound_by : "<<>>" and tag_name : "body", so, new string should be ""<<body>>"(without quotes)

#Input Format:
First line of input contains number of testcases T. For each testcase, there will be a single line containing bound_by and tag_name seperated by space.

#Output Format:
For each testcase, in a new line, print the new modified string as described.

#User Task:
The task is to complete the function join_middle() which should return the modified string.

#Constraints:
1 <= T <= 100
1 <= |tag_name| <= 103

#Example:
Input:
2
<> body
[[]] tag

Output:
<body>
[[tag]]

#Explanation:
Testcase 2: tag is in the middle of [[]], so new string formed is [[tag]].
"""

#solution.py
def join_middle(bound_by, tag_name):

    b=len(bound_by)

    t=int(b/2)
  # complete the statement below to return the string as required

    return bound_by[0:t] + tag_name + bound_by[t: ]

