# Higher/lower game

# Import modules
import random

# Import logo from art.py
from art import logo

# Import vs from art.py
from art import vs

# Import game_data from game_data.py
from game_data import data as game_data 

# Present user input to select higher/lower options base don game_data.py using random module
def game():
    print(logo)
    score = 0
    game_over = False
    data2 = random.choice(game_data)
    
    while not game_over:
        data1 = data2
        data2 = random.choice(game_data)
        if data1 == data2:
            data2 = random.choice(game_data)
        
        print(f"Compare A: {data1['name']}, a {data1['description']}, from {data1['country']}.")
        print("VS")
        print(f"Against B: {data2['name']}, a {data2['description']}, from {data2['country']}.")
        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_input == 'a':
            if data1['follower_count'] > data2['follower_count']:
                score += 1
                print(f"You're right! Current score: {score}.")
            else:
                print(f"Sorry, that's wrong. Final score: {score}.")
                game_over = True
        elif user_input == 'b':
            if data2['follower_count'] < data1['follower_count']:
                score += 1
                print(f"You're right! Current score: {score}.")
            else:
                print(f"Sorry, that's wrong. Final score: {score}.")
                game_over = True
                
game()