# Unicode hex symbols for each piece type and color
SYMBOLS = {
    "white": {
        "king": "\u2654", "queen": "\u2655", "rook": "\u2656",
        "bishop": "\u2657", "knight": "\u2658", "pawn": "\u2659"
    },
    "black": {
        "king": "\u265A", "queen": "\u265B", "rook": "\u265C",
        "bishop": "\u265D", "knight": "\u265E", "pawn": "\u265F"
    }
}

# piece class
class Piece():
    def __init__(self, row, col, piece_name, color):
        self.row = row
        self.col =  col
        self.color = color
        self.piece_name = piece_name
        self.symbol = SYMBOLS[color][piece_name]

    # draw the pieces in right place
    def draw(self, canvas, sq_size):
        x = self.col * sq_size + sq_size / 2
        y = self.row * sq_size + sq_size / 2
        canvas.create_text(x, y, text=self.symbol, font=("Arial", 48))