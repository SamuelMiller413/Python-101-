# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings


string_1 = input("enter string 1:\n    ")
string_1_count = int(len(string_1))

string_2 = input("enter string 2:\n    ")
string_2_count = int(len(string_2))

string_3 = input("enter string 3:\n    ")
string_3_count = int(len(string_3))


max = 0
if string_1_count >= 0:
    max = string_1_count
    winner = f"\n{string_1}/{string_1_count}"
    
if  string_2_count >= max:
    winner += f"\n{string_2}/{string_2_count}"
    
    if  string_2_count > max:
        max = string_2_count
        winner = f"\n{string_2}/{string_2_count}"

if string_3_count == max:
    winner += f"\n{string_3}/{string_3_count}"

    if string_3_count > max:
        max = string_3_count
        winner = f"\n{string_3}/{string_3_count}"

print(f"\n\n{winner}\n\n")

