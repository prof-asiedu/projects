# get year input
year =int(input("Enter the year: " ))
# check if input is a leap year
if year % 4 == 0:
    if year % 100 != 0:
        print(" leap")
    else:
        if year % 400 == 0:
            print("leap year")
         
        else:
            print("not leap year")

else:
    print("not leap")