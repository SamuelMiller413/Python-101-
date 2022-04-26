# user_input = int(input("Enter a number you'd like to have squared: "))
# # number = int(user_input)

# print(user_input ** 2)

# name = None

# while name != "your name":
#     name = input("Please type your name: ")

# print("Finally!")

# word = "cradle"

# count = 5
# while count > 0:
#   print("mr. deltoid")
#   count -= 1
# >>>>>>>>>>>>>>>>>>>>>>>>> Using 'quit' keyword
# for char in word:
#     if char in "aeiou":
#         break
#     print(char)

# print("done")

# prompt = None
# while True and prompt != 'quit':
#     prompt = input('say something: ')
#     if prompt == 'quit':
#             prompt = 'quit'
#     print(prompt[::-1])
# print("bye!! (it's tiuq, btw. ;)")
        
# while True:
#     # Start the program
#     prompt = input("what would you like to do? ")
    
#     if prompt == "quit":
#         # Leave the program
#         break
#     elif prompt == "dance for me!":
#         # do other stuff
#         do_something()
#     print(prompt[::-1])

# print("!!!EYB")        

# >>>>>>>>>>>>>>>>>>>>>>>>> Using 'continue' keyword
# word = "hello"

# for char in word:
#     if char in "aeiou":
#         continue
#     print(char)

# print("done")

# count = 5
# while count > 0:
#     print(str(count) + " :)")
#     count -= 1

# >>>>>>>>>>>>>>>>>>>>>>>>> Using "f strings" {}
#    
# name = "Tom"
# age = 99

# print(f"Hello {name}. Next year you'll be {age + 1}!")

# print("Welcome to the unfulfilling market!")
# print("Tell us what you want, and we won't have it.")

# food = input("What do you want? ")
# amount = int(input(f"How much of {food}? "))

# print(f"You want {amount} {food}? Sorry, we only have {amount - 1}.")

# >>>>>>>>>>>>>>>>>>>>>>>>> Using str.format() instead of f-string

# print("{1} is not {0}, but it's {1}!".format("Basil", "Sage"))


# print("Welcome to the unfulfilling market!")
# print("Tell us what you want, and we won't have it.")

# food = input("What do you want? ")
# amount = int(input("How much of {}? ".format(food)))

# print("You want {0} {1}? Sorry, we only have {2}.".format(amount, food, amount -1))

# name = "harold"

# my_string = f"hei there {name.upper()}, f-strings are hot {1 + 2 + 3}!"

# print(my_string)

# >>>>>>>>>>>>>>>>>>>>>>>>> Using minilanguage with f-strings
# >>>>>>>>>>>>>>>>>>>>>>>>>^^^^^^^ Use  in game when >1 option e.g. doors

# message = "you move me!"
# note = "Use this 'mini language' in game when >1 option e.g. doors"
# print(f"{message:>40}")
# print(f"{note:>60}")
# print(f"{message:<60}")
# print(f"{note:<60}")
# print(f"{message:^150}")
# print(f"{note:^150}")


# NOTES ON CENTERING
# # print("111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
# window_width = "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
# print(len(window_width))
# center = "Center"
# print(f"{center:>128}")


# >>>>>>>>>>>>>>>>>>>>>>>>> Using 'character escaping' / quotes in quotes / using backslash "\\"
# >>>>>>>>>>>>>>>>>>>>>>>>> ^^^^^^^^^^^  LINE BREAK!!!!!!! = "\n"

# message = "The door reads \"Do Not Enter!\""
# print(message)         #  ^              ^

# print("""hi there,\
# friend""")

# long_str = "check out this very long string that is full of wisdom \
#             so you should definitely keep reading all the way to the end!"

# print(long_str)

# long_str = ("hei there "
#             "how are you?"
#             " remember that this ends up as one string!")

# print(long_str)


# import tkinter as tk

# root = tk.Tk()
# deli = 100           # milliseconds of delay per character
# svar = tk.StringVar()
# labl = tk.Label(root, textvariable=svar, height=10 )

# def shif():
#     shif.msg = shif.msg[1:] + shif.msg[0]
#     svar.set(shif.msg)
#     root.after(deli, shif)

# shif.msg = ' Is this an alert, or what? '
# shif()
# labl.pack()
# root.mainloop()


# text = input('Text to be displayed: ')



# speech = "hello there Samuel. I'm your computer" 
# for i in speech:    #italic
#     print(f"\x1B[3m{i}\x1B[0m", end='', flush=True)
#     time.sleep(0.1)
# print('\n')

# f"\x1B[3m{i}\x1B[0m"
# print("\x1B[3mhello\x1B[0m")
# narration = (f"\x1B[3m{'he looks at you with his one good eye'}\x1B[0m")



# move = ["/","|","\\","-"]
# import time
# import random


