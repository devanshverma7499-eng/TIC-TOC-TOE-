
# Tic-Tac-Toe AI using Minimax

HUMAN = "X"
AI = "O"
EMPTY = " "


def display_board(board):
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i:i + 3]))
        if i < 6:
            print("---+---+---")
    print()


def get_winner(board):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] != EMPTY:
            return board[a]

    return None


def minimax(board, is_ai_turn):
    winner = get_winner(board)

    if winner == AI:
        return 1
    if winner == HUMAN:
        return -1
    if EMPTY not in board:
        return 0

    if is_ai_turn:
        best_score = float("-inf")

        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                score = minimax(board, False)
                board[i] = EMPTY
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")

        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                score = minimax(board, True)
                board[i] = EMPTY
                best_score = min(best_score, score)

        return best_score


def ai_move(board):
    best_score = float("-inf")
    move = None

    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            score = minimax(board, False)
            board[i] = EMPTY

            if score > best_score:
                best_score = score
                move = i

    return move


def play_game():
    board = [EMPTY] * 9

    print("===== TIC-TAC-TOE AI =====")
    print("You are X | Computer is O")
    print("Choose positions from 1 to 9.")

    while True:
        display_board([
            str(i + 1) if cell == EMPTY else cell
            for i, cell in enumerate(board)
        ])

        try:
            position = int(input("Your move (1-9): ")) - 1
        except ValueError:
            print("Enter a valid number!")
            continue

        if position not in range(9) or board[position] != EMPTY:
            print("Invalid or occupied position!")
            continue

        board[position] = HUMAN

        if get_winner(board) == HUMAN:
            display_board(board)
            print("Congratulations! You won!")
            break

        if EMPTY not in board:
            display_board(board)
            print("It's a draw!")
            break

        move = ai_move(board)
        board[move] = AI
        print("Computer chooses position:", move + 1)

        if get_winner(board) == AI:
            display_board(board)
            print("Computer wins!")
            break

        if EMPTY not in board:
            display_board(board)
            print("It's a draw!")
            break


play_game()
