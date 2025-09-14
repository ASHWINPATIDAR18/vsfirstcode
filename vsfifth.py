#set
'''s1={11,22,33,44,55,66,11,22,11,55,33}    #can't put duplicate data
s2={55,66,77,88}
s1.update(s2)
print(s1)'''


'''s1={1,2,3,4,5}
s2={4,5,6}
#s1.union(s2)
#p=s1.intersection(s2)
#p=s1.discard(7)
#p=s1.remove(3)
print(p)'''


'''d1={1,2,3,4,5,6} #dictionary
d2={2,3,4}
#q=d1.issubset(d2)
#r=d2.issubset(d1)
s=d1.issuperset(d2)

print(s)'''


#k1={}
#print(type(k1))

#k1=set()
#print(type(k1))


'''s1=33,44,55,66
l1=list(s1)

#l2=list(77,88,99)     #should only pass 1 argument that's why Error
l2=list([77,88,99])

print(l2)'''


#Dictionary
'''d1={"Carname":"Toyota","Year":"1998","Name":"Ashwin"}
print(d1)'''


'''p=1234
c=0
while c!=3:
    c=c+1
    pin=int(input("Enter a pin:"))
    if pin==p:
        print("Transaction Successful")
        break
    else:
        print("Incorrect Pin")
else:
    print("Card Blocked")'''


d1={45:"Amit",81:"Ajay","Age":18,"Weight":50}
#print(d1)

for i in d1:
    print(i,d1[i],sep=' ')