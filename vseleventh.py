'''fp=open("b.txt","w")
print(fp.name)
print(fp.mode)
print(fp.readable())
print(fp.writable())
print(fp)
fp.close()
print(fp.closed)'''


'''fp=open("b.txt","w")
n1=input("Enter Your Name:")
fp.write(n1)
fp.close()'''


'''fp=open("b.txt","w")
l1=["Pune\n","Nashik\n","Beed\n","Akola\n"]
fp.writelines(l1)
fp.close()'''


'''fp=open("b.txt","r")
print(fp.read())
fp.close()'''


'''fp=open("b.txt","r")
print(fp.read(3))
fp.close()'''


fp=open("b.txt","r")
while True:
    k=fp.readline()
    if k=='':
        break
    print(k,end='')
fp.close()