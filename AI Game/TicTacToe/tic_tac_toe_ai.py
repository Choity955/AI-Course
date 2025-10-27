import tkinter as tk
from tkinter import messagebox

PLAYER = "X"
AI = "O"
board = [" "] * 9
scores = {"player": 0, "ai": 0, "draw": 0}

def check_winner(b, mark):
    win_combos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[a]==b[b_]==b[c]==mark for a,b_,c in win_combos)

def is_draw(b):
    return " " not in b

def minimax(b, is_max):
    if check_winner(b, AI): return 1
    if check_winner(b, PLAYER): return -1
    if is_draw(b): return 0

    best = -999 if is_max else 999
    mark = AI if is_max else PLAYER

    for i in range(9):
        if b[i] == " ":
            b[i] = mark
            score = minimax(b, not is_max)
            b[i] = " "
            best = max(best, score) if is_max else min(best, score)
    return best

def ai_move():
    best_score, move = -999, None
    for i in range(9):
        if board[i] == " ":
            board[i] = AI
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score, move = score, i
    if move is not None:
        make_move(move, AI)

def make_move(index, mark):
    board[index] = mark
    buttons[index].config(text=mark, fg="red" if mark==PLAYER else "blue", state="disabled")

    if check_winner(board, mark):
        update_score("player" if mark==PLAYER else "ai")
        messagebox.showinfo("Game Over", f"{'You' if mark==PLAYER else 'AI'} win!")
        reset_board()
    elif is_draw(board):
        update_score("draw")
        messagebox.showinfo("Game Over", "It's a Draw!")
        reset_board()
    elif mark == PLAYER:
        ai_move()

def on_click(i):
    if board[i] == " ":
        make_move(i, PLAYER)

def reset_board():
    for i in range(9):
        board[i] = " "
        buttons[i].config(text=" ", state="normal")

def update_score(winner):
    scores[winner] += 1
    score_label.config(text=f"Player: {scores['player']}   AI: {scores['ai']}   Draw: {scores['draw']}")

root = tk.Tk()
root.title("Tic Tac Toe - AI vs You")

score_label = tk.Label(root, text="Player: 0   AI: 0   Draw: 0", font=("Arial", 14, "bold"))
score_label.grid(row=0, column=0, columnspan=3, pady=10)

buttons = [
    tk.Button(root, text=" ", font=("Arial", 20, "bold"), width=5, height=2, command=lambda i=i: on_click(i))
    for i in range(9)
]
for i, btn in enumerate(buttons):
    btn.grid(row=i//3+1, column=i%3)

tk.Button(root, text="Reset Board", font=("Arial", 14, "bold"), bg="lightgray", command=reset_board)\
    .grid(row=4, column=0, columnspan=3, sticky="nsew", pady=10)

root.mainloop()
