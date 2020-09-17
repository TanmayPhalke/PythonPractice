#check divisiblity of 2 numbers

def checkdivisiblity(x,y):
    if x%y==0:
        divisibleflag = 1
    else:
        divisibleflag = 0
    return divisibleflag

x = int(input("Enter first number -> "))
y = int(input("Enter second number -> "))

flag = checkdivisiblity(x,y)

if flag==1:
    print(x," is divisible by ",y)
else:
    print(x, " is not divisible by ",y)
