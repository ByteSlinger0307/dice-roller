import random  # Import the random module to generate random numbers

# Start an infinite loop
while True:
    # Generate a random integer between 1 and 6 (inclusive) to simulate a dice roll
    dice_number = random.randint(1, 6)
    
    # Print the result of the dice roll
    print(f"The dice number is: {dice_number}")
    
    # Prompt the user to decide whether they want to roll the dice again
    roll_again = input("Do you want to roll the dice again? (Y/N): ")
    
    # Check if the user's response is 'Y' (case-insensitive)
    if roll_again.lower() == "y":
        # If 'Y', continue the loop to roll the dice again
        continue
    else:
        # If the response is anything other than 'Y', break out of the loop
        break

# End of the program