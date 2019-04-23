Copy the end

# You are given a string str of length >=2. You need to extract the last 2 characters and print a new string that has the extracted characters 3 times concatenated.

# Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains a string str.

# Output Format:
For each testcase, in a new line, print the newstring.

# Your Task:
This is a function problem. Do not take any input. Just complete the function copyCat and return the newstring.

# Constraints:
1 <= T <= 100

# Example:
Input:
1
cat

# Output:
atatat

# solution

{
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        str=input()
        print(copyCat(str))
        testcases-=1
        
if __name__=='__main__':
    main()
}

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#User function Template for python3
def copyCat(str):
    ##Your code here
    N=len(str)
    strA=str[N-2:]
    return strA*3