# game = True
# sword = False
# dm = "Funk Shun"

# # time_half = time.sleep(.5)
# # time1 = time.sleep(1)
# # time2 = time.sleep(2)
# #time3 = time.sleep(3)
# # time4 = time.sleep(4)

# pause = '…'

# funk_shun_speech = f"We don’t get very many wanderers here in Smirkwood.\n\
# {pause} For the best if you ask me. \n\
# At any rate, I'm called Funk Shun."
# for i in funk_shun_speech:   
#     print(i, end='', flush=True)
#     time.sleep(0.05)
#     if i == pause:
#         time.sleep(.75)
# print('\n')
# time.sleep(1)




# RhymeName

# name = input("What's your name then?\n")
# rhyme = "Schl"
# rhyme_name = "Schl" + name[1::]
# # print(f"rhymes with {rhyme_name}")
# newname = ""
# x = ""


# for let in name:
#     if let in ['a', 'e', 'i', 'o', 'u']:
#         x = let
#     if let in range(int(len(name[x::]))):
#         newname += x + let
# print(newname)
# name = input("What's your name then?\n")
# vowels = ['a', 'e', 'i', 'o', 'u']
# consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
# captured_consonants = ""
# captured_substring = ""
# new_user_input = ""

# for i in name:
#     if i in consonants:
#         break
#     elif i in vowels:
#         captured_substring = captured_substring + i 
#         if i in name:
# print (captured_substring)

# def funny_name(name):
#     prefix = "Schl"
#     rhyme_name = ""
    
#     found_vowel = False
#     for i in name:
#         if i in 'aeiouyAEIOUY':
#             found_vowel = True
#         if found_vowel == True:
#             rhyme_name += str.lower(i)
#     return prefix + rhyme_name

# name = input("type name: ")
# rhyme_name = funny_name(name)

# =========================================================
import time
import random
import sys
import string

prompting = True
sword = False
dm = "Funk Shun"
rate = 0.05
pause_rate = time.sleep(.75)
pause = '…'
pause_less = "æ"
end_sentence = time.sleep(.2)
comma = time.sleep(.1)
name = "Samuel"
rhyme_name = "Schlamuel"

def funny_name(name):
    prefix = "Schl"
    rhyme_name = ""
    
    found_vowel = False
    for i in name:
        if i in 'aeiouyAEIOUY':
            found_vowel = True
        if found_vowel == True:
            rhyme_name += str.lower(i)
    return prefix + rhyme_name
                                
def sleep(time_value):
    if time_value == 'half':
        time.sleep(.5)
    if time_value == 1:
        time.sleep(1)
    if time_value == 2:
        time.sleep(2)
    if time_value == 3:
        time.sleep(3)
    if time_value == 4:
        time.sleep(4)                         

def funk_shun_speech(funk_shun, rate_ratio = 1, pause_time_ratio = 1):
    rate = 0 * rate_ratio
    pause_time = 0 * pause_time_ratio
    for i in funk_shun:
        if i in '.?!':                
            print(i, end='', flush=True)
            time.sleep(.2)
        elif i == ',':
            print(i, end='', flush=True)
            time.sleep(.15)
        elif i == pause:
            time.sleep(pause_time)
        elif i == pause_less:
            time.sleep(.3)    
        else:
            print(i, end='', flush=True)
            time.sleep(rate)
    time.sleep(pause_time)
    print('\n')

def narration_speech(narration, rate_ratio = 1, pause_time_ratio = 1):
    rate = 0 * rate_ratio
    pause_time = 0 * pause_time_ratio
    
    for i in narration:
        if i in '.?!':                
            print(f"\x1B[3m{i}\x1B[0m", end='', flush=True)
            time.sleep(.2)
        elif i == ',':
            print(f"\x1B[3m{i}\x1B[0m", end='', flush=True)
            time.sleep(.15)
        elif i == pause:
            time.sleep(pause_time)
        elif i == pause_less:
            time.sleep(.3)
        else:
            print(f"\x1B[3m{i}\x1B[0m", end='', flush=True)
            time.sleep(rate)
    time.sleep(pause_time)
    print('\n')

def narration_speech_aug(narration, rate_ratio = 1, pause_time_ratio = 1):
    rate = 0.03 * rate_ratio
    pause_time = .75 * pause_time_ratio
    
    for i in narration:
        if i in '.?!':                 
            print(f"\x1B[3m{i}\x1B[0m", end='', flush=True)
            time.sleep(.2)
        elif i == ',':
            print(f"\x1B[3m{i}\x1B[0m", end='', flush=True)
            time.sleep(.15)
        elif i == pause:
            time.sleep(pause_time)
        elif i == pause_less:
            time.sleep(.3)
        
        else:
            print(f"\x1B[3m{i}\x1B[0m", end='', flush=True)
            time.sleep(rate)
    time.sleep(pause_time)
    print('\n')
