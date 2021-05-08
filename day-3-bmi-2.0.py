# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# get the height in meters
height = float(input ("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

# calculate the bmi
bmi = int(weight / (height * height))
print(bmi)
message = ''
#print messages
if bmi < 18.5:
    message =f" Your BMI is {bmi}, you are underweight"
elif bmi < 25:
    message =f" Your BMI is {bmi}, you have a normal weight"
elif bmi < 30:
    message = f"Your BMI is {bmi}, you are slightly overweight"
elif bmi < 35:
    message = f"Your BMI is {bmi}, you are overweight"
else:
    message =f" Your BMI is {bmi}, you are clininically obese"

print(message)