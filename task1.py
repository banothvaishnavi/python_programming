import random

def print_board(board):
    """Print the Tic Tac Toe board."""
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Check if the player has won."""
    # Check rows, columns, and diagonals
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    """Check if the game is a draw."""
    return all(cell != ' ' for row in board for cell in row)

def get_player_move(board):
    """Get the player's move."""
    while True:
        try:
            row = int(input("Enter the row (1, 2, or 3): ")) - 1
            col = int(input("Enter the column (1, 2, or 3): ")) - 1
            if board[row][col] == ' ':
                return row, col
            else:
                print("That cell is already taken. Try again.")
        except (IndexError, ValueError):
            print("Invalid input. Enter numbers between 1 and 3.")

def get_computer_move(board):
    """Get the computer's move."""
    empty_cells = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    return random.choice(empty_cells)

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_mode = input("Choose game mode - Player vs Player (1) or Player vs Computer (2): ")
    
    print_board(board)
    
    while True:
        if game_mode == '2' and current_player == 'O':
            row, col = get_computer_move(board)
            print(f"Computer chose: row {row+1}, column {col+1}")
        else:
            print(f"Player {current_player}'s turn")
            row, col = get_player_move(board)
        
        board[row][col] = current_player
        print_board(board)
        
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        
        if check_draw(board):
            print("The game is a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

play_game()