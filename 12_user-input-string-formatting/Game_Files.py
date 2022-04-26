def funny_name(name):
    prepend = 'Schl'
    rhyme_name = ''
    found_vowel = False
    for i in name:
        if i in 'aeiou':
            found_vowel = True
        if found_vowel == True:
            rhyme_name += i
    return prepend + rhyme_name
name = input('type name:')
rhyme_name = funny_name(name)
print(rhyme_name)

import random
import time
import sys
game = True
sword = False
dm = "Funk Shun"
rate = 0.05
pause = '…'

def sleep_time(time_value):
    if time_value == 1:
        time.sleep(0.05)
    if time_value == 2:
        time.sleep(0.01)
    if time_value == 3:
        time.sleep(1)
def funk_shun(speech):
    rate = .05
    pause_time = .75
    for i in speech:
        if i == pause:
            time.sleep(pause_time)
        else:
            print(i, end='', flush=True)
            time.sleep(rate)
    time.sleep(pause_time)
    print('\n')
narration = f"\n\
a surly little gnome walks out\n\
from behind a rock at the edge of the path \n\
and pokes you\n\
{pause}\x1B[3mhard\x1B[0m{pause}\n\
in your side with a knobby walking stick."
funk_shun(narration,)
sys.exit()
#for i in narration:
#    print(f”\x1B[3m{i}\x1B[0m”, end=‘’, flush=True)
#    time.sleep(0.05)
#    if i == pause:
#        time.sleep(.25)
funk_shun_speech = f"...and just who might you be??\n   "
funk_shun(funk_shun_speech)
sleep_time(3)
narration = f"\nhe’s hard to look at{pause}\n\
but you know better than to tell him so.{pause}\n\
\n\
because although he comes up only to your knees,  \n\
you can tell he’s quite fierce. {pause}a scrapper--\n\
and likely a biter to boot.{pause}\n\
in fact, {pause}\n\
he keeps eyeing your left boot like he might bite it\n\
    {pause}why the left one?...{pause}\n "
funk_shun(narration)
sleep_time(2)
sys.exit()
#for i in funk_shun_speech:
#
#    if i == pause:
#        time.sleep(.75)
#    else:
#        print(i, end=‘’, flush=True)
#        time.sleep(0.05)
narration = f"\nhe’s hard to look at{pause}\n\
but you know better than to tell him so.{pause}\n\
\n\
because although he comes up only to your knees,  \n\
you can tell he’s quite fierce. {pause}a scrapper--\n\
and likely a biter to boot.{pause}\n\
in fact, {pause}\n\
he keeps eyeing your left boot like he might bite it\n\
    {pause}why the left one?...{pause}\n "
#                                                                                                       come to think of it\n\
#                                                                                                       you realize you never even noticed that rock before...
for i in narration:
    print(f"\x1B[3m{i}\x1B[0m", end='', flush=True)
    time.sleep(0.05)
    if i == pause:
        sleep_time(1)
print('\n')
time.sleep(.05)
print('\n')
funk_shun_speech = "...and just WHO might you be, hmmpph??\n   "
for i in funk_shun_speech:
    print(i, end='', flush=True)
    time.sleep(0.05)
    if i == pause:
        time.sleep(.75)
print(" ")
name = input()
print('\n')
funk_shun_speech = f"\nhmmmm...{pause}\n’{name},' you say?"
for i in funk_shun_speech:
    print(i, end='', flush=True)
    time.sleep(rate)
    if i == pause:
        time.sleep(.75)
print('\n')
time.sleep(1)
narration = "\nhe looks at you with his one good eye"
for i in narration:    #italic
    print(f"\x1B[3m{i}\x1B[0m", end='', flush=True)
    time.sleep(rate)
    if i == pause:
        time.sleep(.75)
print('\n')
time.sleep(1)
narration = "\nto himself he says"
for i in narration:    #italic
    print(f"\x1B[3m{i}\x1B[0m", end='', flush=True)
    time.sleep(rate)
    if i == pause:
        time.sleep(.75)
print('\n')
funk_shun_speech = f"\n{name} {pause} rhymes with Schl{name}.{pause}\n I have a cousin named {name}. {pause}‘Tis a strange name, {pause}{pause}{pause}\nbut I like it! {pause}\n\
We don’t get many wanderers here in Smirkwood.\n\
{pause} That’s usually for the best if you ask me.\n\
But you seem harmless enough, I suppose. \n\
At any rate, I’m called {dm}. {pause}\nWelcome to Smirkwood, {name}!"
for i in funk_shun_speech:
    print(i, end='', flush=True)
    time.sleep(0.05)
    if i == pause:
        time.sleep(.75)
print('\n')
sleep_time(3)























