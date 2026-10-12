import tkinter as tk
from chess_engine import ChessPieces

# variable
root = tk.Tk()
HEIGHT = WIDTH = 600
SQUARE_SIZE = HEIGHT // 8
light = "#f0d9b5"
dark = "#b58863"

# window setting
root.title("Chess")
root.geometry("600x600")
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# draw chessboard
for row in range (8):
    for col in range (8):
        x1 = row * SQUARE_SIZE
        y1 = col * SQUARE_SIZE
        x2 = x1 + SQUARE_SIZE
        y2 = y1 + SQUARE_SIZE

        color = light if (col + row) % 2 == 0 else dark
        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

# draw chess pieces
chess_pieces = ChessPieces(canvas, SQUARE_SIZE)
chess_pieces.draw_pieces()

root.mainloop()