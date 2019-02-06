"""
Created on : 08/10/18
author: @rodolfo_herrera"""

""" Docstring:
In this game you are transported to an Enchanted Forest and must escape from a powerful Hunter, by following a predetermined path
to the Temple portal.The game consists of three main stages, representing different parts of the forest. You must succesfully
navigate through them in order to succeed. There is an optional path at the start that can be taken before the first challenge.

Challenges:

0) First Hunt
1) The Fairy meadow
2) The Hunter
3) The Temple

B) Known bugs or errors :
None
"""

import random
import time

#Start
def start():

    global name
    global lines

    lines = ('_' * 120)

    print(lines)
    print("""
\t\t _____           _                 _           _  ______                  _
\t\t|  ___|         | |               | |         | | |  ___|                | |
\t\t| |__ _ __   ___| |__   __ _ _ __ | |_ ___  __| | | |_ ___  _ __ ___  ___| |_
\t\t|  __| '_ \ / __| '_ \ / _` | '_ \| __/ _ \/ _` | |  _/ _ \| '__/ _ \/ __| __|
\t\t| |__| | | | (__| | | | (_| | | | | ||  __/ (_| | | || (_) | | |  __/\__ \ |_
\t\t\____/_| |_|\___|_| |_|\__,_|_| |_|\__\___|\__,_| \_| \___/|_|  \___||___/\__|

""")

    print(lines)

    print("\nYou wake up in a mysterious, wooded Land.")
    input('\n-Press any key to continue-\n')

    name = input('Please type your name:\n\n>')

    print(lines)
    print(f"""
MYSTERIOUS VOICE: Welcome to the Enchanted Forest {name}!

Sadly you came at a really bad time, as the Hunter is looking to dispose of any newcomers!

In order for you to survive, you need to go to the Fairy's territory and ask for their help. Just
follow the trail ahead and you should be set.""")
    print(lines)

    first_choice()

#First Choice
def first_choice():
#This function allows you to go to the optional challenge or the first challenge. It has
# a simple conditional structure and allows the user to rest without having to type the
#name again.

    input('\n-Press any key to continue-\n')

    print("""What will you do?
1)Face the Hunter
2)Rest
3)Reach Fairy's meadow""")

    choice_1 = input('\n>')
    choice_1 = choice_1.lower()


    if '1' in choice_1 or 'hunter' in choice_1:

        optional_challenge()

    elif '2' in choice_1 or 'rest' in choice_1 :

        print('\nMYSTERIOUS VOICE: There is no time to sleep! Hurry up!! \n')
        first_count = 1
        first_choice()

    elif '3' in choice_1 or "reach fairy" in choice_1:

        fairy_area(1)

    else:

        print('\nSorry I didn\'t get that. Choose again!\n')
        first_choice()


#Optional Challenge
def optional_challenge():
#An extra challenge. It is composed of a simple conditional and was made to simplify the
#else function, in case you typed a wrong menssage.

    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    print(lines )

    print("""
You decide to face you fears and go straight into the path of danger. You feel a powerful presence
that grows stronger after every step...until even the air seems to weight you down.""")

    print(lines)

    input('\n-Press any key to continue-\n')

    print("""
An unexpected arrow pierces through your chest and you hear a maniatical laugh in the background,
as you slowly lose consciousness. """)

    optional_answer = input("""\nWhat should you do?
1) Try to escape.
2) Curse the Hunter\n\n>""")
    optional_answer = optional_answer.lower()


    if optional_answer == '1' or optional_answer == 'try to escape':

        print('A mysterious light blinds the enemy, as you make a miraculous escape.')

        input('\n-Press any key to continue-\n')

        fairy_area(2)

    elif optional_answer == '2' or optional_answer == 'curse':

        print('You utter unspeakable words, as the Hunter shoots his final arrow...')

        fail(0)

    else:

        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print('Wrong input. Please type again!')

        input('\n-Press any key to continue-\n')
        optional_challenge()






