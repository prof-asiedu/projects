# Done by rich
print("Welcome to the tip calculator 2.0")

# Greet the user/ welcome message
# ask for the total bill
total_bill = int(input("What was the total bill: "))
# ask for the percentage tip
tip_percentage=int( input("What percentage tip would you like to give? 10, 12, 0r 15?: %"))
tip_percent = tip_percentage /100;
tip = tip_percent * total_bill
new_bill = total_bill + tip
# ask for the number of people to split tip 
tip_shared_btn = int(input("How many people to split the bill?: "))
# display each person bill to 2 dp
each_person = new_bill /tip_shared_btn
each_person_rounded = round(each_person, 2)
final_tip =f"Each person should pay GHS{each_person_rounded}"
print(final_tip)