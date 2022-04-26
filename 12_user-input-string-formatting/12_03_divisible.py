# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

entry = int(input("\nenter a number between 1 and 1,000,000,000\n"))

# if entry != range(1, 1000000000):
#     print(f"\nenter number within specified parameters\n")

if entry in range(1, 1000000000):
    if entry % 3 == 0:
        print("entry is divisible by 3") 
    if entry %3 != 0:    
        print("entry is not divisible by 3")