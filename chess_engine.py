from chess_pieces import Piece

# ALL PIECES
# white pieces
white_rook = Piece(0, 0, "rook", "white")
white_knight = Piece(0, 1, "knight", "white")
white_bishop = Piece(0, 2, "bishop", "white")
white_queen = Piece(0, 3, "queen", "white")
white_king = Piece(0, 4, "king", "white")
white_bishop2 = Piece(0, 5, "bishop", "white")
white_knight2 = Piece(0, 6, "knight", "white")
white_rook2 = Piece(0, 7, "rook", "white")

# black pieces
black_rook = Piece(7, 0, "rook", "black")
black_knight = Piece(7, 1, "knight", "black")
black_bishop = Piece(7, 2, "bishop", "black")
black_queen = Piece(7, 3, "queen", "black")
black_king = Piece(7, 4, "king", "black")
black_bishop2 = Piece(7, 5, "bishop", "black")
black_knight2 = Piece(7, 6, "knight", "black")
black_rook2 = Piece(7, 7, "rook", "black")

# all pieces list
pieces = [
    white_rook, white_knight, white_bishop, white_queen, white_king, white_bishop2, white_knight2, white_rook2,
    black_rook, black_knight, black_bishop, black_queen, black_king, black_bishop2, black_knight2, black_rook2
]

# all chess pieces drawn on the board
class ChessPieces():
    def __init__(self, canvas, square_size):
        self.canvas = canvas
        self.square_size = square_size

    def draw_pieces(self):
        for col in range(8):
            # draw white pawns
            white_pawn = Piece(1, col, "pawn", "white")
            white_pawn.draw(self.canvas, self.square_size)

            # draw black pawns
            black_pawn = Piece(6, col, "pawn", "black")
            black_pawn.draw(self.canvas, self.square_size)


        # draw pieces
        for piece in pieces:
            piece.draw(self.canvas, self.square_size)

