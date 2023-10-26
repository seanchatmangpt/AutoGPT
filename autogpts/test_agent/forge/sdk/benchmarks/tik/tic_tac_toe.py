# and passes all the tests.

def tic_tac_toe():
    """
    This function runs a Tic-Tac-Toe game through command lines.
    It prompts players for their moves and checks for a winner or a draw.
    It returns one of the following strings when the game is over:
    "Player 1 won!"
    "Player 2 won!"
    "Draw"
    """
    # Initialize the game board as a 3x3 grid with empty squares
    game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    # Keep track of the current player
    current_player = 1

    # Keep track of the number of moves made
    moves = 0

    # Keep playing until there is a winner or a draw
    while True:
        # Prompt the current player for their move
        move = input("Player " + str(current_player) + ", enter your move in the format 'x,y': ")

        # Check if the input is valid
        if len(move) != 3 or move[1] != ",":
            print("Invalid input. Please try again.")
            continue

        # Convert the input into coordinates
        x = int(move[0])
        y = int(move[2])

        # Check if the coordinates are within the game board
        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Invalid input. Please try again.")
            continue

        # Check if the square is already filled
        if game_board[x][y] != " ":
            print("That square is already filled. Please try again.")
            continue

        # Place the current player's number in the chosen square
        game_board[x][y] = str(current_player)

        # Print the updated game board
        print("   0  1  2")
        print("0: " + game_board[0][0] + " | " + game_board[0][1] + " | " + game_board[0][2])
        print("  -----------")
        print("1: " + game_board[1][0] + " | " + game_board[1][1] + " | " + game_board[1][2])
        print("  -----------")
        print("2: " + game_board[2][0] + " | " + game_board[2][1] + " | " + game_board[2][2])

        # Check for a winner
        if (game_board[0][0] == game_board[0][1] == game_board[0][2] != " ") or \
                (game_board[1][0] == game_board[1][1] == game_board[1][2] != " ") or \
                (game_board[2][0] == game_board[2][1] == game_board[2][2] != " ") or \
                (game_board[0][0] == game_board[1][0] == game_board[2][0] != " ") or \
                (game_board[0][1] == game_board[1][1] == game_board[2][1] != " ") or \
                (game_board[0][2] == game_board[1][2] == game_board[2][2] != " ") or \
                (game_board[0][0] == game_board[1][1] == game_board[2][2] != " ") or \
                (game_board[0][2] == game_board[1][1] == game_board[2][0] != " "):
            # Print the winner and end the game
            print("Player " + str(current_player) + " won!")
            return "Player " + str(current_player) + " won!"

        # Check for a draw
        if moves == 8:
            # Print the draw and end the game
            print("Draw")
            return "Draw"

        # Switch to the other player and increment the number of moves
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1
        moves += 1

# Run the game
tic_tac_toe()