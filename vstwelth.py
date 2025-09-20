#Recursion
'''def fun1():
    print("Hello",end=' ')
    fun1()

fun1()'''


'''def sum1(n):
    if n==1:
        return 1
    else:
        return n+sum1(n-1)
r=sum1(5)
print("Sum is:",r)'''


'''def fact1(n):
    if n==1:
        return 1
    else:
        return n*fact1(n-1)
    
r=fact1(5)
print("Factorial is:",r)'''


'''def fact1(n):
    if n==1:
        return 1
    else:
        return n*fact1(n-1)
    
while True:
    x=int(input("Enter a number:"))
    r=fact1(x)
    print("Factorial is:",r)'''


#Lambda Expression
'''r=lambda a,b:a+b
p=r(6,7)
print("Sum is:",p)'''


'''r=lambda a,b:a+b
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))

p=r(x,y)
print("Sum is:",p)'''


'''r=lambda a,b:a if a>b else b
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))

p=r(x,y)
print("Greater number is:",p)'''


r=lambda n:1 if n==1 else n*r(n-1)
while True:
    x=int(input("Enter a number:"))
    p=r(x)
    print("Factorial is:",p)