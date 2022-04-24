# TODO: Write a prompt that asks users to "type something to win"
#       They will only win if they type "something" into the prompt
#
# Collect user input
# Compare to the string "something"
# Print a win or lose message

#num = random.randint(1, 10)
#guess = None

#while guess != num:
#	guess = input("guess a number between 1 and 10: ")
#	guess = int(guess)

#	if guess == num:
#		print("congratulations! you won!")
#		break
#	else:
#		print("nope, sorry. try again!")


# The following lines are the fixed code: 

'''
answer = 'something'
guess = None
guess_again = None

while guess != answer:
    guess = input("Type something to win: ")
    guess = str(guess)
    guess_again = input("Again, please just type something... ")
    guess_again = str(guess_again)
    
    if guess == answer:
      print('Aren\'t you the clever one!')
      break
    if guess_again == answer:
      print('Aren\'t you the clever one!')
      break
    else:
        print(guess_again)
'''

