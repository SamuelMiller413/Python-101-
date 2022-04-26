import string

title= "Guide to Order Values"
header_low = "lowercase:"
header_up = "UpperCase:"

def title_aug(x):
    title_format = ""
    for char in x:
        title_format += char+'\u0332'
    print(f"\n{title_format:^68}\n")

def header_aug(x):
    header_format = ""
    for char in x:
        header_format += char  #f"\x1B[3m{}\x1B[0m"
    print (f"\x1B[3m{header_format:^46}\x1B[0m\n")
        
def table(x):
    i = 0
    j = 0
    line = ""
    width = 9
    for char in x:
        element = ""
        element_format = ""
        char_ord = str(ord(char))
        element += f"{char} = {char_ord}"
        element_format += f"{element:{width}}"
        line += element_format
        i += 1
        j += 1
        if i > 3:
            # print()
            i = 0
            print(f"{line:^48}")
            line = ""  
        if j > 25:
            # print()
            print(f"{line:^48}")
            print()

title_aug(title) 
header_aug(header_low)
table(string.ascii_lowercase)    
header_aug(header_up)
table(string.ascii_uppercase) 

# ==============  Alternate - no if  ============== 
# import string

# total_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" 
# line_lower = ""
# line_upper = ""
# element = ""
# title_post = ""
# title_pre = 'Guide to Order Values:'

# for i in title_pre:
#     title_post += i+"\u0332"
    
# for char in total_list: 
#     if char in string.ascii_uppercase:
#         element += char + " = " + str(ord(char)) + " "
#         line_upper += f"{element:8}"
#         element = ""
#     elif char in string.ascii_lowercase:
#         element += char + " = " + str(ord(char)) + " "
#         line_lower += f"{element:8}"
#         element = ""

# print()
# print(f"         {title_post}")

# print()
# print()
# print(f"{'For lowercase Letters:':^40}")
# print()
# print(f"{line_lower[:32]:^40}")
# print(f"{line_lower[32:64]:^40}")
# print(f"{line_lower[64:96]:^40}")
# print(f"{line_lower[96:128]:^40}")
# print(f"{line_lower[128:160]:^40}")
# print(f"{line_lower[160:192]:^40}")
# print(f"{line_lower[192:]:^40}")
# print()
# print(f"{'For UpperCase Letters:':^40}")
# print()
# print(f"{line_upper[:32]:^40}")
# print(f"{line_upper[32:64]:^40}")
# print(f"{line_upper[64:96]:^40}")
# print(f"{line_upper[96:128]:^40}")
# print(f"{line_upper[128:160]:^40}")
# print(f"{line_upper[160:192]:^40}")
# print(f"{line_upper[192:]:^40}")
# print()


# =================  just in case  ================= 
  
# line_format = ""
# print(element_format, end=" ")
# line_len = 3 * ((width *3)//2)
# char_ord = str(ord(char))

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
