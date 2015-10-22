# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

num_range = 100
max_guesses = 7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, num_range, max_guesses, remaining_guesses
    
    secret_number = random.randrange(0, num_range)    
    remaining_guesses = max_guesses
    
    print
    print "New game. Range is from 0 to", num_range
    print "Number of remaining guesses is", remaining_guesses

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range, max_guesses
    
    num_range = 100
    max_guesses = 7
    new_game()
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range, max_guesses
    
    num_range = 1000
    max_guesses = 10
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global secret_number, remaining_guesses
    
    try:
        guess = int(guess)
    except ValueError:
        print
        print "Guess must be an number"
        return

    print
    print "Guess was", guess
    remaining_guesses -= 1
    print "Number of remaining guesses is", remaining_guesses
    
    if guess == secret_number:
        print "Correct!"
        new_game()
        return
    elif remaining_guesses == 0:
        print "You ran out of guesses.  The number was", secret_number
        new_game()
        return
    elif guess < secret_number:
        print "Higher!"
    else:
        print "Lower!"

# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
