import math
print("Input degree: ") 
r=int(input())
r=math.radians(r)
print("Output radian:",r)
print("Height: ")
h=int(input())
print("Base, first value: ")
bf=int(input())
print("Base, second value: ")
bs=int(input())
a=(bs+bf)/2*h
print("Area:",a)
print("Input number of sides: ")
n=int(input())
s=90*(n-2)
s=s/n
print("Input the length of a side: ")
s=math.tanh(s)
l=int(input())
s=s*l/2
ara=l*n*s/2
print("The area of the polygon is:",ara)
print("Length of base: ")
lb=int(input())
print("Height of parallelogram: ")
hp=int(input())
area=hp*lb
print("Area:",area)