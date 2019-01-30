#Classes and Objects - Python
"""
After learning functions, the obvious course of action would be to learn Classes. Classes in Python use the class keyword just like the CPP and Java counterparts.

In this question, we'll implement class and create objects.

#Input Format:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains 6 lines of input. The first line is the name of object1. The second line is the hp of object1. The third line is the boost amount for object1. The fourth line is the name of the object2. The fifth line is the hp of oject2. the sixth line is the boost amount for object2.

#Output Format:
For each testcase, in a new line, print the output as directed.

#Your Task:
This is a function problem. You don't need to take any input. Complete the class functions getName and getHp; and also complete the function fusion.
The fusion function takes two objects and returns a third object that has following properties:
name = first-half of obj1 name+ last-half of obj2 name.
hp = hp of obj1+hp of obj2

#Constraints:
1 <= T <= 100
name of op1
1 <= hp of op1 <= 500
1 <= boost of op1 <= 200
name of op2
1 <= hp of op2 <= 500
1 <= boost of op2 <= 200

#Examples:
Input:
1
Spiderman
76
4
Hulk
213
1

#Output:
Spidlk 517

#Explanation:
Testcase1: 
Object1=> Name= Spiderman, Hp= 76*4
Object2=> Name= Hulk, Hp= 213*1
length(Spiderman)/2=4. 4 characters = Spid
length(Hulk)/2=2. 2 characters from end = lk
Object3=> Name= Spid+lk, Hp= 76*4+213*1=517
"""

#solution.py
class Character:

    def __init__(self,name,hp):

        self.name=name ##Assigning name to the current object's name variable

        self.hp=hp ##Assigning hp to the current object's hp variable

    def boost(self,amount):

        self.hp=self.hp*amount ## boosting current object's hp

    def getName(self):

        ##complete this. Return name of the current object

        return(self.name)

    def getHp(self):

        ##complete this. return hp of the current object

        return(self.hp)

def fusion(a,b):

    ##This function takes two Character objects as parameter

    ## Create a new object that has name equal to first-half of a's name + last-half of b's name

    ## Also new object's hp is the sum of a's hp + b's hp

    ##return the newly created object

    l=len(a.name)//2

    ll=len(b.name)//2
 
   name=a.name[:l]+b.name[ll:]

    return(Character(name,a.hp+b.hp))

    

def show(a):
 ##Already completed

    print(a.getName(),a.getHp()) 
