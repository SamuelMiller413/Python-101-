# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

entry = input(f"write something:\n    ")

ay = ''
ee = ''
eye = ''
oh = ''
you = ''
why = ''

for i in entry:
    if i in 'aA':
        ay += i 
    if i in 'eE':
        ee += i
    if i in 'iI':
        eye += i
    if i in 'oO':
        oh += i
    if i in 'uU':
        you += i 
    if i in 'yY':                
        why += i

print(f"\n# of Occurrences of:\n\n A/a = {len(ay)}\nE/e = {len(ee)}\nI/i = {len(eye)}\nO/o = {len(oh)}\nU/u = {len(you)}\nY/y = {len(why)}\n\n")