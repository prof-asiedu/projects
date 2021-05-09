#ask for pizza size
pizza_size = input("type  S, L, M for size: ")
add_pepperoni = input("Add pepperoni 'Y'es or 'N'o: ")
extra_cheese = input("Extra cheese 'Y'es or 'N'o: ")

bill = 0

if pizza_size == 'S':
    if add_pepperoni == 'Y':
        bill = 15 + 2
    else:
        bill = 15
elif pizza_size == 'M':
    if add_pepperoni == 'Y':
        bill = 20 + 3
    bill = 20
else:
    if add_pepperoni == "Y":
        bill = 25 + 3
    else:
        bill = 25

if extra_cheese == "Y":
    bill +=1

print(f"Your final bill is ${bill}")

