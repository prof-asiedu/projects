#ask for the age
age = input("What is your current age: \n")

#cast age to int
age_as_int =int(age)
terminal = 60
#compute the age in years
age_left = terminal - age_as_int 
# print(age_left)

days_left = age_left * 365
weeks_left = age_left * 52
months_left = age_left * 12

message = f"Your have {months_left} months, {weeks_left} weeks, and {days_left} days left. Plan well."
print("\n")
print(message)