
# name = input("Hello! Welcome to the world of DnD. What is your name? ")
# print(f"Welcome {name}! Thanks for playing. If at any point you want to stop playing, simply type 'quit'.")
# game = True
# sword = False

# while game == True:
#     doors = input("You encounter two doors. A door on your left and a door on your right. Which door would you like to go through? ")
#     if doors == "quit":
#         print("Game Over. Thanks for playing!")
#         game = False
#     elif doors != "left" and doors != "right":
#         print("That's not an option. Please only enter left or right.")
#     elif doors == "left":
#         while True:
#             direction = input("You enter the door on your left, which.... is empty. Would you like to look around? If not, you will return to the beginning. ")
#             if direction == "no":
#                 break
#             if direction == "yes":
#                 sword = input("Woot! You found a sword! Do you want to take the sword? ")
#                 if sword == "yes":
#                     sword = True
#                     print("You take the mighty sword and leave the room. Why not try the door on your right now? ;)")
#                     if direction == "yes" and sword == True:
#                         break
#     elif doors == "right":
#         while True:
#             direction_two = input("Ah! You encounter a mighty dragon named Grogu! Do you attack Grogu? ")
#             if direction_two == "yes" and sword == True:
#                 print("You have slain the mighty Grogu! Congratulations hero. You win!")
#                 break
#             elif direction_two == "yes" and sword == False:
#                 print(f"Grogu eats {name} whole. You lose. 'Hint: You May Want to Search Around in that Seemingly Empty Room Next Time. ;)'")
#                 break
#             elif direction_two == "no" and sword == True:
#                 print(f"You walk away from the castle with your new sword and head home. Thanks for playing {name}!")
#                 break
#             elif direction_two == "no" and sword == False:
#                 print(f"You walk away from the castle with nothing. Thanks for playing {name}!")
#                 break



#Game initial setup
import time
game = True
sword = False

#Game intro
name = input('\nEnter your name:\n')
time.sleep(2)
print(f'\nWelcome to the Game {name}\n')
time.sleep(2)
print('You will face a series of choices in this game. Choose wisely and you will become a WARRIOR. Thats the only way to leave this place.... alive')
time.sleep(1)
print('Good luck!!!')

#Game development
while game:
    time.sleep(2)
    doors = input('\nYou are in Room # 1 and have two doors in front of you (left or right)\nType which door you want to go through:\n')
    # INPUT VERIFIER doors
    while (doors != 'left') and (doors != 'right'):
        print('\nWhoops, that\'s not an option. Type only left or right')
        doors = input()
    
    if doors == 'left':
        
        while True:
            time.sleep(2)
            print('\nYou are in Room # 2, seemingly empty. You wanna look around?\nType yes or no (then you will return to Room # 1)')
            choice1 = input()
            # INPUT VERIFIER choice1
            while (choice1 != 'yes') and (choice1 != 'no'):
                print('\nWhoops, that\'s not an option. Type only yes or no')
                choice1 = input()

            if choice1 == 'no':
                break
            elif (choice1 == 'yes') and (sword == False):
                for i in range(0,5):
                        time.sleep(1)
                        print('.')
                print('\nWow!!! You found a sword. It looks so nice. Wanna grab it?\nType yes or no')
                choice2 = input()
                # INPUT VERIFIER choice2
                while (choice2 != 'yes') and (choice2 != 'no'):
                    print('\nWhoops, that\'s not an option. Type only yes or no')
                    choice2 = input()

                if choice2 == 'no':
                    print('\nThat\'s so sad :( Maybe you\'ll need it later on...')
                    continue    
                elif choice2 =='yes':
                    print(f'\nGreat! Now you have a sword. You are a WARRIOR {name}')
                    sword = True
                    continue
            elif (choice1 == 'yes') and (sword == True):
                for i in range(0,5):
                        time.sleep(1)
                        print('.')
                print('\nWell, there\'s nothing here anymore. Maybe you can try the right door in Room #1')
                continue

    elif doors == 'right':
        
        while True:
            time.sleep(3)
            print('\nYou encounter with a DRAGON. Wanna fight it? (TIP: Only do it if you are a WARRIOR)\nType yes or no')
            fight_dragon = input()
            # INPUT VERIFIER fight_dragon
            while (fight_dragon != 'yes') and (fight_dragon != 'no'):
                print('\nWhoops, that\'s not an option. Type only yes or no')
                fight_dragon = input()

            if fight_dragon == 'no':
                time.sleep(2)
                print('\nAlright, heading back')
                break
            elif fight_dragon == 'yes':
                time.sleep(2)
                print(f'\nThis is it {name}. Attack the Dragon!!!!\n')
                if sword == True:
                    time.sleep(2)
                    print('You are a WARRIOR and have your sword with you. Let\'s go!!!!')
                    for i in range(0,5):
                        time.sleep(1)
                        print('.')
                    print(f'You defeated the Dragon. You won {name}!!!\n')
                    game = False
                    break
                elif sword == False:
                    time.sleep(2)
                    print('You have no weapons with you, this is gonna be tough')
                    for i in range(0,5):
                        time.sleep(1)
                        print('.')
                    print(f'Sorry {name}, you were not a WARRIOR and the dragon ate you. You lose :(\n(TIP: Maybe you need to pick up a weapon next time)\n')
                    game = False
                    break
