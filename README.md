# TicTacToe Via Prompt Engineering

This document provides a detailed explanation of a simple Tic Tac Toe game implemented in Python. This code demonstrates fundamental programming concepts such as functions, loops, conditional statements, list manipulation, and basic game logic.

## Step-by-Step Explanation

1.  **Import `random`:**

    ```python
    import random
    ```

    This line imports the `random` module, which will be used by the AI to make random moves.

2.  **`print_board(board)` Function:**

    ```python
    def print_board(board):
        """Prints the Tic Tac Toe board to the console."""
        for row in board:
            print(" | ".join(row))
            print("-" * 9)
    ```

    This function takes the current state of the `board` (a list of lists representing the 3x3 grid) as input. It iterates through each `row` and prints the cells joined by " | ". After each row, it prints a separator line "---------". This provides a visual representation of the Tic Tac Toe board in the console.

3.  **`check_winner(board, player)` Function:**

    ```python
    def check_winner(board, player):
        """Checks if the given player has won the game."""
        # Check rows
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):
                return True
        # Check columns
        for i in range(3):
            if all(board[j][i] == player for j in range(3)):
                return True
        # Check diagonals
        if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
            return True
        return False
    ```

    This function determines if a given `player` ('X' or 'O') has won the current round. It checks all possible winning conditions:

      * **Rows:** It iterates through each row and checks if all cells in that row are occupied by the `player`.
      * **Columns:** It iterates through each column and checks if all cells in that column are occupied by the `player`.
      * **Diagonals:** It checks both main diagonals to see if all cells are occupied by the `player`.
        If any of these conditions are met, the function returns `True`; otherwise, it returns `False`.

4.  **`is_board_full(board)` Function:**

    ```python
    def is_board_full(board):
        """Checks if all cells on the board are filled."""
        return all(cell != " " for row in board for cell in row)
    ```

    This function checks if the `board` is completely full. It uses a generator expression `(cell != " " for row in board for cell in row)` to iterate through all cells and checks if any cell is still empty (" "). The `all()` function returns `True` if all cells are not empty, and `False` otherwise.

5.  **`get_empty_cells(board)` Function:**

    ```python
    def get_empty_cells(board):
        """Returns a list of coordinates (row, column) of all empty cells."""
        return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    ```

    This function identifies and returns a list of coordinates (row, column) for all empty cells (" ") on the `board`. It uses a list comprehension to efficiently create this list.

6.  **`ai_move(board)` Function:**

    ```python
    def ai_move(board):
        """Determines a random valid move for the AI player."""
        empty_cells = get_empty_cells(board)
        return random.choice(empty_cells)
    ```

    This function determines the AI's move. It first gets a list of all `empty_cells` using the `get_empty_cells()` function. Then, it uses `random.choice()` to select a random coordinate from the list of empty cells. This represents a simple AI that makes purely random valid moves.

7.  **`play_game()` Function:**

    ```python
    def play_game():
        """The main function that controls the game flow."""
        board = [[" " for _ in range(3)] for _ in range(3)]
        player_score = 0
        ai_score = 0

        # Play rounds until one player reaches a score of 3
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

            # Check if player wins the round
            if check_winner(board, "X"):
                print_board(board)
                print("You win this round!")
                player_score += 1
                board = [[" " for _ in range(3)] for _ in range(3)] # Reset the board
                continue

            # Check if the round is a tie
            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                board = [[" " for _ in range(3)] for _ in range(3)] # Reset the board
                continue

            # AI's turn
            ai_row, ai_col = ai_move(board)
            board[ai_row][ai_col] = "O"

            # Check if AI wins the round
            if check_winner(board, "O"):
                print_board(board)
                print("AI wins this round!")
                ai_score += 1
                board = [[" " for _ in range(3)] for _ in range(3)] # Reset the board
                continue

            # Check if the round is a tie after AI's move
            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                board = [[" " for _ in range(3)] for _ in range(3)] # Reset the board

        # Determine the overall winner of the game
        print(f"\nFinal Score - Player: {player_score}, AI: {ai_score}")
        if player_score > ai_score:
            print("Congratulations! You won the game!")
        else:
            print("AI won the game. Better luck next time!")
    ```

    This is the main function that orchestrates the Tic Tac Toe game.

      * It initializes an empty `board`, `player_score`, and `ai_score`.
      * It enters a `while` loop that continues until either the player or the AI reaches a score of 3. This implements a "best out of five rounds" format.
      * Inside the loop, it prints the current `score` and the `board`.
      * **Player's Turn:** It enters another `while True` loop to handle the player's input until a valid move is entered.
          * It prompts the player to enter their move as row and column numbers (0-2).
          * It uses a `try-except` block to handle potential `ValueError` if the player enters non-numeric input.
          * It checks if the entered row and column are within the valid range and if the chosen cell is empty.
          * If the move is valid, it places 'X' on the board and breaks out of the inner loop.
          * If the move is invalid, it prints an error message.
      * After the player's move, it checks if the player has won the round using `check_winner()`. If so, it prints the board and a winning message, increments the `player_score`, and resets the `board` for the next round using `continue`.
      * It then checks if the round is a tie using `is_board_full()`. If so, it prints the board and a tie message, and resets the `board`.
      * **AI's Turn:** If the player hasn't won or tied, the AI makes a move using `ai_move()`, and 'O' is placed on the board.
      * It then checks if the AI has won the round and if the round is a tie after the AI's move, similar to the player's turn.
      * Once one player reaches a score of 3, the outer `while` loop terminates.
      * Finally, it prints the `final score` and declares the overall winner of the game.

8.  **`if __name__ == "__main__":` Block:**

    ```python
    if __name__ == "__main__":
        print("Welcome to Tic Tac Toe!")
        print("You are 'X', and the AI is 'O'.")
        print("First to win 3 rounds wins the game.")
        play_game()
    ```

    This is a standard Python construct that ensures the code inside this block only runs when the script is executed directly (not when it's imported as a module). It prints a welcome message and instructions to the player before calling the `play_game()` function to start the game.

This detailed explanation should provide a clear understanding of the Python code and its logic, which is crucial for your career development. Understanding how to break down code into functions, handle user input, implement game rules, and control the flow of execution are fundamental programming skills.
