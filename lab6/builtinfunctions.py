import time
import math

#Write a Python program with builtin function to multiply all the numbers in a list
def multiple(l):
    x=iter(l)
    sum=int(1)
    while True:
        try:
            sum=sum*next(x)
        except StopIteration:
            print(sum)
            break
multiple([1,2,3,4,5,6,7])
#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def count(s):
    up=int(0)
    lw=int(0)
    for i in s:
        if(i.isupper()):
            up=up+1
        else:
            lw=lw+1
    print("upper case letters: "+str(up))
    print("lower case letters: "+str(lw))
count("SDakjsdSDADaskjs")
#Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def palindrome(s):
    l=len(s)
    ll=int(l/2)
    for i in range(0,ll):
        if(s[i]!=s[l-i-1]):
            print(s+" is not palindrome")
            return
    print(s+" is palindrome")
palindrome("1235321")
#Write a Python program that invoke square root function after specific milliseconds.
def square():
    num=int(input())
    t=int(input())
    time.sleep(t/1000)
    print("Square root of "+str(num)+" after "+str(t)+" miliseconds is "+str(math.sqrt(num)))
#Write a Python program with builtin function that returns True if all elements of the tuple are true.
def check(tup):
    for t in tup:
        if(str(type(t)).find('bool')!=-1):
            if(not t):
                return False
        else:
            return False
    return True
tuple3 = (True, True, True)
print(check(tuple3))    

