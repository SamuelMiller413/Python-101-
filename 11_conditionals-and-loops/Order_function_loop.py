
# word = "you "
# # first_letter = word[0]
# # end_word = word[1:-1]
# first_letter = ""   
# end_word = ""
# for char in word:
#     if char == word[0:1]:
#         first_letter += char       
#     elif char in word[1:-1:]: 
#         end_word += char

# # print('x')
# # print(first_letter)
# # print(end_word)
# # print(word[0:1])
# # print(end_word)
# print(word[0])
# print(word[1:-1])
# print("cmcm")
# print(first_letter)
# print(end_word)




import string
line_1 = ""
line_2 = ""
line_3 = ""
line_4 = ""
line_5 = ""
line_6 = ""
line_7 = ""
print('')
title = 'Guide to Order Values '
for i in title:
    print(i+"\u0332",end='')
print('')
print('')
print('     For lowercase letters:')
print('')
for char in string.ascii_lowercase:
    if ord(char) in range(97,104):
        line_1 += char + " = " + str(ord(char)) + " "
    elif ord(char) in range(104,108):
        line_2 += char + " = " + str(ord(char)) + " "
    elif ord(char) in range(108,113):
        line_3 += char + " = " + str(ord(char)) + " "
    elif ord(char) in range(113,116):
        line_4 += char + " = " + str(ord(char)) + " "
    elif ord(char) in range(116,119):
        line_5 += char + " = " + str(ord(char)) + " "
    elif ord(char) in range(119,121):
        line_6 += char + " = " + str(ord(char)) + " "
    elif ord(char) in range(121,123):
        line_7 += char + " = " + str(ord(char)) + " "
print(line_1)
print(line_2)
print(line_3)
print(line_4)
print(line_5)
print(line_6)
print(line_7)
#...
line_1 = ""
line_2 = ""
line_3 = ""
line_4 = ""
line_5 = ""
line_6 = ""
line_7 = ""
print('')
print('     For UpperCase letters:')
print('')
for char in string.ascii_uppercase:
    if ord(char) in range(65,72):
        line_1 += char + " = " + str(ord(char)) + " "
    elif ord(char) in range(72,76):
        line_2 += char + " = " + str(ord(char)) + " "
    elif ord(char) in range(76,81):
        line_3 += char + " = " + str(ord(char)) + " "
    elif ord(char) in range(81,84):
        line_4 += char + " = " + str(ord(char)) + " "
    elif ord(char) in range(84,87):
        line_5 += char + " = " + str(ord(char)) + " "
    elif ord(char) in range(87,89):
        line_6 += char + " = " + str(ord(char)) + " "
    elif ord(char) in range(89,91):
        line_7 += char + " = " + str(ord(char)) + " "
print(line_1)
print(line_2)
print(line_3)
print(line_4)
print(line_5)
print(line_6)
print(line_7)
print('')
