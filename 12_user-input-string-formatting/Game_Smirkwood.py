import time
import random

prompting = True
funk_shun_not_called = True
sword = False
dm = "Funk Shun"
rate = 0.05
pause_rate = time.sleep(.75)
pause = '…'
pause_less = "æ"
narration_aug = 'narration, 2'

def funny_name(name):
    prefix = "Schl"
    rhyme_name = ""
    
    found_vowel = False
    for i in name:
        if i in 'aeiouyAEIOUY':
            found_vowel = True
        if found_vowel == True:
            rhyme_name += str.lower(i)
    return prefix + rhyme_name
                                
def sleep(time_value):
    if time_value == 1:
        time.sleep(1)
    if time_value == 2:
        time.sleep(2)
    if time_value == 3:
        time.sleep(3)
    if time_value == 4:
        time.sleep(4)                         

def funk_shun_speech(funk_shun, rate_ratio = 1, pause_time_ratio = 1):
    rate = .03 * rate_ratio
    pause_time = .75 * pause_time_ratio
    for i in funk_shun:
        if i in '.?!':                
            print(i, end='', flush=True)
            time.sleep(.2)
        elif i == ',':
            print(i, end='', flush=True)
            time.sleep(.15)
        elif i == pause:
            time.sleep(pause_time)
        elif i == pause_less:
            time.sleep(.3)    
        else:
            print(i, end='', flush=True)
            time.sleep(rate)
    time.sleep(pause_time)
    print('\n')

def narration_speech(narration, rate_ratio = 1, pause_time_ratio = 1):
    rate = 0.02 * rate_ratio
    pause_time = .75 * pause_time_ratio
    
    for i in narration:
        if i in '.?!':                
            print(f"\x1B[3m{i}\x1B[0m", end='', flush=True)
            time.sleep(.2)
        elif i == ',':
            print(f"\x1B[3m{i}\x1B[0m", end='', flush=True)
            time.sleep(.15)
        elif i == pause:
            time.sleep(pause_time)
        elif i == pause_less:
            time.sleep(.3)
        else:
            print(f"\x1B[3m{i}\x1B[0m", end='', flush=True)
            time.sleep(rate)
    time.sleep(pause_time)
    print('\n')

def narration_speech_aug(narration, rate_ratio = 1, pause_time_ratio = 1):
    rate = 0.02 * rate_ratio
    pause_time = .75 * pause_time_ratio
    
    for i in narration:
        if i in '.?!':                 
            print(f"\x1B[3m{i}\x1B[0m", end='', flush=True)
            time.sleep(.2)
        elif i == ',':
            print(f"\x1B[3m{i}\x1B[0m", end='', flush=True)
            time.sleep(.15)
        elif i == pause:
            time.sleep(pause_time)
        elif i == pause_less:
            time.sleep(.3)
        
        else:
            print(f"\x1B[3m{i}\x1B[0m", end='', flush=True)
            time.sleep(rate)
    time.sleep(pause_time)
    print('\n')


narration = f"\n\
a surly little gnome walks out\n\
from behind a rock at the edge of the path \n\
and pokes you\n\
{pause_less}hard{pause_less}\n\
in your side with a knobby walking stick."
narration_speech(narration)

time.sleep(1)
print('\n')

funk_shun = f"...and just who might you be, then??\n"
funk_shun_speech(funk_shun)

narration = f"holding your side,\n\
you grimace.\n\
he's not exactly pleasant to look at{pause}\n\
and he's terribly pungent\n\
but don't tell him so.{pause}\n\
he comes up only to your knees,  \n\
but you can tell he's quite fierce. {pause}a scrapper--\n\
probably a biter, you decide.{pause}\n\
best to keep your distance."
narration_speech(narration)

funk_shun = "...and just WHO might you be, hmmpph??"
funk_shun_speech(funk_shun)                                    
name = str.capitalize(input("-> My name is: "))
rhyme_name = funny_name(name)

funk_shun = f"\nhmmmm...{pause}\n'{name}', you say?"
funk_shun_speech(funk_shun)
print('\n')
time.sleep(1)

narration = "\nhe looks at you with his one good eye"
narration_speech(narration, 2, 2)

