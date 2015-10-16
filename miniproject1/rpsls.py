# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

# global NAMES list used by both helper functions
NAMES = ["rock", "Spock", "paper", "lizard", "scissors"]

def name_to_number(name):
    """
    convert name to number
    throws a ValueError if name is invalid
    """

    # just find and return the index of name in NAMES
    # if/elif/else is too painful ..
    return NAMES.index(name)


def number_to_name(number):
    """
    convert number to name
    throws an IndexError if number is not in range [0,4]
    """
    
    # just return the correct element in NAMES
    # again, if/elif/else is too painful ..
    return NAMES[number]

import random

def rpsls(player_choice):
    """
    play a round of rock paper scissors lizard Spock
    takes the player choice as input
    generates a random choice for the computer
    determines the winner
    """
    
    # print a blank line to separate consecutive games
    print

    # print out the message for the player's choice
    print "Player chooses", player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses", comp_choice
    
    # compute difference of comp_number and player_number modulo five
    result = (comp_number - player_number) % 5
    
    # use if/elif/else to determine winner, print winner message
    if result == 1 or result == 2:
        print "Computer wins!"
    elif result == 3 or result == 4:
        print "Player wins!"
    else:
        print "Player and computer tie!"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


