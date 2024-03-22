# Write a program that tests the compatibility between two people.

print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")
name2 = input("What is their name?") 

# Combine the names and convert to lowercase
combined_names = name1 + name2
lower_names = combined_names.lower()

# Count the number of times the letters in the word TRUE occurs
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

# Count the number of times the letters in the word LOVE occurs
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

# Combine the two digits to form a two-digit number
score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