time.sleep(1)

narration = f"\nthen,{pause} to himself he says"
narration_speech(narration)

print('\n')

funk_shun = f"\n'{name}',{pause}\n\
rhymes with {rhyme_name}.{pause}"
funk_shun_speech(funk_shun, 2, 2)

narration = "then looking back to you"
narration_speech(narration)

funk_shun = f"I have a cousin named {name}.{pause}\n\
'Tis a strange name, {pause}{pause}{pause}\n\
but I like it!{pause}\n\
Oh and by the way,{pause}\n\
you have a beautiful dog, I must say."
funk_shun_speech(funk_shun)

narration = "you have no dog..."
narration_speech(narration, 2, 2)

funk_shun = "And your prounouns, pray tell?"
funk_shun_speech(funk_shun)

pronouns = input("->My pronouns are: ")
funk_shun = f"\nAh, {pronouns}. Makes sense to me.\nWe gnomes have a saying:\n{pause}'If you don't gnome my pronouns,{pause_less}\nthen you don't gnome me!'{pause}\nAt any rate, I'm called {dm}, he/him/his, thank you.{pause}"
funk_shun_speech(funk_shun)

narration = f"he scratches his belly with his yellow fingernails\nas he surveys the lush, green woods surrounding you."
narration_speech(narration)

funk_shun = f"I'll tell you, {name},\nwe don’t get many wanderers here in Smirkwood,{pause}\nand that's usually for the best if you ask me.\nBut you seem harmless enough, I suppose.{pause}\nthat {pause_less} and I like your dog.\n\""
funk_shun_speech(funk_shun)
funk_shun = f"So welcome to Smirkwood, {name}!"
funk_shun_speech(funk_shun)

narration = f"....{pause}\nhe takes a healthy swig\nfrom a skin slung over his shoulder."
narration_speech(narration)
sleep('half')
print("*burps*\n")
sleep('half')
narration = f"he notices you eyeing his drink.\nfor a moment he pulls it closer to him.{pause}\nthen {pause}as if some strange force\nreminded him of his manners,{pause}\nhe begrudginly holds it out to you in offer,\n"    
narration_speech(narration)
while prompting:
    
    prompt_1 = str.lower(input("'yes'  > Why yes, thank you.\n\n  \x1B[3mor\x1B[0m\n  \n'no'  > Ummm. Thanks, but no thanks.\n\n  -> "))
    
    while (prompt_1 != 'yes') and (prompt_1 != 'no'):
        funk_shun = f"Huh? 'yes' or 'no' would suffice, thank you."
        funk_shun_speech(funk_shun)
        prompt_1 = input()
    if prompt_1 == 'yes':
        while True:
            sleep(1)
            narration = f"\nyou take it, thanking him.\nas you bring it to your mouth,\nyou try not to notice\nthat the mouth of the skin is crusted over\nfrom years of use.{pause}\nyou close your eyes and take a swig.{pause}\nit’s sickeningly sweet,{pause}\n     warm,{pause}\n         and going bad...{pause}\nHe notices you grimace at the taste\nand laughs sadistically."
            narration_speech(narration)
            funk_shun = f"Not a fan of sugar water, eh?\nHa!\nWell and good, then.\nMore for me!"
            funk_shun_speech(funk_shun)
            narration = f"you hand it back to him."
            narration_speech(narration)
            break
    elif prompt_1 == 'no':
        while True:
            sleep(1)
            narration = f"\nyou tell him thanks, but no thanks.\ngood job using your manners, {name}.\nLooking at you like you’d just refused a lordship,\nhe says:"
            narration_speech(narration)
            funk_shun = f"Not a fan of sugar water, eh? \nHa!\nWell and good, then.\nMore for me!" 
            funk_shun_speech(funk_shun)
            narration = f"He takes another gulp before\nre-slinging the pouch over his knobby shoulder."  
            narration_speech(narration)
            break
    break
funk_shun = f"Now as I was saying, we don’t get many wanderers in Smirkwood. We-{pause}\n...\nWhat’s \x1B[3mthat\x1B[0m look for?\nAre you surprised?\nWow, you really \x1B[3maren't\x1B[0m from around here.\nDoes that mean you haven’t heard the stories?\nSheesh."
funk_shun_speech(funk_shun)