# ===========================
line_1 = ""
line_2 = ""
line_3 = ""
line_4 = ""
line_5 = ""
line_6 = ""
line_7 = ""






# def line(x):
#     width = 8
#   for num in x:
#         for base in 'd':
#             print('{0:{width}}'.format(num, base=base, width=width), end=' ')
#     print()
# width = 8
# def enil(x):
#     for num in x:
#         for base in 'd':
#             print(f"{num:{width}}", end=" ")
#     print()
# enil(string.ascii_lowercase)







# char_ord = str(ord(char))
import string

width = 9
x = ""

# char_ord = str(ord(char))


# def guide(x):
#     i = 0
#     j = 0
#     # line_len = 3 * ((width *3)//2)
#     line = ""
#     for char in x:
#         element = ""
#         line_format = ""
#         element_format = ""
#         char_ord = str(ord(char))
#         element += f"{char} = {char_ord}"
#         element_format += f"{element:{width}}"
#         line += element_format
#         # print(element_format, end=" ")
#         i += 1
#         j += 1
#         if i > 3:
#             # print()
#             i = 0
#             print(f"{line:^50}")
#             line = ""  
#         if j > 25:
#             # print()
#             print(f"{line:^50}")

# print('\n\n')

# guide(string.ascii_lowercase)    

# print('\n\n')


#   print(f"{gut:^50}")     
#     print()

# def guide(x):
#     i = 0
#     line_len = 3 * ((width *3)//2)
#     for char in x:
#         line = ""
#         element = ""
#         line_format = ""
#         element_format = ""
#         char_ord = str(ord(char))
#         element += f"{char} = {char_ord}"
#         element_format += f"{element:{width}}"
#         line += element_format
#         print(element_format, end=" ")
#         i += 1
#         if i > 3:
#             print()
#             i = 0
#         # print(f"{line_format}:^")
#     print()

# print('\n\n')

# guide(string.ascii_lowercase)    

# print('\n\n')


# for char in string.ascii_lowercase:
#     if ord(char) in range(97,104):
#         line_1 += char + " = " + str(ord(char)) + " "
#     elif ord(char) in range(104,108):
#         line_2 += char + " = " + str(ord(char)) + " "
#     elif ord(char) in range(108,113):
#         line_3 += char + " = " + str(ord(char)) + " "
#     elif ord(char) in range(113,116):
#         line_4 += char + " = " + str(ord(char)) + " "
#     elif ord(char) in range(116,119):
#         line_5 += char + " = " + str(ord(char)) + " "
#     elif ord(char) in range(119,121):
#         line_6 += char + " = " + str(ord(char)) + " "
#     elif ord(char) in range(121,123):
#         line_7 += char + " = " + str(ord(char)) + " "
# print(line_1)
# print(line_2)
# print(line_3)
# print(line_4)
# print(line_5)
# print(line_6)
# print(line_7)
# #...


# line_1 = ""
# line_2 = ""
# line_3 = ""
# line_4 = ""
# line_5 = ""
# line_6 = ""
# line_7 = ""
# print('')
# print('     For UpperCase letters:')
# print('')
# for char in string.ascii_uppercase:
#     if ord(char) in range(65,72):
#         line_1 += char + " = " + str(ord(char)) + " "
#     elif ord(char) in range(72,76):
#         line_2 += char + " = " + str(ord(char)) + " "
#     elif ord(char) in range(76,81):
#         line_3 += char + " = " + str(ord(char)) + " "
#     elif ord(char) in range(81,84):
#         line_4 += char + " = " + str(ord(char)) + " "
#     elif ord(char) in range(84,87):
#         line_5 += char + " = " + str(ord(char)) + " "
#     elif ord(char) in range(87,89):
#         line_6 += char + " = " + str(ord(char)) + " "
#     elif ord(char) in range(89,91):
#         line_7 += char + " = " + str(ord(char)) + " "




# print("omg you did it!")
# narration_test = f"What you're reading right now is a test. You may, dear reader, wonder what it tests. it is a test to see whether the modicaction works! the modification? the one with the character '.?!'. did that work?"
# narration_speech_aug(narration_test)
                                
gut = f"gut"
print(f"{gut:>40}")


# def line(x):
#     width = 8
#   for num in x:
#         for base in 'd':
#             print('{0:{width}}'.format(num, base=base, width=width), end=' ')
#     print()

