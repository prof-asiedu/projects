# get year input
year =int(input("Enter the year: " ))
# check if input is a leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
           print("Leap year")
        else:
            print("not leap year.")
    else:
        print("Leap year.")

else:
    print("not leap")