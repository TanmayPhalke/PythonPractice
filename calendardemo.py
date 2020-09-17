#trying basic calendar functions :)

import calendar

def dispMonth(mm,yy):
    print(calendar.month(yy,mm))

def dispYear(yy):
    print(calendar.calendar(yy,2,1,6,3))

print("1. Display Month of the year \n2. Display year calender\n ")
option = int(input("Please enter your choice: "))

if option == 1:
    mm = int(input("Enter the month: "))
    yy = int(input("Enter the year: "))
    if mm >= 1 and mm<=12:
        if len(str(yy)) == 4:
            dispMonth(mm,int(yy))
        else:
            print("Enter correct year :) ")
    else:
        print("Enter correct month :) ")
elif option == 2:
    yy = int(input("Enter the year: "))
    if len(str(yy)) == 4:
        dispYear(yy)
    else:
        print("Enter correct year :) ")
