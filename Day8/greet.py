# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello")
    print("Welcome")
    print("Good Morning")
    
greet()

# Function with input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Welcome {name}")
    print("Good Morning", name)
    
greet_with_name("Art")

# Function with more than one input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"Welcome {name}")
    print(f"Good Morning {name} from {location}")
    
greet_with("Art", "Washington D.C.")

#function with keyword arguments
greet_with(location="Washington D.C.", name="Art")
