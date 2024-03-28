# Quick program to make a repeating folder structure for a project

# Importing the os module
import os

# Function to create a folder structure
def create_folders():
    # Assuming you are in the project directory
    # Create a folder with the following format for each day within a range provided by the user
    for day in range(1, 101):
        # Name a folder with the day number
        folder_name = f"Day{day}"
        # If folder already exists in the directory, print a message. Otherwise, create the folder
        if os.path.exists(folder_name):
            print(f"Folder Day{day} already exists")
        else:
            os.makedirs(folder_name)
            print(f"Folder Day{day} created")
            
# Call the function
create_folders()
        