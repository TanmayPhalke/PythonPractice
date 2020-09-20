x = float(input("Enter point x: "))
y = float(input("Enter point y: "))

if x>0 and y>0:
    print("First quadrant")
elif x<0 and y>0:
    print("Second quadrant")
elif x < 0 and y < 0:
    print("Third quadrant")
elif x>0 and y<0:
    print("Fourth quadrant")
elif x==0 and y==0:
    print("Origin")
elif x==0:
    print("x point")
elif y==0:
    print("y point")