narration = f"as he brings his brings palm to forehead in exasperation,\nyou wonder to yourself\nwhy he’s so surprised by your ignorance\ngiven that he just admitted\nthat visitors here are so few.\nhowever, the fact remains:\nyou’re completely unfamiliar with this place\nand you have no idea what you might run into here."
narration_speech(narration)

while prompting:
    dragon_story = False
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>     
    prompt_2 = str.lower(input("Do you want to know more about the 'stories' he mentions?\n\n'yes'  > Wait, what stories?\n\n  \x1B[3mor\x1B[0m\n\n'no'  > \x1B[3myou decide that you can handle whatever comes your way.\nAnd clear your throat significantly.\x1B[0m\n\n  -> "))
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
    while (prompt_2 != 'yes') and (prompt_2 != 'no'):
        funk_shun = f"\nHuh? 'yes' or 'no' would suffice, than you."
        funk_shun_speech(funk_shun)
        prompt_2 = str.lower(input())
    
    if prompt_2 == 'yes':
        while True:
            sleep(1)
            narration = f"\nyou take the bait..."
            narration_speech(narration)
            funk_shun = f"Really? So you \x1B[3mdo\x1B[0m have some sense.\nWell where to start, then??\nI’ve got one word for you, {name}: Huge, scary dragons!"
            funk_shun_speech(funk_shun)
            narration = "..."
            narration_speech(narration, 2, 2)
            narration = f"The two of you (or 3?) begin down the path,{pause_less}\nstrolling beneath boughs of ancient trees hanging over you,{pause_less}\nas they shade you from the noonday sun.{pause}\nYou breathe in the smell of the flowers blossoming in their branches,{pause_less}\n(all the more since they take the\nsour edge off your companion’s scent).{pause_less}\n\
You savor the silent patience\nof a realm untouched\nby either hurry or flurry.{pause}\nAs you stroll along,\nyou start to ask him to share more about the dragon\nbut he cuts you off with a silent wave of his hand.\nThe two of you listen to the birds and their songs,{pause}\nto the wind as it dances.{pause}{pause}\n\
After a while,\nyou come to the foot of a great mountain.{pause}\nAs you near it,{pause_less}\nyou nearly stumble on a rock jutting out from the ground.{pause_less}\nLucky for you,\nhe points it out to you in friendly warning,\nand together,\nyou both ascend the slight rise approaching the mountain.{pause}\n\
Carved into the ancient stone,\nthere are two weathered oaken doors,\nidentical and superb in their craftmanship\n.{pause}\n.{pause}\nSpeaking for the first time\nsince you commenced your journey together,{pause_less}he says:"
            narration_speech(narration)
            funk_shun = f"This is Door & Door.\nI call them D&D for short, but that’s unimportant.\nThey’re locked, but luckily,\nI possess the key that opens both.\nBut first,\nyou should know what you’re getting into before I let you in.\nSo take a seat there, {name}.\nThis is quite the yearn I’m about to spin."
            funk_shun_speech(funk_shun)
            narration = f"Hmmm...\nYou sit down in front of D&D,\nbracing yourself for the exhaustion that’s sure to set in soon.\nhe clears his throat,\nfrom which escapes a glob of you-don’t-wanna-know-what.\nbefore it splatters on the ground\nhe begins the tale of The Dragon Dragon..."
            narration_speech(narration)
            dragon_story_intro = True
            break   #go to dragon story
        break

    if prompt_2 == 'no':
        while True:
            sleep(2)
            funk_shun = f"\nHmmm...{pause}You seem like one with great purpose.\nI’ll get out of your way."
            funk_shun_speech(funk_shun)
            narration = f"you suspect he may be mocking you.\nbut you’re glad to move on without him.\nas he’s leaving, he stops{pause}\nas if liminally aware of his better nature,\nif only for a brief moment.\nhe turns to face you."
            narration_speech(narration)
            funk_shun = f"Just one last thing.{pause}\nIf you should need anything,\nsay you’re in trouble{pause}\nor you just need a friend,{pause}\nyou have only to say,{pause}\n‘call Funk Shun’.{pause}\nAs long as you’re still in Smirkwood,\nI’ll be there."
            funk_shun_speech(funk_shun)
            narration = f"you nod, {pause}thanking him."
            narration_speech(narration)
            funk_shun = f"oh it’s the least I can do.\n.{pause}.{pause}.{pause}\nEspecially after the last time\na person came wandering through here and –{pause_less}\nOh there I go again, prattling on.{pause}\nI suppose I should be getting on\nbefore I bore you and the dog.{pause}\nGood luck, {rhyme_name}."
            funk_shun_speech(funk_shun)
            narration = f"then,{pause} under his stinky breath:"
            narration_speech(narration)
            funk_shun = f"\x1B[3mYou'll need it!\x1B[0m"
            funk_shun_speech(funk_shun)
            narration = f"ominous.{pause}.{pause}.{pause}\nmeh ¯\_(ツ)_/¯{pause}\nit’s probably nothing, you suppose.\nhe starts away into the woods,{pause_less}\ndisregarding the path{pause_less}\nwhistling a tune to himself that reminds you...{pause}\nof a song you’ve not heard in a long while...{pause}\nno time for that now though,{pause}\n\
no time.\nhe disappears into the woods,\nyet his sweet and sour pungence lingers on...\nhanging like an overripe pear that\nrefuses to fall..."
            narration_speech(narration) 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>            
            prompt_3b = str.lower(input("Call after him, telling him you've changed you're mind?\n\n'yes'  > \x1B[3m\x1B[0mHe comes back\x1B[0m\n  \x1B[3mor\x1B[0m\n'no'  > \x1B[3myou're just glad he's gone.\x1B[0m\n  -> ")) 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            while (prompt_3b != 'yes') and (prompt_3b != 'no'):
                narration = f"did you mean 'yes' or 'no'?"
                narration_speech(narration)
                prompt_3b = str.lower(input())
            
            if prompt_3b == 'yes':
                while True:
                    narration = f"he appears suddenly beside you,\npetting the air with genuine affection,\nthen looks up at you." 
                    narration_speech(narration)
                    funk_shun = f"Really?? Oh good!"
                    funk_shun_speech(funk_shun)
                    narration = f"a wide, yellow grin grows happily on his face."
                    narration_speech(narration)
                    funk_shun = f"You can’t imagine how tired I am\nof talking only to myself.\nWell where to start, then??\nI’ve got one word for you, {name}: Huge, scary dragons!"
                    funk_shun_speech(funk_shun)
                    narration = "..."
                    narration_speech(narration, 2, 2)
                    narration = f"The two of you (or 3?) begin down the path,{pause_less}\nstrolling beneath boughs of ancient trees hanging over you,{pause_less}\nas they shade you from the noonday sun.{pause}\nYou breathe in the smell of the flowers blossoming in their branches,{pause_less}\n(all the more since they take the\nsour edge off your companion’s scent).{pause_less}\n\
You savor the silent patience\nof a realm untouched\nby either hurry or flurry.{pause}\nAs you stroll along,\nyou start to ask him to share more about the dragon\nbut he cuts you off with a silent wave of his hand.\nThe two of you listen to the birds and their songs,{pause}\nto the wind as it dances.{pause}{pause}\n\
After a while,\nyou come to the foot of a great mountain.{pause}\nAs you near it,{pause_less}\nyou nearly stumble on a rock jutting out from the ground.{pause_less}\nLucky for you,\nhe points it out to you in friendly warning,\nand together,\nyou both ascend the slight rise approaching the mountain.{pause}\n\
Carved into the ancient stone,\nthere are two weathered oaken doors,\nidentical and superb in their craftmanship\n.{pause}\n.{pause}\nSpeaking for the first time\nsince you commenced your journey together,{pause_less}he says:"
                    narration_speech(narration)
                    funk_shun = f"This is Door & Door.\nI call them D&D for short, but that’s unimportant.\nThey’re locked, but luckily,\nI possess the key that opens both.\nBut first,\nyou should know what you’re getting into before I let you in.\nSo take a seat there, {name}.\nThis is quite the yearn I’m about to spin."
                    funk_shun_speech(funk_shun)
                    narration = f"Hmmm...\nYou sit down in front of D&D,\nbracing yourself for the exhaustion that’s sure to set in soon.\nhe clears his throat,\nfrom which escapes a glob of you-don’t-wanna-know-what.\nbefore it splatters on the ground\nhe begins the tale of The Dragon Dragon..."
                    narration_speech(narration)

                    dragon_story = True
                    break
                break
                      # go to dragon story                
            
            if prompt_3b == 'no':
                while True:   
                    narration = f"you're side still hurts\nand you're glad as ever he's gone.{pause}\nstill, you take note: you can always call him back{pause}\nshould you need him, by just saying,\n‘call funk shun’.\n\nYou continue down the path for a little while.{pause}\nAs you stroll,{pause}\n\
the boughs of ancient trees hang over you,{pause_less}\nshading you from the noonday sun.{pause}\nYou savor the smell of the flowers blossoming in their branches,{pause_less}\nand the silent patience of a realm untouched\nby the hand of the city,\nthat hand that reaches for you like that of the grave itself,{pause}\n\
that hand that eventually captures{pause_less}\nand strangles even the best of us.{pause}\n{pause}.\n{pause}.\n{pause}.\nWhere did that come from?\nYou’re quite the cynic, aren’t you?{pause}\nAs you begin to argue with yourself,{pause_less}\nin your own head,{pause_less}\nsomething hard\nand as unforgiving as your own self-opinion\ntrips you up!\n\n\
OUCH!\n\nIt’s a rock, jutting out from the dirt.\nYou look up and\nyour gaze lands upon the foot of a great mountain.\n{pause}\nCut into the ancient stone are two oaken doors,\n{pause_less}worn and weathered by time,{pause_less}\nbut sturdy in their stubborn refusal to give way\nto the incessant insult of entropy\nand its constant,\n\
{pause}insidious{pause}\nhatred for all things ordered and alive—\n       —okay whoa, seriously.\n        \nyou’re just bumming yourself out now...\n{pause}\nyou leave the entropy stuff aside for now\nand study the strange old doors.\n\nYou have a notion to open them up and\nfind out what’s behind them.\n\
An old adage about\nsome ill-fated cat comes to mind\nbut you leave that aside as well,\nhiding it somewhere deep\nin your mind near the entropy loop.\n\nYou climb the slight rise leading to the doors\nand approach them\nwith a cautious excitement.{pause_less}.{pause_less}.{pause_less}"
                    narration_speech(narration)

                    while True:

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                        prompt_3c = str.lower(input(f"Would you like to try the 'left' door?\n  Or the 'right' door?\n   Or stop and 'think' for a moment?\n\n'left', 'right', \x1B[3mor\x1B[0m 'think'\n  -> ")) 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    
                        while (prompt_3c != 'left') and (prompt_3c != 'right') and (prompt_3c != 'think'):
                            narration = f"did you mean 'left', 'right', or 'think'?"
                            narration_speech(narration)
                            prompt_3c = str.lower(input())
                        if prompt_3c == 'left':
                            while True:
                                sleep(1)
                                print("\n*Tries Door*\n")
                                sleep(1)
                                narration = f"Oh snap! It's locked!"
                                narration_speech(narration)
                                break

                        if prompt_3c == 'right':
                            while True:
                                sleep(1)
                                print("\n*Tries Door*\n")
                                sleep(1)
                                narration = f"Oh snap! It's locked!"
                                narration_speech(narration)
                                break
                        
                        if prompt_3c == 'think':
                            while True:
                                sleep(1)
                                print("\n*Tries Thinking*\n")
                                sleep(1)
                                print("Wise Choice!")
                                narration = f"You plop yourself down in front of the entrances.{pause}\nWhat're you going to do now?{pause}?"
                                narration_speech(narration)
                                narration = f"If only there was someone you could call.{pause_less}.{pause_less}.{pause_less}\nCall.{pause_less}.{pause_less}.{pause_less}"
                                narration_speech(narration)
                                narration = f"Wait!{pause_less} Didn’t that nasty gnome\nOffer to help you should you need him?{pause_less}\nbut what was it he said to do?.{pause_less}\n.{pause_less}\n.{pause_less}\nHe said to ‘call’—{pause}wait, what what his name again?\n\nsay the magic words..."
                                narration_speech(narration)
                                
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                prompt_3d = str.lower(input(f"Who you gonna ‘call’?\n -> "))
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#                                 
                                while prompt_3d != 'call funk shun':
                                    narration = f"'call' him by name\n"
                                    narration(prompt_3d)
                                    prompt_3d = str.lower(input())
                                
                                if prompt_3d == "call funk shun":
                                    while True:
                                        print("\n*¡POP!*\n")
                                        narration = f"Out of thin air,{pause}\n right in front you\n appears the gnome from earlier!{pause}\nin all his{pause}...um...{pause}glory...{pause}"
                                        narration_speech(narration)
                                        funk_shun = f"Well hello there!{pause}\n{name}, is it?{pause}\nIt appears you decided to call me.{pause}\nThey always do.{pause_less}.{pause_less}.{pause_less}"
                                        funk_shun_speech(funk_shun)
                                        narration = f"Wait a second,{pause}\nwhat does that mean?{pause}?{pause_less}\n\nBut before you can inquire,\nhe uncorks his waterskin and takes a long gulp\nofthe rotten, sweet liquid." 
                                        narration_speech(narration)
                                        funk_shun = f"Aahh!{pause} That’s the good stuff!{pause_less}\nYou don’t know what you’re missing out on, {rhyme_name}.{pause_less}This is the nectar of the gods, I swear.{pause}\nOh!{pause_less}It looks like you’ve found Door & Door!\nGood friends of mine!\nI call them D&D for short.{pause}\nAt any rate,\n\
I bet you’ve noticed that they’re locked?{pause_less}\nFunny story about D&D..."          #Go to Dragon Story
                                        dragon_story == True
                                        break
                                    break 
                            break                         
                    break            
            break                                
    break