#Second Challenge Area
def fairy_area(f) :
#In this area you face your first challenge, which is a fight against an opponent of a fixed level.
#Your odds of success depend on your armor. The for loop is used to check elements of the list. The
#while loop is used to avoid a wrong command from the user. The first conditionals are to change the
#computer's response and the last conditionals (including the nested ones) determine the outcome of
#the challenge.

    if f == 1:

        print("""
You cross the dark forest until you reach the most beautiful place you have ever seen. Nested in
the hearth of the forest is a majestic meadow full of colour and splendor.""")

        input('\n-Press any key to continue-\n')

        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print(lines)

        print("""
FAIRY MOTHER: Welcome to our domain! We heard about your plight and are willing to help you out.
We can give you the map to a Temple that can return you home. Nevertheless, since nothing comes
for free, you will need to win a challenge first!""")

        print("""\n
For this challenge you will face one of my minions. You do not seem like the fittest of fighers,
so I will provide you with an enchanted shield and sword.

Choose wisely...  """)

        print(lines)

        input('\n-Press any key to continue-\n')

    else:
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print("""
You are barely conscious,but you manage to cross the dark forest. You reach a mesmerizing meadow.

Then,suddenly, a winged figure appears and you close you eyes in exhaustion. """)

        input('\n-Press any key to continue-\n')

        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print(lines)

        print("""
FAIRY MOTHER: Welcome to our domain! You were lucky one of our scouts was there to help you out.
We nursed you back to help and can give you a map to get out of this Realm.

Nevertheless, since nothing comes for free, you will need to win a challenge first!""")

        input('\n-Press any key to continue-\n')


        print("""\n
For this challenge you will  face one of my minions. You do not seem like the fittest of fighers,
 so I will provide you with an enchanted shield and sword.

Choose wisely...  """)

        print(lines)

        input('\n-Press any key to continue-\n')


    items_list = []
    survival_chance = 0

    a = '1) Mirror Shield'
    b = '2) Fairy Dust Shield'
    c = '1) Mithril Sword'
    d = '2) Mystic Sword'

    print('Choose your defense:\n')

    shield_options = [a, b]

    for item in shield_options:

        print(item)
        #This makes sure that I can show the capitalized names, but avoids errors on the input.
        shield_options[shield_options.index(item)] = item.lower()

    shield_choice = input('\n> ')
    shield_choice = shield_choice.lower()
    shield_choice = shield_choice.strip()


    for item in shield_options:

        if shield_choice in item and shield_choice not in '\n' and shield_choice not in '\r\n' and shield_choice != 'shield':

            items_list.append(shield_options[shield_options.index(item)])
            break


    while items_list == []:

        shield_choice = input('There seems to be a typo. Please choose your item again:\n> ')

        shield_choice = shield_choice.lower()
        shield_choice = shield_choice.strip()

        for item in shield_options:

            if shield_choice in item and shield_choice not in '\n' and shield_choice not in '\r\n' and shield_choice != 'shield':

                items_list.append(shield_options[shield_options.index(item)])
                break


    if items_list[0] == shield_options[0] :

        print('''
FAIRY MOTHER: I do not think that is the strongest of shields... Perhaps you want to enchant your
opponent with his own beauty?''')

        input('\n-Press any key to continue-\n')


    elif items_list[0] == shield_options[1] :

        print('''
FAIRY MOTHER: So you want to use my own magic against me? How dare you!''')

        input('\n-Press any key to continue-\n')

    print('Choose your offense:\n')



    sword_options = [c,d]

    for item in sword_options:

        print(item)
        #This makes sure that I can show the capitalized names, but avoids errors on the input.
        sword_options[sword_options.index(item)] = item.lower()

    sword_choice = input('\n> ')

    sword_choice = sword_choice.lower()
    sword_choice = sword_choice.strip()


    for item in sword_options:

        if sword_choice in item and sword_choice not in '\n' and sword_choice not in '\r\n' and sword_choice != 'sword':

            items_list.append(sword_options[sword_options.index(item)])
            break


    while len(items_list) < 2:

        sword_choice = input('\nThere seems to be a typo. Please choose your item again:\n> ')

        sword_choice = sword_choice.lower()
        sword_choice = sword_choice.strip()

        for item in sword_options:

            if sword_choice in item and sword_choice not in '\n' and sword_choice not in '\r\n' and sword_choice != 'sword':

                items_list.append(sword_options[sword_options.index(item)])
                break



    if items_list[1] == sword_options[0] :

        print('''
FAIRY MOTHER:That is a big sword for such a small person... ''')

        mithril_answer = input("""
1) I am tougher than how I look.
2) Actually I wanted a bigger one. \n\n>""")

        if '1' in mithril_answer or 'tougher than' in mithril_answer:

            print('\nFAIRY MOTHER: We will see on the battlefield...')
            input("\n-Press any key to continue-\n")

        elif '2' in mithril_answer or 'bigger one' in mithril_answer:

            print('\nFAIRY MOTHER: That\'s cheecky!')
            input("\n-Press any key to continue-\n")

        else :

            print("Let's move on\n")
            input("\n-Press any key to continue-\n")



    elif items_list[1] == sword_options[1]:

        print('''
FAIRY MOTHER: A weapon used by the arcane wizards. Are you into magic? ''')

        mystic_answer = input('''
1) Do you mean the card game?
2) It is never too late to learn!
3) I didn\'t even know you needed magic for this! \n\n>''')
        mystic_answer = mystic_answer.lower()


        if mystic_answer == '1' or 'card_game' in mystic_answer:

            print('\nFAIRY MOTHER: That was not what I had in mind.')

            input("\n-Press any key to continue-\n")

        elif mystic_answer == '2' or 'never too late' in mystic_answer:

            print('\nFAIRY MOTHER: Growth mindset! I like that!')

            input("\n-Press any key to continue-\n")

        elif mystic_answer == '3' or 'know you needed magic' in mystic_answer:
            print('\nFAIRY MOTHER: You learn something new every day')
            input("\n-Press any key to continue-\n")

        else :
            print('What a bizarre answer...')
            input("\n-Press any key to continue-\n")




    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("FAIRY MOTHER: We are all set! Let's see what you are made of. Be prepared!")

    input("\n-Press any key to continue-\n")

    print(lines)

    print("""\nYour opponent comes defiantly. You both draw your swords.

FAIRY MOTHER: Let the Match begin!""")

    input('\n-Press any key to continue-')
    print(lines)

    print('\nYou engage in a vicious fight...')

    time.sleep(5)



    if items_list[0] == shield_options[0] :
        survival_chance += 0.2

        if items_list[1] == sword_options[0] :
            survival_chance += 0.5

        elif items_list[1] == sword_options[1] :
            survival_chance += 0.2

    elif items_list[0] == shield_options[1]:
        survival_chance += 0.5

        if items_list[1] == sword_options[0]:
            survival_chance += 0.5

        elif items_list[1] == sword_options[1] :
            survival_chance += 0.2



    if survival_chance == 1:

        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        print('\n' + lines)
        print(f"""
The battle was EPIC and your opponent lies on the ground, defeated.

FAIRY MOTHER:My minion didn't stand a chance. You are a true champion, {name}. Make good use of
this map and Godspeed!""")
        print(lines)

    elif survival_chance == 0.7 :
        print("""
You both seem to be evenly matched. Each blow comes stronger than the next and the whole Earth
seems to be shaking. Only luck and perseverance can decide who will win.""")

        input("\n-Press any key to continue-\n")

        luck = random.randint(1,2)

        if luck == 2 :

            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

            print('\n' + lines)
            print(f"""
But then you opponent falls to the ground and you deliver the final blow.

FAIRY MOTHER: I underestimated you. That was an excellent fight...Congratulations {name}! Make
good use of this map and Godspeed!""")
            print(lines)

        elif luck == 1 :

            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

            print('\n' + lines)

            print('\nYou fought bravely, but lost.\n')

            print(lines)

            fail(1)


    elif survival_chance < 0.7 :

        print("You fought bravely,but could barely scratch your opponent.")

        fail(1)


    input('\n-Press any key to continue-\n')

    print("""You received a map! You follow the route through the forest, as it becomes more dark
and sinister...""")

    input('\n-Press any key to continue-\n')

    hunter()





