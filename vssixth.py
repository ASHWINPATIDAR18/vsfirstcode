#Functions
'''def fun1():
    print("Hello Ashwin")
    print("Hello Friends")
fun1()'''


'''def fun1():
    print("Ram Ram")
    print("Namaste")
print("A")             #normal line
fun1()
fun1()'''


'''def add():
    x=int(input("Enter first number:"))
    y=int(input("Enter second number:"))
    z=x+y
    print("Addition is:",z)
add()        #function call
add()
add()'''


'''def add(p,q):     #formal parameters
    r=p+q
    print("Addition is:",r)

x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
add(x,y)'''          #actual parameter (argument passing)


'''def add(p,q):
    z=p+q
    return z

x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
result=add(x,y)
print("Addition is:",result)'''


def add(p,q):
    z=p+q
    print("Addition is:",z)

x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
result=add(x,y)
print("Addition is:",result)