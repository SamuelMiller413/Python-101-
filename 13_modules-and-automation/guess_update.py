import random

num = random.randint(1,20)
guess = None
x = 0
while guess != num and x < 5:
    while x < 1:     
        guess = input("\n\nAlright, you scoundrel. You've got 4 tries\nto guess the magic number. It's between 1 and 20. What is it??\nEnter number:  ")
        guess = int(guess)
        x += 1
        
        if guess == num:
            print("\nGreat job! I knew you could do it!")
            x = 5
            break
        elif guess > num:
            print("\nToo high!")
            break
        elif guess < num:
            print("\ntoo low!")
            break
        
    
    while x <= 5:
        guess = input("Guess again.\nEnter number:  ")
        guess = int(guess)
        if guess == num:
            print("\nGreat job! I knew you could do it!")
            x = 5 
            break
        if x == 4:
            if guess > num:
                print("Alright. That was too high but i'll give you\none more try because I like you.")
            elif guess < num:
                print("Alright. That was too low but i'll give you\none more try because I like you.")   
        elif guess > num:
            print("\nToo high!")
        elif guess < num:
            print("\ntoo low!")
        x += 1 
    
    while x > 5 and guess != num:
        print("Better luck next time!")
        break
    x += 1
    
    