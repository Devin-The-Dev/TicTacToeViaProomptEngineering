import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def ai_move(board):
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_score = 0
    ai_score = 0

    while player_score < 3 and ai_score < 3:
        print(f"\nScore - Player: {player_score}, AI: {ai_score}")
        print_board(board)

        # Player's turn
        while True:
            try:
                row, col = map(int, input("Enter your move (row and column, 0-2): ").split())
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")

        if check_winner(board, "X"):
            print_board(board)
            print("You win this round!")
            player_score += 1
            board = [[" " for _ in range(3)] for _ in range(3)]
            continue

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            board = [[" " for _ in range(3)] for _ in range(3)]
            continue

        # AI's turn
        ai_row, ai_col = ai_move(board)
        board[ai_row][ai_col] = "O"

        if check_winner(board, "O"):
            print_board(board)
            print("AI wins this round!")
            ai_score += 1
            board = [[" " for _ in range(3)] for _ in range(3)]
            continue

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            board = [[" " for _ in range(3)] for _ in range(3)]

    print(f"\nFinal Score - Player: {player_score}, AI: {ai_score}")
    if player_score > ai_score:
        print("Congratulations! You won the game!")
    else:
        print("AI won the game. Better luck next time!")

if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!")
    print("You are 'X', and the AI is 'O'.")
    print("First to win 3 rounds wins the game.")
    play_game()
