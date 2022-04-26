# Use the built-in `sys` module to explicitly quit your script.
# Include this functionality into a loop where you're asking the user
# for input in an infinite `while` loop.
# If the user enters the word "quit", you can exit the program
# using a functionality provided by this module.

import sys
player_input = ''

while True:
    player_input = str(input("What is the reason you're alive?  "))
    if player_input == "Because.":
        sys.exit()
    # input("Oh yeah? Why?  ")
    # if input == "Because.":
    #     quit()
    
    # while True:
    #     input("Why? ")
    #     if input == "Because.":
    #         quit()
