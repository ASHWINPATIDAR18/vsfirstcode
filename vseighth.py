'''p=1
for i in range(1,5):
    for j in range(1,8):
        if j>=(5-i) and j<=(3+i):
            print(p,end='')
        else:
            print('',end='')
    print()'''


'''p=1
for i in range(1,5):
    for j in range(1,8):
        if j>=(5-i) and j<=(3+i):
            print(p,end='')
            p=p+1
        else:
            print('',end='')
    print()
    p=1'''


#Prime Numbers
'''x=int(input("Enter a number:"))
for i in range(2,x):
    if x%2==0:
        print("Not Prime")
        break
else:
    print("Prime")'''


#WAPP to print prime number between range()
'''p=int(input("Enter starting range:"))
q=int(input("Enter ending range:"))
for x in range(p,q):
    for i in range(2,x):
        if x%i==0:
            break
    else:
        print(x,end=' ')'''


p=int(input("Enter starting range:"))
q=int(input("Enter ending range:"))
h=[]
for x in range(p,q):
    for i in range(2,x):
        if x%i==0:
            break
    else:
        print(x,end=' ')
        h.append(x)

print()
print()
print()
length=len(h)
mid=length//2
print(h[mid]+h[mid-1])