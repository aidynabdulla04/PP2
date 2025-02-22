def square(n):
    for i in range(1, n+1):
        yield i*i

def even(n):
    for i in range(0, n+1):
        if(i%2==0):
            yield i
n=int(input())
e = even(n)
for i in e:
    print(i,end=",")
print()

def div(n):
    for i in range(0, n+1):
        if(i%3==0):
            if(i%4==0):
                yield i

def squares(a,b):
    for i in range(a, b+1):
        yield i*i
a=int(input())
b=int(input())
sq=squares(a,b)
for i in sq:
    print(i,end=",")
print()

def numbers(n):
    while(n!=-1):
        yield n
        n=n-1
n=int(input())
nums=numbers(n)
for i in nums:
    print(i,end=",")