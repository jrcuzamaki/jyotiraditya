import chess
import chess.engine

# Initialize the chess board
board = chess.Board()

# Load the chess engine
engine = chess.engine.SimpleEngine.popen_uci("C:/Program Files/Stockfish/stockfish.exe")
# Function to make a move using the chess engine
def make_move():
    result = engine.play(board, chess.engine.Limit(time=2.0))
    move = result.move
    board.push(move)
    print("Bot's move:", move.uci())
    print(board)

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

# Close the chess engine
engine.quit()