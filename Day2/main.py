# Tip calculator and party split
# Generate a welcome
print("Welcome to the tip calculator and party split")

# Ask for amount spent on the bill
bill = input("How much was the bill? $")

# Ask for tip percentage
tip = input("What percentage would you like to tip? 10, 12, 15, 20? ")

# Ask for number of people splitting the bill
people = input("How many people are splitting the bill? ")

# Total the bill plus tip
tip_as_percent = int(tip) / 100
total_tip = float(bill) * tip_as_percent
total_bill = float(bill) + total_tip
bill_per_person = total_bill / int(people)
final_amount = round(bill_per_person, 2)




# Present the total bill plus tip divided by the number of people
print(f"Each person should pay: ${final_amount}")