#2nd Challenge Area
def hunter():
#An area when you have to survive for three turns. The function has a while loop to control
#number of turns and your lives and a nested conditional structure for what happens when you
#get hit. If you succeed, you go to the third area.

    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    print(lines)

    print("""\nWhile walking to the Temple, you start to feel a powerful presence that grows stron-
ger after every step...until even the air seems to weight you down.""")

    print(lines)

    input('\n-Press any key to continue-\n')

    print('And then you see the Hunter! He stares at you and starts to draw his bow.\n')

    lives = 2
    turns = 3

    fatal = '\nThat was a fatal shot! You fell into the ground.\n'
    non_fatal_hit = '\nYou got hit! You won\'t survive another one!\n'
    miss = '\nYou narrowly avoided the arrow!\n'


    #While loop that starts the game
    while lives > 0 and turns > 0 :

        left = False
        right = False

        your_movement = input("""What should you do? Think fast!
    1) Advance to the left.
    2) Advance to the right.
    3) Freeze at the spot.\n\n>""")

        your_movement = your_movement.lower()

        arrow_direction1 = random.randint(1,2)

        if arrow_direction1 == 1 :
            right = True

        elif arrow_direction1 == 2 :
            left = True

        else :
            print('Error')

        if '1' in your_movement or 'left' in your_movement:

            if left == True :
                lives -= 1

                if lives == 0:
                    print(fatal)
                    fail(2)

                else :
                    print(non_fatal_hit)

            elif left == False :
                print(miss)

            input('-Press any key to continue-\n')
            print('The Hunter prepares another arrow...\n')
            input('-Press any key to continue-\n')

        elif '2' in your_movement or 'right' in your_movement:

            if right == True :
                lives -= 1

                if lives == 0:
                    print(fatal)
                    fail(2)

                else :
                    print(non_fatal_hit)

            elif right == False :
                print(miss)

            input('-Press any key to continue-\n')
            print('The Hunter prepares another arrow...\n')
            input('-Press any key to continue-\n')

        elif '3' in your_movement or 'freeze' in your_movement:

            lives -= 1

            if lives == 0:
                print(fatal)
                fail(2)

            else :
                print(non_fatal_hit)

            input('-Press any key to continue-\n')
            print('\n\nThe Hunter prepares another arrow...\n')
            input('\n-Press any key to continue\n')

        else:
            print('Error')
            turns += 1

        turns -= 1

        if turns == 0:
            print("""\n\n\n\n\n\nBut he suddenly losses his balance and falls to the ground. You take advantage to escape.""")

    input('\n-Press any key to continue\n')
    temple()


