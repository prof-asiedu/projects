lover_one = input("First lover: ")
lover_two = input("Second Lover: ")
combine_names = lover_one.lower() + lover_two.lower()

# check for the number of times true loves comes
t = combine_names.count("t")
r = combine_names.count("r")
u = combine_names.count("u")
e = combine_names.count("e")

# check for the number of times true loves comes
l = combine_names.count("l")
o = combine_names.count("o")
v = combine_names.count("v")
e = combine_names.count("e")

true_score = t + r + u + e

love_score = l + o + v + e


true_love_score = int(str(true_score)+ str(love_score))
# print(f"Your love score is {true_love_score}% ")

# print the names
# print(combine_names)
# print(type(true_love_score))
message =''
if true_love_score <10 and true_love_score > 90:
    message =f"Your love score is {true_love_score}%, you will be great together"
elif true_love_score >9 and true_love_score < 60:
    message =f"Your score is {true_love_score}%, you need to work more to win more"
else:
    message =f"Your score is {true_love_score}%, you guys are compatible. Cheers"


print(message)