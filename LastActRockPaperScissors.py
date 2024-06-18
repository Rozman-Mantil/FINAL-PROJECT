#1
import random

#2
def rock_paper_scissors():
    # Define the game options
    options = ['rock', 'paper', 'scissors']
    
    # Initialize scores
    player_score = 0
    computer_score = 0
    
    print("Welcome to Rock-Paper-Scissors!")
    print("You will play against the computer. The first to win 2 rounds wins the game.")
    
    while player_score < 2 and computer_score < 2:
        print("\nChoose your move: rock, paper, or scissors")
        player_choice = input("Your choice: ").lower()
        
        # Validate user input
        while player_choice not in options:
            print("Invalid choice. Please enter rock, paper, or scissors.")
            player_choice = input("Your choice: ").lower()
        
        # Computer makes a random choice
        computer_choice = random.choice(options)
        
        # Determine winner for this round
        if player_choice == computer_choice:
            print(f"Both chose {player_choice}. It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print(f"You chose {player_choice} and computer chose {computer_choice}. You win this round!")
            player_score += 1
        else:
            print(f"You chose {player_choice} and computer chose {computer_choice}. Computer wins this round!")
            computer_score += 1
        
        # Display current score
        print(f"Score - You: {player_score}, Computer: {computer_score}")
    
    # Determine the overall winner
    if player_score > computer_score:
        print("Congratulations! You won the game!")
    else:
        print("Sorry, the computer won the game. Better luck next time!")

# Run the game
rock_paper_scissors()
