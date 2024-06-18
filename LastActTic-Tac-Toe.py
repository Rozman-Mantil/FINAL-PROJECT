def print_board(board):
    """Prints the Tic-tac-toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    """Check if the player has won the game."""
    for row in board:
        if all([cell == player for cell in row]):
            return True
    
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    
    return False

def is_board_full(board):
    """Check if the board is full."""
    return all([cell != ' ' for row in board for cell in row])

def get_player_move(player_name, board):
    """Get valid move from the player."""
    while True:
        try:
            move = input(f"{player_name}, enter your move (row column): ")
            row, col = map(int, move.split())
            if row < 0 or row > 2 or col < 0 or col > 2:
                raise ValueError("Invalid input. Row and column must be between 0 and 2.")
            if board[row][col] != ' ':
                raise ValueError("That position is already taken. Choose another.")
            return row, col
        except ValueError as ve:
            print(ve)
            continue

def main():
    print("Welcome to Tic-tac-toe!")

    # Initialize players
    player1_name = input("Enter name of Player 1 (X): ")
    player2_name = input("Enter name of Player 2 (O): ")
    players = [player1_name, player2_name]
    symbols = ['X', 'O']

    # Initialize board
    board = [[' ' for _ in range(3)] for _ in range(3)]

    current_player = 0  # Index to keep track of current player

    # Game loop
    while True:
        print_board(board)
        player_name = players[current_player]
        player_symbol = symbols[current_player]
        
        # Get player move
        row, col = get_player_move(player_name, board)
        
        # Make the move
        board[row][col] = player_symbol
        
        # Check for win
        if check_win(board, player_symbol):
            print_board(board)
            print(f"Congratulations! {player_name} ({player_symbol}) wins!")
            break
        
        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = 1 - current_player

if __name__ == "__main__":
    main()
