# Treasure map program.

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

# Welcome people to the game
print("Welcome to Trasure Island.")
print("Your mission is to survive and find the treasure.")

# Ask the user to choose between left or right
choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'\n").lower()

# If the user chooses the wrong path, they die, otherwise they continue on.
if choice1 == "left":
    choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    if choice2 != "wait":
        print("You are eager to find the treasure, but this is water and in water are sharks. You are eaten by a shark. Game Over.")
        exit()
    else:
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n").lower()
        if choice3 == "red":
            print("You found the treasure! You win!")
        elif choice3 == "yellow":
            print("You found a room full of fire. You burned to death. Game Over.")
        elif choice3 == "blue":
            print("You enter a room full of beasts. You are eaten. Game Over.")
        else:
            print("You sought the void door that doesn't exist. Game Over.")
            exit()

else:
  print("You fell into a hole. It was pretty clearly there, you should have looked. Game Over.")
  exit()