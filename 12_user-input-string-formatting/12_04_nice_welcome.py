# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

first_name_only = ""

name = input("enter name:\n ")


for i in name:
    if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        first_name_only += i
        flag = True
    if i == " ":
        flag = False
        break

if flag == True:
    print(f"\nwelcome to my script, {first_name_only}!")
if flag == False:
    print(f"Nobody wants to know your last name, {first_name_only}!")
    