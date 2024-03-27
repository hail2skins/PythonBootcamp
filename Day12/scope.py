# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
    
# increase_enemies()
# print(f"enemies outside function: {enemies}")

# #global scope
# player_health = 10 #available everywhere

# # Local scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength + player_health)
    
# drink_potion() # 2, from local scope inside the function, 10 from global scope

# There is no block scope
game_level = 3

enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]