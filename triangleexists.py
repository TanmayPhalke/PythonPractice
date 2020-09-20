x = float(input("Enter the length1 of triangle: "))
y = float(input("Enter the length2 of triangle: "))
z = float(input("Enter the length3 of triangle: "))

if x+y>z and x+z>y and y+z>x:
    print("Triangle exists!")
else:
    print("Triangle doesnt exist")
