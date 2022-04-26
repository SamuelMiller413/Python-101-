# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.



# use a while loop!
# alt = ""
# opinion = input("\n\nWhat's your honest opinion of baseball?\n    ")

# for i in opinion:
#     if i.isalpha():
#         alt += i + "^"
#     else:
#         alt += i + "$"            starting place>>>>now use bool
# print(f"{alt}")

alt = ""
flag = True
opinion = input("\n\nWhat's your honest opinion of baseball?\n    -> ")

for i in opinion:
    if i.isalpha():
        if flag == True:
            alt += str.lower(i)
            flag = False
        elif flag == False:
            alt += str.upper(i)
            flag = True
    else:
        alt += i
print(f"\n\n{alt}\n\n")

# make a thing that retiurns a bool flag every time it iterates a letter, switching hte binary off and on.
# anything that's not, it prints without change





