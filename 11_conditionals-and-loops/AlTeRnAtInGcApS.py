string_to_iterate = "alternatingcaps"
solution = "" #call it solution_string
for char in string_to_iterate:
    if char in string_to_iterate[0 : : 2]:
        solution += str.upper(char)
    elif char in string_to_iterate[1 : : 2]:
        solution += str.lower(char)
    elif char in string_to_iterate == " ":
        solution += char

print(solution)


# for i in range(len(string_to_iterate)):
#     char = string_to_iterate[i]
#     if i % 2 == 0:
#         char = char.upper() 
#         # print(i)
#         # print(solution)
#     else:
#         char = char.lower()

#     solution += char
# print(solution )