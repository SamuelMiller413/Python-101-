# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

flag = True

while flag is True:

    entry = input("Enter the number you want to know the month of:\n    ")
    if entry == 'quit':
        flag = False
    else:
        num = int(entry)

        if num in range(1,12):
            if num == 1:
                print("\nJanuary\n")
            if num == 2:
                print("\nFebruary")
            if num == 3:
                print("\nMarch\n")
            if num == 4:
                print("\nApril\n") 
            if num == 5:
                print("\nMay\n")
            if num == 6:
                print("\nJune\n")
            if num == 7:
                print("\nJuly\n")
            if num == 8:
                print("\nAugust\n")
            if num == 9:
                print("\nSeptember\n")
            if num == 10:
                print("\nOctober\n")
            if num == 11:
                print("\nNovember\n")
            if num == 12:
                print("\nDecember\n")
        
        if num not in range(1,12):
            print('Error')