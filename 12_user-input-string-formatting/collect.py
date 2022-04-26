# >>>> Sassy Return <<<<

user_input = input("What do you care about? ")
return_phrase = "you: 'I care about: "
for char in user_input:
    if char in user_input[::2]:
        return_phrase += str.upper(char)
    elif char in user_input[1::2]:
        return_phrase += str.lower(char)
print((return_phrase) + "'")

