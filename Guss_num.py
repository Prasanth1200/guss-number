import random

# Function to start the guessing game
def start_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts_left = 10  # Limit the number of attempts
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {attempts_left} attempts to guess the number.")

    # Game loop
    while attempts_left > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guessed the correct number!")
            break
        
        attempts_left -= 1
        print(f"You have {attempts_left} attempts left.")
        
    if attempts_left == 0:
        print(f"Sorry, you've run out of attempts. The correct number was {number_to_guess}.")

# Main program starts here
start_game()
