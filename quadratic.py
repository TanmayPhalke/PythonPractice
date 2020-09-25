import math

x = float(input("Enter the value of point x: "))
y = float(input("Enter the value of point y: "))
z = float(input("Enter the value of point z: "))

a = y*y-4*x*z

if a>0:
    x1 = (-y + math.sqrt(a)) / (2 * x)
    x2 = (-y - math.sqrt(a)) / (2 * x)
    print("x1 = %.2f; x2 = %.2f" % (x1, x2))
elif a == 0:
    x1 = -y/(2*x)
    print("x1 = $.2f" % x1)
else:
    print("Roots don't exist...")
