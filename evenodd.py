#check if a number is even or odd :)

def checkevenodd(n):
    if n % 2 == 0:
        print("The number is EVEN")
    else:
        print("The number is ODD")

n = float(input("Enter the number to check: "))
checkevenodd(n)