import string
# line_1 = ""
# line_2 = ""
# line_3 = ""
# line_4 = ""
# line_5 = ""
# line_6 = ""
# line_7 = ""
# print('')
# title = 'Guide to Order Values '
# for i in title:
#     print(i+"\u0332",end='')
# print('')
# print('')
# print('     For lowercase letters:')
# print('')
# for char in string.ascii_lowercase:
#     if ord(char) in range(97,104):
#         line_1 += char + " = " + str(ord(char)) + " "
#     elif ord(char) in range(104,108):
#         line_2 += char + " = " + str(ord(char)) + " "
#     elif ord(char) in range(108,113):
#         line_3 += char + " = " + str(ord(char)) + " "
#     elif ord(char) in range(113,116):
#         line_4 += char + " = " + str(ord(char)) + " "
#     elif ord(char) in range(116,119):
#         line_5 += char + " = " + str(ord(char)) + " "
#     elif ord(char) in range(119,121):
#         line_6 += char + " = " + str(ord(char)) + " "
#     elif ord(char) in range(121,123):
#         line_7 += char + " = " + str(ord(char)) + " "
# print(line_1)
# print(line_2)
# print(line_3)
# print(line_4)
# print(line_5)
# print(line_6)
# print(line_7)
# #...
# line_1 = ""
# line_2 = ""
# line_3 = ""
# line_4 = ""
# line_5 = ""
# line_6 = ""
# line_7 = ""
# print('')
# print('     For UpperCase letters:')
# print('')


# total_list = string.ascii_lowercase, string.ascii_uppercase
# line_upper = ""
# line_lower = ""
# for char in total_list: 
#     if char in string.ascii_uppercase:
#         line_lower += char + " = " + str(ord(char)) + " "
#         print(range(line_upper[1, 2, 3, 4]))
#         print(list(line_upper[5, 6, 7, 8]))
#         print(list(line_upper[9, 10, 11, 12]))
#         print(list(line_upper[13, 14, 15, 16]))
#         print(list(line_upper[17, 18, 19, 20]))
#         print(list(line_upper[21, 22, 23, 24]))
#         print(list(line_upper[25, 26]))
#     if char in string.ascii_uppercase:
#         line_upper += char + " = " + str(ord(char)) + " "
#         print(list(line_upper[1, 2, 3, 4]))
#         print(list(line_upper[5, 6, 7, 8]))
#         print(list(line_upper[9, 10, 11, 12]))
#         print(list(line_upper[13, 14, 15, 16]))
#         print(list(line_upper[17, 18, 19, 20]))
#         print(list(line_upper[21, 22, 23, 24]))
#         print(list(line_upper[25, 26]))
   

print(list(string.ascii_lowercase))

import string
import time

letter_list = list(string.ascii_letters) # creates list of all lettter in alphabet, lower and upper case
prompting = True

def encrypt(x):
    og_char = ''
    aug_char = ''
    aug_line = ''
    
    for char in x:
        
        if char in letter_list:
            og_char = str(letter_list.index(char))
            aug_char = str(int(og_char) - 3)
            aug_line += (str(letter_list[(int(aug_char))]))
            # accessing letter list, 
        
        else:
            aug_line += char
    
    return aug_line 
  

def de_crypt(y):
    og_char = ''
    aug_char = ''
    aug_line = ''
    
    for char in y:
        
        if char in letter_list:
            og_char = str(letter_list.index(char))
            aug_char = str(int(og_char) + 3)
            aug_line += (str(letter_list[(int(aug_char))]))
         
        else:
            aug_line += char
    
    return aug_line  
    

print("\n\nWelcome, cypherpunk! I am the crpyt keeper, keeper of the crypt.")
while prompting:
    
    to_c_or_not_to_c = input("\n\nWould you like to\n\n   '1' Encrypt      -or-    '2' Decrpyt              (or '@quit' to quit)\n\n\x1B[3mEnter '1' or '2'\x1B[0m: ")    

    while (to_c_or_not_to_c != '1') and  (to_c_or_not_to_c != '2') and (to_c_or_not_to_c != '@quit'):
        time.sleep(.4)
        print("'1' or '2', please...        or you can always '@quit'")
        break
    if to_c_or_not_to_c == '1':
        time.sleep(.4)
        plain = input("Alright then. What would you like to encrpyt? \x1B[3mdon't worry, your secret is safe with me....\x1B[0m\n\n   Enter text: ")
        time.sleep(.4)
        print(f"Oh wow. I can see why you'd like to keep that a secret.\n   Here it is:\n")     
        encrypted_text = encrypt(plain)
    
        print(encrypted_text)
    elif to_c_or_not_to_c == '2':
        time.sleep(.4)
        code = input("\n\nAlright then. What would you like to decrpyt? \x1B[3mdoh the anticipation....\x1B[0m\n\n   Enter text: ")
        time.sleep(.4)
        print(f"\n\nOh dANG... Some things should stay a secret.\nBut then again, I'm literally made of codes...\n   But enough about me, here it is:\n")
        print(de_crypt(code))
    elif to_c_or_not_to_c == '@quit':
        time.sleep(1)
        print("Well, alright. Hope I was helpful. Zljb yxzh pllk!\n") 