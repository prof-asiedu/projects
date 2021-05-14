for n in range(1, 101):
    if(n %3 == 0 and n%5 ==0):
        print("Fixbuzz")
    elif(n %3 ==0):
        print("Fix")
    elif(n % 5 ==0):
        print("buzz")
    else:
        print(n)