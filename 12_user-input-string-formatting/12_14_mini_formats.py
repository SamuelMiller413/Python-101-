# Use Python's string mini-language to display the table
# that you've built before in a slightly better formatted manner:
#
#  0  1  2  3  4  5  6  7  8  9
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47 48 49

# i think the instructions mean to pay attention to the margins
# >>>>> see the spaceing on line 4

import sys

width = 2
x = ""
def line(x):
    for num in x:
        for base in 'd':
            print('{0:{width}}'.format(num, base=base, width=width), end=' ')
    print()

print()
line(range(10))
line(range(10,20))
line(range(20,30))
line(range(30,40))
line(range(40,50))

# >>>>>>>    even better!    <<<<<<<

def enil(x):
    for num in x:
        for base in 'd':
            print(f"{num:{width}}", end=" ")
    print()

print()
enil(range(10))
enil(range(10,20))
enil(range(20,30))
enil(range(30,40))
enil(range(40,50))

# >>>>>>>>>>>>>>>>>> or <<<<<<<<<<<<<<<<<<<<

print("\n\n")
for num in range(10):
    for base in 'd':
        print('{0:{width}}'.format(num, base=base, width=width), end=' ')
print()
for num in range(10,20):
    print('{0:{width}}'.format(num, width=width), end=' ')
print()
for num in range(20,30):
    print('{0:{width}}'.format(num, width=width), end=' ')
print()
for num in range(30,40):
    print('{0:{width}}'.format(num, width=width), end=' ')
print()
for num in range(40,50):
    print('{0:{width}}'.format(num, width=width), end=' ')
print()
print("\n\n")

