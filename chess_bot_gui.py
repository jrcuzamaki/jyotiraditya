import chess
import chess.svg
import chess.engine
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout


# Chess GUI widget
class ChessWidget(QWidget):
    def _init_(self):
        super()._init_()

        # Initialize the chess board
        self.board = chess.Board()

        # Load the chess engine
        self.engine = chess.engine.SimpleEngine.popen_uci("path_to_stockfish_engine")

        # Create a SVG widget to display the chessboard
        self.svg_widget = QSvgWidget(self)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.svg_widget)
        self.setLayout(layout)

        # Update the chessboard display
        self.update_board()

    def update_board(self):
        # Generate the SVG representation of the chessboard
        svg = chess.svg.board(board=self.board)

        # Load the SVG into the widget
        self.svg_widget.load(svg.encode("utf-8"))

    def mousePressEvent(self, event):
        # Get the square from the mouse click position
        square_size = self.svg_widget.width() // 8
        file_idx = event.x() // square_size
        rank_idx = 7 - event.y() // square_size
        square = chess.square(file_idx, rank_idx)

        # Get the list of legal moves
        legal_moves = list(self.board.legal_moves)

        # Check if the clicked square is a valid move
        move = next((move for move in legal_moves if move.from_square == square), None)

        # If the move is valid, make it
        if move:
            self.board.push(move)
            self.update_board()

            # Check for game over
            if self.board.is_game_over():
                print("Game over. Result:", self.board.result())
                self.engine.quit()
                app.quit()

            # Bot's turn
            self.make_move()

    def make_move(self):
        result = self.engine.play(self.board, chess.engine.Limit(time=2.0))
        move = result.move
        self.board.push(move)
        self.update_board()

        # Check for game over
        if self.board.is_game_over():
            print("Game over. Result:", self.board.result())
            self.engine.quit()
            app.quit()


if  __name__ == "_main_":
    # Create the application
    app = QApplication(sys.argv)

    # Create the chess widget
    widget = ChessWidget()
    widget.show()

    # Execute the application
    sys.exit(app.exec_())