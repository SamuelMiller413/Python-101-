#we want any word entered to be translated
#word = "good"
input_letter = ""
char_aug = 1
list_of_words = ["food", "chicken", "dog", "truck"]

# for word in list_of_words:
#     new_word = ""
    
#     for char in word:
#         new_word += chr(ord(char) + char_aug)
        
#         # for list_of_words
#         # if ord(char):
            
#     print(new_word)

list_of_codes = ["gppe", "dijdlfo", "eph", "usvdl"]
return_aug = 1 


for ret in list_of_codes:
    return_word = ""

    for char_ret in ret:
        return_word += chr(ord(char_ret) - return_aug)

    print(return_word)