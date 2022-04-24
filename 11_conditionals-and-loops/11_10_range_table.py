# Read up on `range()` and additional options for `print()`.
# Then use a loop to print the following table to the console:
#
# 0 1 2 3 4 5 6 7 8 9
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47 48 49
from typing import List


line_1 = ""
line_2 = ""
line_3 = ""
line_4 = ""
line_5 = ""

for num in range(10):
    line_1 += (str(num)) + (" ")
for num in range(10,20):
    line_2 += (str(num)) + (" ") 
for num in range(20,30):
    line_3 += (str(num)) + (" ")
for num in range(30,40):
    line_4 += (str(num)) + (" ")
for num in range(40,50):
    line_5 += (str(num)) + (" ")

print(line_1)
print(line_2)
print(line_3)
print(line_4)
print(line_5)



    # if num in range(10,20):
    #     print(num)


# EXAMPLE:
# if char.isalpha():
#         solution += char