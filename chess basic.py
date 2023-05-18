import chess
import chess.svg

# Initialize the chess board
board = chess.Board()

# Function to make a move for the bot
def make_move():
    move = get_best_move()
    board.push(move)
    print("Bot's move:", move.uci())
    print(board)

# Function to get the best move for the bot (random move in this example)
def get_best_move():
    legal_moves = list(board.legal_moves)
    return legal_moves[0] if legal_moves else None

# Main game loop
while not board.is_game_over():
    if board.turn == chess.WHITE:
        # Human's move
        move = input("Enter your move (in algebraic notation): ")
        board.push_san(move)
        print(board)
    else:
        # Bot's move
        make_move()

# Print the game result
print("Game over. Result:",board.result())