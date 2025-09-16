'''def fun1(x,y,z=0):
    print(x+y+z)

fun1(10,20)
fun1(11,22,33)'''


''' fun1(*g):
    print(g)
    h=list(g)
    print(h)
fun1(10)
fun1(10,20)
fun1(10,20,30)
fun1(10,20,30,40,50,60,70,80,90,100,110,120,130,140,150)'''


#star pattern

'''for i in range(5)
   print("*",end='')'''


'''for i in range(5):
    print("A",end='')
    for j in range(3):
        print("B",end='')
    print()'''
       

'''for i in range(1,6):
    for j in range(1,6):
        if j<=i:
            print("*",end='')
        else:
            print('',end='')
    print()'''


'''for i in range(1,6):
    for j in range(1,6):
        if j>=i:
            print("*",end='')
        else:
            print('',end='')
    print()'''


'''for i in range(1,6):
    for j in range(1,6):
        if j<=(6-i):
            print("*",end='')
        else:
            print('',end='')
    print()'''


for i in range(1,5):
    for j in range(1,8):
        if j>=(5-i) and j<=(3+i):
            print("*",end='')
        else:
            print('',end='')
    print()