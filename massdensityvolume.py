opt = int(input("Choose an option:\n 1. Mass \n 2. Density \n 3. Volume \n 4. Exit \n"))
if opt == 1:
    density = int(input("Enter Density: "))
    volume = int(input("Enter Volume: "))
    mass = density*volume
    print("Mass = ",mass)
elif opt == 2:
    mass = int(input("Enter Mass: "))
    volume = int(input("Enter Volume: "))
    density = mass/volume
    print("Density = ",density)
elif opt == 3:
    mass = int(input("Enter Mass: "))
    density = int(input("Enter Density: "))
    volume = mass/density
    print("Volume = ",volume)
elif opt == 4:
    print("Exiting :) ")
else:
    print("Choose a correct option :3")
