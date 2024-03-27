#Number Guessing Game Objectives:
import random

# Area for constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Area for functions
# function to check the user's guess against the actual answer
def check_answer(user_guess, actual_answer, num_turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    if user_guess > actual_answer:
      print("Too high.")
      return num_turns - 1
    elif user_guess < actual_answer:
      print("Too low.")
      return num_turns - 1
    else:
      print(f"You got it! The answer was {actual_answer}.")
    
# function to set the difficulty level
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Include an ASCII art logo.
#import the logo from art.py
from art import logo
print(logo)

# Game function
def game():
    
    # Welcome the player to the game.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Set the answer to the number that the player needs to guess.
    answer = random.randint(1, 100)
    print(f"Pssst, the correct answer is {answer}") #comment this out before running real game

    # Set the number of turns the player has.
    turns = set_difficulty()

    # While loop to allow the player to guess the number.
    # set the guess global variable
    guess = 0
    # Track the number of turns and reduce by 1 if they get it wrong.
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
    
        # Allow the player to submit a guess for a number between 1 and 100.
        guess = int(input("Guess a number between 1 and 100: "))

        # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return

game()

# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).