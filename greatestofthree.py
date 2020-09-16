#check the greatest of three numbers 

a = int(input("Enter 1st no. ->  "))
b = int(input("Enter 2nd no. ->  "))
c = int(input("Enter 3rd no. ->  "))

if a > b and a > c:
    greatest = a
elif b > a and b > c:
    greatest = b
else:
    greatest = c

print(greatest)
