#Is and In Operator
"""
Moving on, Lets introduce 3 more operators in python, is, is not & in.

'is' and 'is not' operators are coding equivalents of '==' and '!='  respectively. However, there are some minor differences that will be covered in the second module.
'in' operator is used to check if something is in some other thing, like 5 in range(2,6). It's useful in loops.
There is List (no need to know about it now, we would be covering it afterwards) of numbers num_list, and some integer queries Q. You need to tell if the numbers are present in the list or not, by outputing True or False.

#Input Format:
First line of input contains number of testcases T. For each testcase, the first line will contain list of numbers, and second line will contain queries.

#Output Format:
For each query, in a new line, print True or False, depending on input.

#Your Task:
This is a function problem, you don't need to take any input. Complete the function number_present() and return True or False.

#Example:
Input:
1
1 2 3 4 5 6 7 8 9 10
3 6 8 12

Output:
True
True
True
False

#Explanation:
Testcase 1: Since 3, 6, 8 are preset in the given list and 12 is not present.

#solution.py

def number_present(num, query):

    #num is a 'list', query is a 'int'

    for i in range(len(num)):
    #write this here - i in range(len(num))

                             # see the use of 'in' in for loop

        if (num[i] is query) : #write this here - num[i] is query

                             # see the use of 'is' as equal to

            return True

    return False
