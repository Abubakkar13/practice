Lambda sum
"""
You are given two numbers x and y. print the sum of x and y

Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains 2 lines of input containing x and y.

Output Format:
For each testcase, in a new line, print the sum of x and y.

Your Task:
This is a function problem, you don't need to output anything. Just complete lambda function to sum the x and y

Constraints:
1 <= T <= 100

Examples:
Input:
1
2
3
Output:
5
"""

# solution
{
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        x=int(input())
        y=int(input())
        
        print(sum(x,y))
        
        testcases-=1
        
if __name__=='__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
##Write your lambda function here that will be assigned to sum
sum=lambda x,y:x+y