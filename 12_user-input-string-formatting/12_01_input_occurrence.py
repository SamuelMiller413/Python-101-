  # Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4


result = ""
entry = input("please enter a string of words:\n\n  words: ")
print("thanks!")
letter = input("what letter are you looking for?\n\n  letter: ")
print("great, let's take a look!")
flag = True

while flag:

    for i in entry:
        if i == letter:
            result = entry.index(i)
            print(result)
            flag = False
            break
    else:
        print("uh oh. looks like the letter you're looking for doesn't reside in the string of words you've provided!")
        flag = False
        break

