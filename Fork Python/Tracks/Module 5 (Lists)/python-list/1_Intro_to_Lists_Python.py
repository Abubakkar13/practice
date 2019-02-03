#Intro to Lists - Python
"""
Lists in Python is used to store data at every index starting from 0. Lists  in Python works similarly to strings, it uses len() function to find the length, and it uses square brackets [ ] to access data. For eg. if we have list arr = [1, 2, 3, 4, 5], then a[0] = 1, a[1] = 2, a[2] = 3 and so on... Let's get it more clearly through the question below:

Given an array (list) of integers A, the task is to check if first or last element in array A is 0.

Input Format:
First line of input contains number of testcases T. For each testcase, first line of input contains length of list and next line contains N integers to be inserted into list.

Output Format:
For each testcase, print "Yes" if first or last element in list is 0, else print "No".

Constraints:
1 <= T <= 100
1 <= N <= 105
1 <= A[i] <= 106

User Task:
The task is to complete the function check_zero(), which returns true if first or last element is 0, else returns false.

Example:
Input:
2
5
0 1 2 3 0
6
2 3 4 5 1 0

Output:
Yes
Yes

Explanation:
Testcase 1: First and last element of list is 0, so output is "Yes".
Testcase 2: Last element of list is 0, so output is "Yes".
"""

#solution.py
def check_zero(size_array, arr):

    
    # complete the if statement to check

    # if first or last element in list is 0

    if(arr[0]==0 or arr[size_array-1]==0 ):

        return True

    else:

        return False