# Dragon Story

funk_shun = f"Long ago,\nwhen these vast woods were yet young,\nhardly even formed,\na great shape like a storm cloud descended upon humble Smirkwood.\nAll was confusion, all was unclear.\nThe order of things here was then still being set in place,\nas if some great author had just begun to discover\nthe language with which to form this world we now breathe in."
funk_shun_speech(funk_shun)
narration = f"As he embellishes,\nhe looks into the sky,\ngesturing with his dirt covered hands as if\nhe was painting broad strokes upon the sky.\nThen his right hand comes to his belly.\nHe scratches it absentmindedly as he turns to you..."     
narration_speech(narration)
funk_shun = f"Now, I know what you’re thinking, {rhyme_name}.\nYou’re wondering what a big\ncloud of confusion has to do with anything."
funk_shun_speech(funk_shun)
narration = f"He takes a swig of his sugar water,\n"
print("\n*burps*\n")
narration = f"he wipes his mouth on his hairy arm\nbefore returning cap to container."     
narration_speech(narration)



# double check prompt_4~~~!!
while prompting:
    prompt_4 = str.lower(input("Would you like Funk Shun to 'continue' or 'skip' to the end?\n\n'continue'  >\x1B[3mcontinue with story\x1B[0m\n   \x1B[3mor\x1B[0m\n'skip'  >\x1B[3mjust get on to the end!\x1B[0m\n \n  -> ")) 

    while (prompt_4 != 'continue') and (prompt_4 != 'skip'):
        prompt_4 = str.lower(input(f"did you mean 'continue' or 'skip'?\n\n  -> "))
        narration_speech(prompt_4)
            
    if prompt_4 == 'continue':
        while True:
            sleep(1)
            funk_shun = f"\nWell it wasn’t just a any old storm cloud thing.\nIt was a Dragon Cloud!{pause_less}\n I can see you don’t know what a Dragon Cloud is.\nWell the short of it is that before a dragon is really fleshed out,\nas it were,\nthey manifest as\n‘something of a feeling on the horizon of the world’s understanding.’{pause_less}\nAt least that’s what the great smirkwoodian scholar,\nGnome Chomsky, said in his classic gnome-tome,\n‘Understanding the Great Riddle.’\nI’ve never quite understood what he meant\nbut I suppose that’s sort of the point.{pause_less}\nAt any rate, Gnome Chomsky say it is through a 'process of understanding'\nthat a dragon forms from the great cloud of confusion.\nSome of the mystical Agnome-stics\nhave even gone so far as to claim that\na dragon is the very culmination of understanding itself.\nBut after all, what do they know?!"
            funk_shun_speech(funk_shun)   
            narration = f"You sense a joke in that last exclamation,\nbut are too afraid to think on it further."     
            narration_speech(narration)
            funk_shun = f"At any rate, we call him The Dragon Dragon.\nLegend has it he formed as Smirkwood\ncame to understand \x1B[3mitself\x1B[0m, as it were.\nThe forming of our beloved wood correlated directly\nwith the forming of the dragon.\nWhile I’m sure it’s just a coincidence,{pause_less}\nThey say his presence here was terrible!\nHe scoured the forest,\nstopping the poor gnomes of old as he happened upon them,\ndemanding of them the riddles they held\n– he loves riddles just like we do."
            funk_shun_speech(funk_shun)  
            narration = f"he pauses because he can see you have some questions."
            narration_speech(narration)
            
            prompt_4b = str.lower(input(f"Would you like to ask him:\n\n >Do you like 'riddles'?\n  >Do you like 'jokes' as well?\n   >what happened 'if' they didn't have a riddle?\n \x1B[3mor\x1B[0m\n    >Can you please just 'move' on?\n\n -> "))
            
            while (prompt_4b != 'riddles') and (prompt_4b != 'jokes') and (prompt_4b != 'if') and (prompt_4b !='move'):
                prompt_4b = str.lower(input(f"Did you mean 'riddles', 'jokes', 'if', 'move'?\n\n  -> "))  
                    
            if prompt_4b == 'riddles':
                while True:
                    funk_shun = f"\nWell, of course I do!\nI’m a Gnome ain’t I?"
                    funk_shun_speech(funk_shun)
                    prompt_4b = str.lower(input(f"Would you like to ask him:\n >Do you like 'riddles'?\n >Do you like 'jokes' as well?\n >what happened 'if' they didn't have a riddle?\n \x1B[3mor\x1B[0m\n >Can you please just 'move' on?\n\n -> "))
                    break
            if prompt_4b == 'jokes':
                while True:
                    funk_shun = f"\nOh most certainly!\nBut no time for jokes now.\nAsk me later!"
                    funk_shun_speech(funk_shun)
                    prompt_4b = str.lower(input(f"Would you like to ask him:\n >Do you like 'riddles'?\n >Do you like 'jokes' as well?\n >what happened 'if' they didn't have a riddle?\n \x1B[3mor\x1B[0m\n >Can you please just 'move' on?\n\n -> "))
                    break
            if prompt_4b == 'if':
                while True: 
                    funk_shun = f"\nHe turned them into a –"
                    funk_shun_speech(funk_shun)
                    print("\n*gasps*\n")
                    funk_shun = f"– a human...\nI mean...\n...no offense, you understand.\nI’ve had human friends before..."
                    funk_shun_speech(funk_shun)
                    prompt_4b = str.lower(input(f"Would you like to ask him:\n >Do you like 'riddles'?\n >Do you like 'jokes' as well?\n >what happened 'if' they didn't have a riddle?\n \x1B[3mor\x1B[0m\n >Can you please just 'move' on?\n\n -> "))
                    break
            elif prompt_4b == 'move':
                while True:
                    break
            funk_shun = f"\nWell at any rate, that was long ago.\nHe hasn’t left his lair in many generations."
            funk_shun_speech(funk_shun)
            break   
        break
    
    
    if prompt_4 == 'skip':
        while True:
            sleep(1)
            narration = f"\nyou ask him to please just get to the point\nso we can all get home by dinner."
            narration_speech(narration)
            break
        break
    break
