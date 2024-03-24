# Ceasar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Unified the encrypt and decrypt functions into one function called ceasar
# The function takes in the text, shift amount, and the direction (encode or decode)
def ceasar(start_text, shift_amount, cipher_direction):
    if cipher_direction != "encode" and cipher_direction != "decode": # Check if the user input is valid
        print("Invalid input. Please try again.")
        exit()
    end_text = "" # Initialize the end_text variable to store the final text
    for letter in start_text: # Loop through each letter in the start_text
        if letter in alphabet:
            position = alphabet.index(letter)
            if cipher_direction == "decode":
                new_position = (position - shift_amount) % len(alphabet)
            else:
                new_position = (position + shift_amount) % len(alphabet)
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is {end_text}")
    
# Import the logo from the art.py file
from art import logo
print(logo)

should_end = False # Initialize the should_end variable to False
while not should_end:
    # Ask the user for the direction (encode or decode)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # Ask the user for the text to be encrypted or decrypted
    text = input("Type your message:\n").lower()
    # Ask the user for the shift amount
    shift = int(input("Type the shift number:\n"))
    # Check if the shift amount is greater than the number of letters in the alphabet
    #shift = shift % 26
 
    # Call the ceasar_cipher function and pass in the user inputs
    ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
    