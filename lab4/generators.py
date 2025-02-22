# 1. Create a generator that generates the squares of numbers up to some number
def square(n):
    for i in range(1, n+1):
        yield i*i
# 2. Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even(n):
    for i in range(0, n+1):
        if(i%2==0):
            yield i
n=int(input())
e = even(n)
for i in e:
    print(i,end=",")
print()
# 3. Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def div(n):
    for i in range(0, n+1):
        if(i%3==0):
            if(i%4==0):
                yield i
# 4. Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a,b):
    for i in range(a, b+1):
        yield i*i
a=int(input())
b=int(input())
sq=squares(a,b)
for i in sq:
    print(i,end=",")
print()
# 5. Implement a generator that returns all numbers from (n) down to 0.
def numbers(n):
    while(n!=-1):
        yield n
        n=n-1
n=int(input())
nums=numbers(n)
for i in nums:
    print(i,end=",")