# Dragon Story Coda


narration = f""     
narration_speech(narration)
funk_shun = f""
funk_shun_speech(funk_shun)                                             


            




funk_shun = f""
funk_shun_speech(funk_shun)   
narration = f""     
narration_speech(narration)
funk_shun = f""
funk_shun_speech(funk_shun)   
narration = f""     
narration_speech(narration)
funk_shun = f""
funk_shun_speech(funk_shun)   
narration = f""     
narration_speech(narration)
funk_shun = f""
funk_shun_speech(funk_shun)               
            

                
                


# 
# funk_shun = f""
# funk_shun_speech(funk_shun)
# narration = f""
# narration_speech(narration)
#                       
# 
# 
# 
# 
# 
# >>to fix up:<<
#       Make Funk's speech timed too, but faster than narrator
#       Indent Funk's speech
#
#       indent Narration
#
#       speed up or skip lines between lines in narration
#
#                       >>to design:<<
#       images for doors using text art
#       
#       dialogue headers like a play
#
#       list options in scenarios with >= 2 options
#
#       utilizes mini language alignment commands
#           eg narration shows up in center?
#
#       Funk asks for what pronouns you use
# 
#       dynamic, speech like pauses in narration/speech
#           insert extra spaces in the dialogue
# 
# #
#
#                       >>to write:<<
#       Short intro into the world of smirkwood
#           you go there looking for a present for your friend who loves smirkwood 
#           but is too afraid, or otherwise unable, to go

