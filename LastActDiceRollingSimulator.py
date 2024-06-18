import random

def roll_dice():
    return random.randint(1, 6)  # returns a random number between 1 and 6

def main():
    print("Welcome to the Dice Rolling Game!")
    print("Each player will roll a dice. The player who wins 2 out of 3 rounds wins the game.")

    player1_wins = 0
    player2_wins = 0
    rounds_to_win = 2
    round_number = 1

    while player1_wins < rounds_to_win and player2_wins < rounds_to_win:
        print(f"\nRound {round_number}:")
        print("Player 1's turn to roll the dice.")
        input("Press Enter to roll...")
        player1_roll = roll_dice()
        print(f"Player 1 rolled: {player1_roll}")

        print("\nPlayer 2's turn to roll the dice.")
        input("Press Enter to roll...")
        player2_roll = roll_dice()
        print(f"Player 2 rolled: {player2_roll}")

        if player1_roll > player2_roll:
            print("Player 1 wins this round!")
            player1_wins += 1
        elif player2_roll > player1_roll:
            print("Player 2 wins this round!")
            player2_wins += 1
        else:
            print("It's a tie for this round!")

        round_number += 1

    # Determine the overall winner
    if player1_wins > player2_wins:
        print("\nPlayer 1 wins the game!")
    else:
        print("\nPlayer 2 wins the game!")

if __name__ == "__main__":
    main()

