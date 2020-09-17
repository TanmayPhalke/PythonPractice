#temperature conversion program

def celtofar(temp):
    tempf = round((temp*(9/5))+32)
    print(temp," in degree Farenheit is: ",tempf,"F")
def fartocel(temp):
    tempc = round((temp-32)*5/9)
    print(temp," in degree Celcius is: ",tempc,"C")

opt =int(input("Choose the conversion type. \n 1. Celcius to Farenheit \n 2. Farenheit to Celcius \n"))
if opt == 1:
    temp = int(input("Enter temperature in celcius: "))
    celtofar(temp)
elif opt == 2:
    temp = int(input("Enter temperature in farenheit: "))
    fartocel(temp)
