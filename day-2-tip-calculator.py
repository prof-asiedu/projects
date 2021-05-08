# Done by rich
print("Welcome to the tip calculator 2.0")

# Greet the user/ welcome message
# ask for the total bill
bill = float(input("What was the total bill: "))
# ask for the percentage tip
tip =int( input("What percentage tip would you like to give? 10, 12, 0r 15?: %"))
tip_percent = tip /100
total_tip_amt = tip_percent * bill
total_bill = bill + total_tip_amt
# ask for the number of people to split tip 
people = int(input("How many people to split the bill?: "))
# display each person bill to 2 dp
bill_per_person = total_tip_amt /people
final_amount = "{:.2f}".format(bill_per_person)
# each_person_rounded = round(each_person, 2)
final_tip =f"Each person should pay GHS{final_amount}"
print(final_tip)