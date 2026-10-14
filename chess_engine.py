import tkinter as tk

# all variables
root = tk.Tk()
HEIGHT = WIDTH = 600
SQUARE_SIZE = HEIGHT // 8

root.title("Chess")
root.geometry("600x600")

canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# selected piece
selected_piece = None
# current turn color
current_turn = "white"


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

# ALL PIECES VARIABLES
# white pieces
white_rook = Piece(0, 0, "rook", "white")
white_knight = Piece(0, 1, "knight", "white")
white_bishop = Piece(0, 2, "bishop", "white")
white_queen = Piece(0, 3, "queen", "white")
white_king = Piece(0, 4, "king", "white")
white_bishop2 = Piece(0, 5, "bishop", "white")
white_knight2 = Piece(0, 6, "knight", "white")
white_rook2 = Piece(0, 7, "rook", "white")
white_pawn1 = Piece(1, 0, "pawn", "white")
white_pawn2 = Piece(1, 1, "pawn", "white")
white_pawn3 = Piece(1, 2, "pawn", "white")
white_pawn4 = Piece(1, 3, "pawn", "white")
white_pawn5 = Piece(1, 4, "pawn", "white")
white_pawn6 = Piece(1, 5, "pawn", "white")
white_pawn7 = Piece(1, 6, "pawn", "white")
white_pawn8 = Piece(1, 7, "pawn", "white")

# black pieces
black_rook = Piece(7, 0, "rook", "black")
black_knight = Piece(7, 1, "knight", "black")
black_bishop = Piece(7, 2, "bishop", "black")
black_queen = Piece(7, 3, "queen", "black")
black_king = Piece(7, 4, "king", "black")
black_bishop2 = Piece(7, 5, "bishop", "black")
black_knight2 = Piece(7, 6, "knight", "black")
black_rook2 = Piece(7, 7, "rook", "black")
black_pawn1 = Piece(6, 0, "pawn", "black")
black_pawn2 = Piece(6, 1, "pawn", "black")
black_pawn3 = Piece(6, 2, "pawn", "black")
black_pawn4 = Piece(6, 3, "pawn", "black")
black_pawn5 = Piece(6, 4, "pawn", "black")
black_pawn6 = Piece(6, 5, "pawn", "black")
black_pawn7 = Piece(6, 6, "pawn", "black")
black_pawn8 = Piece(6, 7, "pawn", "black")

# all pieces list
pieces = [
    white_rook, white_knight, white_bishop, white_queen, white_king, white_bishop2, white_knight2, white_rook2,
    black_rook, black_knight, black_bishop, black_queen, black_king, black_bishop2, black_knight2, black_rook2,
    white_pawn1, white_pawn2, white_pawn3, white_pawn4, white_pawn5, white_pawn6, white_pawn7, white_pawn8,
    black_pawn1, black_pawn2, black_pawn3, black_pawn4, black_pawn5, black_pawn6, black_pawn7, black_pawn8
]

# all chess pieces drawn on the board
class ChessPieces():
    def __init__(self, canvas, square_size):
        self.canvas = canvas
        self.square_size = square_size

    def draw_pieces(self):
        # draw pieces
        for piece in pieces:
            piece.draw(self.canvas, self.square_size)


# draw chessboard
def draw_board(canvas, square_size):
    light = "#EBECD0"
    dark = "#739552"

    for row in range(8):
        for col in range(8):
            x1 = row * square_size
            y1 = col * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size

            color = light if (col + row) % 2 == 0 else dark
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")


# get piece
def get_piece_at(row, col):
    for piece in pieces:
        if piece.row == row and piece.col == col:
            return piece
    return None


# rook move validation
def rook_move_valid(from_row, from_col, to_row, to_col):
    if from_row != to_row and from_col != to_col:
        return False
    
    if from_row == to_row and from_col == to_col:
        return False

    # Horizontal move (same row, different column)
    if from_row == to_row and from_col != to_col:
        start_row = min(from_col, to_col) + 1
        end_row = max(from_col, to_col) - 1
        # check if there any piece in the middle of the way
        for col in range(start_row, end_row):
            if get_piece_at(from_row, col) is not None:
                return False
        return True

    # Vertical move (different row, same column)
    elif from_row != to_row and from_col == to_col:
        start_col = min(from_row, to_row) + 1
        end_col = max(from_row, to_row) - 1
        # check if there any piece in the middle of the way
        for row in range(start_col, end_col):
            if get_piece_at(row, from_col) is not None:
                return False
        return True


# Knight Move Validation
def knight_move_valid(from_row, from_col, to_row, to_col):
    if from_row == to_row and from_col == to_col:
        return False
    
    row_diff = abs(from_row - to_row)
    col_diff = abs(from_col - to_col)

    if (row_diff == 2 and col_diff == 1):
        return True
    elif (row_diff == 1 and col_diff == 2):
        return True
    else:
        return False


