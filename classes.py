import math
class MyStr:

    def getString(self):
        str=input()
        self.str=str
        print(self.str)

    def printString(self):
        print(self.str.upper())

class Shape:
    area_s=0
    def area(self):
        print(self.area_s)
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        print(self.length*self.length)
class Rectangle(Shape):
    def __init__(self, length,width):
        self.length = length
        self.width = width
    def area(self):
        print(self.length*self.width)

class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def show(self):
        print("X:", self.x)
        print("Y:", self.y)
    def move(self, x, y):
        self.x=x
        self.y=y
    def dist(self, x, y):
        d=(x-self.x)**2+(y-self.y)**2
        d=math.sqrt(d)
        print("Distance:",d)

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposite(self, dep):
        self.balance+=dep
    def withdraw(self, wit):
        if(self.balance>=wit):
            self.balance-=wit
        else:
            print("Error: your balance is very low")
def filter(n):
    a = int(math.sqrt(n) + 1)
    for i in range(2, a):
        if (n % i == 0):
            return False
    return True
list=[1,2,3,4,5,6,7,8,9,10,11]
for i in list:
    if(filter(i)):
        print(i)
