# Neighbor of 10
"""
Given a non-negative number n, print True if n is within 2 of a multiple of 10,  else print false.

#Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains a number n.

#Output Format:
For each testcase, in a new line, print True if conditions are met; else print False.

#Your Task:
This is a function problem. Do not take any input. Just complete the function isNeighbor

#Constraints:
1 <= T <= 100
3 <= n <= 1018

#Example:
Input:
4
3
9
13
22
Output:
False
True
False
True

"""
#solution.py

{

#Initial Template for Python 3

//Position this line where user code will be pasted.

def main():
    
    testcases=int(input()) #testcases
    
    while(testcases>0):
        
        n=int(input())
        
        print(isNeighbor(n))
        
        testcases-=1
        

if __name__=='__main__':
    
    main()

}


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

def isNeighbor(num):
    
    return not(2 < (num % 10) < 8)