#Third Challenge Area
def temple():
#A transition function to the third area.

    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print('You keep going until you reach a beautiful temple')

    input('\n-Press any key to continue\n')

    print(lines)
    print(f"""\n
ANGELIC VOICE: Welcome to the Enchanted Temple {name}! This hallowed structure has been here since
times immemorial and is our gate to the different worlds.

In order to return home, you will need to step into the center of one of the three portals.

Be careful though! If you do not choose rightly, you will end up in the Demonic Dimension! \n""")
    print(lines)
    input('\n-Press any key to continue-\n')

    temple_choice()



def temple_choice():
#In this level the user must choose the correct door in order to win. The first conditionals
#refer to the user's first choice, and the for loops shows the portals to the user and the
#second checks if the user response is within each of the list variables and uses a conditional
#to give a response.

    choice_temple = input("""Are you ready?
1)Why don't you tell me which one is it?
2)I would rather face the Hunter, he is probably not as bad.
3)Let's do this!

> """)
    choice_temple = choice_temple.lower()


    if '1' in choice_temple or 'which one is it' in choice_temple:

        print("\nANGELIC VOICE: Where would be the fun in that?")
        input('\n-Press any key to continue-\n')
        temple_choice()


    elif '2' in choice_temple or 'face the hunter' in choice_temple:

        print("\nANGELIC VOICE: You barely survived last time! Don't be foolish!\n")
        input('\n-Press any key to continue-\n')
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        temple_choice()


    elif '3' in choice_temple or "yes" in choice_temple:

        print("\nBest of luck!")
        input('\n-Press any key to continue-\n')


    else:
        print('Sorry I didn\'t get that. Let\'s try again!')
        input('\n-Press any key to continue-\n')
        temple_choice()

    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    print(f"ANGELIC VOICE: This is the last treck! Remember, {name}, the decision could be fatal!")

    input('\n-Press any key to continue-\n')

    print('Please choose a portal:/n')


    total_portals_funny = ['Portal of Shenanigans','Portal of Gibberish','Portal of Spam']
    total_portals_deceive = ['Portal of Serenity','Portal of Victory','Portal of Enlightenment']
    total_portals_answer = ['Portal of Python','Portal of Grimm Brothers','Portal of Cyberspace']


    selected_portals = []
    funny_response = total_portals_funny[random.randint(0,2)]
    deceive_response = total_portals_deceive[random.randint(0,2)]
    portal_answer = total_portals_answer[random.randint(0,2)]


    selected_portals.insert(random.randint(0,2),funny_response)
    selected_portals.insert(random.randint(0,2),deceive_response)
    selected_portals.insert(random.randint(0,2), portal_answer)


    print(lines)
    for item in selected_portals:

        print('\n'+ item)

    print(lines)

    final_answer = input("\nWhich portal is it?\n\n>")
    final_answer = final_answer.lower()

    for item in total_portals_funny:

        item = item.lower()

        if final_answer in item:

            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

            print('\nThat sounds like absolute nonsense! Wrong portal!')
            input('\n-Press any key to continue-\n')

            print('\n\nYou fall into a dimension full of demons!')

            fail(3)

    for item in total_portals_deceive :

        item = item.lower()

        if final_answer in item:

            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

            print("\n\n\nYou were so close! But that was not the answer...")
            input('\n-Press any key to continue-\n')

            print('\n\nYou fall into a dimension full of demons!')

            fail(3)


    for item in total_portals_answer :

        item = item.lower()

        if final_answer in item:

            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
            print('You wake up at your bed, after a very realistic dream...')
            input('\n-Press any key to continue-\n')

            print(lines)
            print("""\n\t\t\t\tCongratulations! \n\n
                     \t\tYou won the game! """)
            print(lines)
            exit(1)

    else:

        print("Sorry I didn't get that. Try again!\n\n")

        temple_choice()




#Fail Function

def fail(x):
#The function that acts when you fail in the game. It has nested statements that can take you to
#different chackpoints or allow you to exit the game.

    input('\n-Press any key to continue-\n')

    print(lines)
    print("""
 \t\t\t\t   ___                   ___
 \t\t\t\t  / __|__ _ _ __  ___   / _ \ __ _____ _ _
 \t\t\t\t | (_ / _` | '  \/ -_) | (_) |\ V / -_) '_|
 \t\t\t\t  \___\__,_|_|_|_\___  \_____/ \_/\___|_|

    """)
    print(lines)

    revive = input('\nDo you want to try again? (y/n)\n\n>')
    revive = revive.lower()
    revive = revive.strip()


    if revive == 'y' :
        checkpoint = input('\nDo you want to start at the last checkpoint?\n\n')

        if checkpoint == 'y':

            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

            if x == 0:
                start()

            elif x == 1:
                fairy_area()

            elif x == 2 :
                hunter()

            elif x == 3:
                temple()


        elif checkpoint == 'n':

            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

            start()

        else:
            start()


    elif revive == 'n' :

        print('Thank you for playing. Better luck next time!')

        exit(0)

    else:
        fail()

start()