# Bishop Move Validation
def bishop_move_valid(from_row, from_col, to_row, to_col):
    if from_row == to_row and from_col == to_col:
        return False
    
    row_diff = abs(from_row - to_row)
    col_diff = abs(from_col - to_col)
    # row and col step calculation
    row_step = 1 if to_row > from_row else -1
    col_step = 1 if to_col > from_col else -1

    if row_diff == col_diff and row_diff > 0:
        for i in range(1, row_diff):
            check_row = from_row + i * row_step
            check_col = from_col + i * col_step

            if get_piece_at(check_row, check_col) is not None:
                return False

        return True


# Queen Move Validation
def queen_move_valid(from_row, from_col, to_row, to_col):
    return rook_move_valid(from_row, from_col, to_row, to_col) or bishop_move_valid(from_row, from_col, to_row, to_col)


# king move validation
def king_move_valid(from_row, from_col, to_row, to_col, color=None):
    if from_row == to_row and from_col == to_col:
        return False

    row_diff = abs(from_row - to_row)
    col_diff = abs(from_col - to_col)

    if row_diff > 1 or col_diff > 1:
        return False

    target_piece = get_piece_at(to_row, to_col)
    if target_piece is not None and color is not None and target_piece.color == color:
        return False

    return True


# pawn move validation
def pawn_move_valid(from_row, from_col, to_row, to_col, color):
    if from_row == to_row and from_col == to_col:
        return False

    if color == "white":
        direction = 1
        start_row = 1
    elif color == "black":
        direction = -1
        start_row = 6
    else:
        return False

    row_diff = to_row - from_row
    col_diff = abs(to_col - from_col)

    if from_col == to_col:
        if row_diff == direction and get_piece_at(to_row, to_col) is None:
            return True

        if from_row == start_row and row_diff == 2 * direction:
            if get_piece_at(from_row + direction, from_col) is not None:
                return False
            if get_piece_at(to_row, to_col) is not None:
                return False
            return True

        return False

    if col_diff == 1 and row_diff == direction:
        target_piece = get_piece_at(to_row, to_col)
        if target_piece is not None and target_piece.color != color:
            return True

    return False


def is_valid_move(piece, to_row, to_col):
    if piece is None:
        return False

    from_row = piece.row
    from_col = piece.col

    if piece.piece_name == "rook":
        return rook_move_valid(from_row, from_col, to_row, to_col)
    if piece.piece_name == "knight":
        return knight_move_valid(from_row, from_col, to_row, to_col)
    if piece.piece_name == "bishop":
        return bishop_move_valid(from_row, from_col, to_row, to_col)
    if piece.piece_name == "queen":
        return queen_move_valid(from_row, from_col, to_row, to_col)
    if piece.piece_name == "king":
        return king_move_valid(from_row, from_col, to_row, to_col, piece.color)
    if piece.piece_name == "pawn":
        return pawn_move_valid(from_row, from_col, to_row, to_col, piece.color)

    return False

# handle mouse click event
def on_click(event, canvas, square_size):
    global selected_piece, current_turn

    col = event.x // square_size
    row = event.y // square_size

    # First click: Pick up a piece
    if selected_piece is None:
        clicked_piece = get_piece_at(row, col)

        if clicked_piece is None:
            print(f"No piece at ({row}, {col})")
            return
        
        # first turn check and switch turn
        if clicked_piece.color != current_turn:
            print(f"It's {current_turn} move")
            return

        selected_piece = clicked_piece
        print(f"Selected: {selected_piece.piece_name} at ({row}, {col})")


    # Second click: Move the selected piece to the new square
    else:
        # target pieces
        target_piece = get_piece_at(row, col)

        # check if there already a piece exist
        if target_piece is not None and target_piece.color == selected_piece.color:
            selected_piece = target_piece
            print(f"Your piece selection is changed to {row,col}.")
            return

        if not is_valid_move(selected_piece, row, col):
            print(f"Invalid {selected_piece.piece_name} move.")
            return

        # Capture opponent piece if present
        if target_piece is not None:
            print(
                f"Captured: {target_piece.color} {target_piece.piece_name} by {selected_piece.color} {selected_piece.piece_name}"
            )
            pieces.remove(target_piece)

        # Update position
        print(f"Moving {selected_piece.piece_name} to ({row}, {col})")
        selected_piece.row = row
        selected_piece.col = col

        # Switch turns, clear selection, and redraw
        current_turn = "black" if current_turn == "white" else "white"
        selected_piece = None

        canvas.delete("all")
        draw_board(canvas, square_size)
        chess_pieces = ChessPieces(canvas, square_size)
        chess_pieces.draw_pieces()


def main():
    # draw board on screen
    draw_board(canvas, SQUARE_SIZE)

    # on click function
    canvas.bind("<Button-1>", lambda event: on_click(event, canvas, SQUARE_SIZE))

    # draw all pieces in the board
    chess_pieces = ChessPieces(canvas, SQUARE_SIZE)
    chess_pieces.draw_pieces()

    root.mainloop()

main()