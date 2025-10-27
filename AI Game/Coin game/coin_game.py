import tkinter as tk
import math

# --- Game Logic (Minimax AI) ---
def minimax(remaining, is_ai):
    if remaining == 0:
        return -1 if is_ai else 1
    moves = [1, 2, 3]
    if is_ai:
        best = -math.inf
        for m in moves:
            if remaining - m >= 0:
                best = max(best, minimax(remaining - m, False))
        return best
    else:
        best = math.inf
        for m in moves:
            if remaining - m >= 0:
                best = min(best, minimax(remaining - m, True))
        return best

def ai_move(remaining):
    best_score = -math.inf
    move = 1
    for m in [1, 2, 3]:
        if remaining - m >= 0:
            score = minimax(remaining - m, False)
            if score > best_score:
                best_score = score
                move = m
    return move

# --- GUI Class ---
class CoinGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🪙 Coin Game: User vs AI")
        self.root.geometry("600x400")
        self.root.configure(bg="#2c2c2c")

        # --- Game variables ---
        self.coins = 15
        self.player_turn = True
        self.game_over = False
        self.message = "Your turn: Take 1, 2, or 3 coins"

        # --- Title label ---
        self.turn_label = tk.Label(
            root, text="Your Turn", font=("Arial", 22, "bold"),
            bg="#2c2c2c", fg="lime"
        )
        self.turn_label.pack(pady=10)

        # --- Coin display area ---
        self.canvas = tk.Canvas(root, width=560, height=120, bg="#2c2c2c", highlightthickness=0)
        self.canvas.pack(pady=10)

        # --- Message label ---
        self.msg_label = tk.Label(
            root, text=self.message, font=("Arial", 14),
            bg="#2c2c2c", fg="white"
        )
        self.msg_label.pack(pady=10)

        # --- Buttons for moves ---
        self.button_frame = tk.Frame(root, bg="#2c2c2c")
        self.button_frame.pack(pady=10)

        self.buttons = []
        for i, val in enumerate([1, 2, 3]):
            btn = tk.Button(
                self.button_frame, text=str(val), font=("Arial", 16, "bold"),
                bg="#3366cc", fg="white", width=5, height=1,
                command=lambda v=val: self.user_move(v)
            )
            btn.grid(row=0, column=i, padx=20)
            self.buttons.append(btn)

        # --- Restart button ---
        self.restart_btn = tk.Button(
            root, text="Restart (R)", font=("Arial", 12, "bold"),
            bg="#e67e22", fg="white", width=12, command=self.restart
        )
        self.restart_btn.pack(pady=10)

        # --- Keyboard shortcut for restart ---
        self.root.bind("r", lambda e: self.restart())

        # --- Initial draw ---
        self.draw_coins()

    # --- Draw coins on canvas ---
    def draw_coins(self):
        self.canvas.delete("all")
        x_start = 25
        for i in range(self.coins):
            x = x_start + i * 35
            y = 40
            self.canvas.create_oval(x, y, x + 25, y + 25, fill="gold", outline="white", width=2)
        if self.coins == 0:
            self.canvas.create_text(280, 60, text="No Coins Left!", fill="white", font=("Arial", 16, "bold"))

    # --- User Move ---
    def user_move(self, value):
        if not self.player_turn or self.game_over:
            return
        if self.coins - value < 0:
            return

        self.coins -= value
        self.draw_coins()

        if self.coins == 0:
            self.message = "You took the last coin. You lose!"
            self.msg_label.config(text=self.message)
            self.turn_label.config(text="Game Over", fg="red")
            self.game_over = True
            return

        self.player_turn = False
        self.message = f"You took {value}. AI's turn..."
        self.msg_label.config(text=self.message)
        self.turn_label.config(text="AI Turn", fg="red")

        self.root.after(800, self.ai_turn)

    # --- AI Move ---
    def ai_turn(self):
        if self.game_over:
            return

        move = ai_move(self.coins)
        self.coins -= move
        self.draw_coins()

        if self.coins == 0:
            self.message = f"AI took {move} and last coin. AI loses! You win!"
            self.msg_label.config(text=self.message)
            self.turn_label.config(text="🎉 You Win!", fg="lime")
            self.game_over = True
        else:
            self.player_turn = True
            self.message = f"AI took {move}. Your turn."
            self.msg_label.config(text=self.message)
            self.turn_label.config(text="Your Turn", fg="lime")

    # --- Restart game ---
    def restart(self):
        self.coins = 15
        self.player_turn = True
        self.game_over = False
        self.message = "Your turn: Take 1, 2, or 3 coins"
        self.msg_label.config(text=self.message)
        self.turn_label.config(text="Your Turn", fg="lime")
        self.draw_coins()


# --- Main Program ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CoinGame(root)
    root.mainloop()

