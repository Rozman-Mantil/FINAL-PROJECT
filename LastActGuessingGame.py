import random

def number_guessing_game():
    # generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # initialize guess and number of attempts
    guess = None
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    
    while guess != secret_number:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("Please enter a number within the valid range of 1 to 100.")
                continue
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} correctly!")
                print(f"It took you {attempts} attempts to guess the number.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    print("Thanks for playing!")

# Run the game
number_guessing_game()
