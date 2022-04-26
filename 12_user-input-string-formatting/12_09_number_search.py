# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.


flag = True

num = int(input("\nenter a number between 0 and 1,000,000,000\n    "))


while flag == True:
    for i in range(1000000000):
        if i == num:
            print(f"\n{num}\n\n")
            flag = False
            break
        else:
            print("erriorrrrr")    
            flag = False
            break