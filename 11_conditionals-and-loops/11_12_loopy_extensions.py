# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.


#i think this will involve iterating over each character
#and if the character is a 'p' 'd' or 'f'
# >>>then it will be added to the value of a variable 'pdf'
# >>>then the truth condition, set as 'pdf', is satisfied, 
#<>Truth accomplished<>

filename = "mrdeltoidisafunnyperson.pdf"
ext = ""
    
flag_ext = None
flag_p = None
flag_d = None
flag_f = None

    
for char in filename:
    if char == '.':
        flag_ext = True
    elif char == 'p':
        flag_p = True    
    elif char == 'd':
        flag_d = True
    elif char == 'f':
        flag_f = True
        
    if flag_p and flag_ext == True:
        flag_p = True
    else:
        flag_p = False
        
if flag_ext and flag_p and flag_d and flag_f == True:
    print('Filename is a pdf file.')
else:
    print('Filename is not a pdf file.')
        