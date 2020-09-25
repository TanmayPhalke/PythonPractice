import math

x = float(input("Enter point x: "))
y = float(input("Enter point y: "))
r = float(input("Enter Radius: "))

hypotenuse = math.sqrt(pow(x,2 + pow(y,2)))

if hypotenuse <= r:
    print("Point belongs to the circle! ")
else:
    print("Point doesnt belong to the circle")