#       Funk Shun's back story, with option to hear it. if player chooses this option,
#           Funk Shun tells his life story

#       Option to eat strange mushrooms or cave slime
#           triggers an endless loop

#       The Draggin' Dragon?
#           depressed
#           recites poetry
#           asks you to sleigh him
#               if you sleigh him
#                   return: "you win?..."
#           riddles are his favorite
#           answer the riddle he's never figured out and he promises
#               to seek professional help
#                   what is it?? 
#                -or-   since he knows the answer to every riddle ever, 
#                           if you can come up with a riddle he can't answer
#                           he has a reason to go on living
#                       you answer the riddle and he gives you a reward
#                       either he goes and takes care of the bullies for you
#                             if this, then he flys off to do so 
#                             and the game ends with an ambiguous
#                             "and the bullies never troubled you again!"
#                        else he gives you a reward which is the perfect gift for you friend
#                        >>¡¡The above 2 options can be presented to you and you can choose!!<<

#       find a way to work in "call Funk Shun" as a command
#           perhaps as a way to solve a certain puzzle
#               ¡¡ or to answer a riddle posed by the dragon !!
#          prompt: "who you gonna call?"
#               "Call Funk Shun!"
#       have Funk Shun tell jokes
#           cmd = 'joke'
#           he tells you jokes that he learned from his dearly departed friend, Gnome Macdonald
#            he sets up joke
#               prompt: ~'idk. what?', or ~'who's there?'
#
#           >>Joke: knock knock. who's there? gnome. gnome who? gnome-or jokes please, I'm dying over here!
#               *slaps knee*        
# #
#               Text being displayed like typing
# speech = "hello there Samuel. I'm your computer" 
# for i in speech:
#     print(i, end='', flush=True)
#     time.sleep(0.1)
# print('\n')





# Ask the player for their name.# name = input('\nEnter your name:\n')
#       slice out first character up to where the first vowel appears
# Display a message that greets them and introduces them to the game world.
# Present them with a choice between two doors.
# If they choose the left door, they'll see an empty room.
# If they choose the right door, then they encounter a dragon.
# In both cases, they have the option to return to the previous room or interact further.
# When in the seemingly empty room, they can choose to look around. 
#           If they do so, they will find a sword. They can choose to take it or leave it.
# When encountering the dragon, they have the choice to fight it.
# If they have the sword from the other room, then they will be able to defeat it and win the game.
# If they don't have the sword, then they will be eaten by the dragon and lose the game.
# 
# 
# # def funk_shun(speech, rate_ratio = 1, pause_time_ratio = 1):
#     rate = 0.05*rate_ratio
#     pause_time = 1*pause_time_ratio
#     for i in speech:
#         if i == pause:
#             time.sleep(pause_time)
#         else:
#             print(i, end='', flush=True)
#             time.sleep(pause_time)
#     time.sleep(pause_time)
#     print('\n')