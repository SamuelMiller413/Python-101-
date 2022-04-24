# You start this journey with a number `n`.
# You have to display a string representation of all numbers from 1 to n,
# but there are some constraints:
# - If the number is divisible by 3, write `Fizz` instead of the number
# - If the number is divisible by 5, write `Buzz` instead of the number
# - If the number is divisible by both 3 and 5, write `FizzBuzz` instead of the number

for num in range(1, 106):
    if (num % 3 == 0) and (num% 5 == 0) == True:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

#               ¡or!

for num in range(1, 106):        
    by_3 = num % 3 == 0
    by_5 = num % 5 == 0
    
    if by_3 and by_5 == True:
        print('FizzBuzz')
    elif by_3 == True:
        print('Fizz')
    elif by_5 == True:
        print('Buzz')
    else:
        print(num)




