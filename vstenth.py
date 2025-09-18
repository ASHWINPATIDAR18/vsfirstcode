#Exception handling
'''print("Hii")
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))

try:
    z=x/y
    print(z)
except ZeroDivisionError:
    print("Why you are dividing with 0")
print("Bye")'''


'''print("Hii")
x=input("Enter first number:")
y=int(input("Enter second number:"))

try:
    z=x/y
    print(z)
except ZeroDivisionError:
    print("Why you are dividing with 0")
except TypeError:
    print("Error")

print("Bye")'''


'''print("Hii")
x=input("Enter first number:")
y=int(input("Enter second number:"))

try:
    z=x/y
    print(z)
except:
    print("Something is wrong")

print("Bye")'''


'''cb=10000
wb=int(input("Enter Amount:"))

try:
    if (cb<wb):
        raise ValueError()
    cb=cb-wb
    print("Money Sent")
    print("Current Bal is:",cb)

except ValueError:
    print("Insufficient Balance")
    print("Current Bal is:",cb)'''


cb=10000
while True:
    wb=int(input("Enter Amount:"))

    try:
        if (cb<wb):
            raise ValueError()
        cb=cb-wb
        print("Money Sent")
        print("Current Bal is:",cb)

    except ValueError:
        print("Insufficient Balance")
        print("Current Bal is:",cb) 