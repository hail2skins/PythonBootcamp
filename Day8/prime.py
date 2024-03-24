# Write your code below this line 👇

def prime_checker(number):
  # Setting all numbers as prime until proven otherwise
  is_prime = True
  # Checking if the number is divisible by any number between 2 and the number itself
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

n = int(input("Check this number")) # Check this number
prime_checker(number=n)