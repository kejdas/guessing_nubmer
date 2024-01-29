import random

def guess_number():
    # Generate a random number between 0 and 100
    r_number = random.randint(0, 100)
    print("Hi, just try to guess the number between 0 - 100")

    # Initialize variables
    playing = True
    counter = 0

    # Main game loop
    while playing:
        # Get user input for their guess
        user_number = int(input())

        # Check if the user's guess is correct
        if user_number == r_number:
            counter += 1
            # Provide feedback on the number of moves taken to guess correctly
            if counter == 1:
                print(f"Congratulations! You win in {counter} move! That's incredible.")
            else:
                print(f"Congratulations! You win in {counter} moves.")
            playing = False
        # Provide hints for incorrect guesses
        elif user_number < r_number:
            print("Sheesh bro, try a bigger number.")
            counter += 1
        elif user_number > r_number:
            print("Hold on, man! You are going in the wrong way. The number is too big.")
            counter += 1

# Call the guess_number function to run the game
guess_number()
