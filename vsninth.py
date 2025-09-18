#x=eval(input("Enter a data:"))
#print(x,type(x))


'''x,y=input("Enter first number:"),input("Enter second number:")
print(x,y)'''


#x,y=input("Enter two numbers:").split(' ')
#print(x,y)


'''x,y,z=input("Enter a date:").split('/')
print(x,y,z)'''


'''x=input("Tell me about yourself:")
y=x.split()
print(y)'''


'''x,y,z=[int(i) for i in input("Enter 3 numbers:").split()]
print(x,y,z,type(x))'''


'''x,y,z=[eval(g) for g in input("Enter 3 numbers:").split()]
print(x,y,z,type(x))'''


'''t1=list([eval(g) for g in input("Enter 3 numbers:").split()])
print(t1,type(t1))'''


#t2=tuple([eval(g) for g in input("Enter 3 numbers:").split()])
#print(t2,type(t2))


'''d1=dict(input().split('-') for x in range(3))
print(d1)'''


'''d2={input("Enter a key:"):input("Enter a value:") for x in range(3)}
print(d2)'''


#Variable length keyword argument
def fun1(**k):
    print(k,type(k))
fun1(ajay=34,vijay=46,rajesh=67)
fun1(name="rakesh",age=22,height=178,roll=44,num="number") 