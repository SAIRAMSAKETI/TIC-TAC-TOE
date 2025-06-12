import tkinter as tk
from tkinter import messagebox
import random


window = tk.Tk()
window.title("Tic Tac Toe - Play vs Robot")
window.geometry("400x500")
window.configure(bg="#f0f0f0")


board = [""] * 9
buttons = []
player_symbol = "X"
robot_symbol = "O"
game_over = False
player_score = 0
robot_score = 0


wins = [(0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)]

def update_scoreboard():
    player_score_label.config(text=f"Player (X): {player_score}")
    robot_score_label.config(text=f"Robot (O): {robot_score}")

def check_winner(symbol):
    for i, j, k in wins:
        if board[i] == board[j] == board[k] == symbol:
            return True
    return False

def is_draw():
    return all(cell != "" for cell in board)

def disable_all():
    for btn in buttons:
        btn.config(state="disabled")

def robot_move():
    global game_over, robot_score

    if game_over:
        return

    
    for symbol in [robot_symbol, player_symbol]:
        for i in range(9):
            if board[i] == "":
                board[i] = symbol
                if check_winner(symbol):
                    board[i] = robot_symbol
                    buttons[i].config(text=robot_symbol, fg="red")
                    if check_winner(robot_symbol):
                        messagebox.showinfo("Game Over", "Robot Wins!")
                        disable_all()
                        game_over = True
                        robot_score += 1
                        update_scoreboard()
                    elif is_draw():
                        messagebox.showinfo("Draw", "It's a draw!")
                        disable_all()
                        game_over = True
                    return
                board[i] = ""

    
    empty = [i for i in range(9) if board[i] == ""]
    if empty:
        idx = random.choice(empty)
        board[idx] = robot_symbol
        buttons[idx].config(text=robot_symbol, fg="red")
        if check_winner(robot_symbol):
            messagebox.showinfo("Game Over", "Robot Wins!")
            disable_all()
            game_over = True
            robot_score += 1
            update_scoreboard()
        elif is_draw():
            messagebox.showinfo("Draw", "It's a draw!")
            disable_all()
            game_over = True

def on_click(i):
    global game_over, player_score
    if board[i] == "" and not game_over:
        board[i] = player_symbol
        buttons[i].config(text=player_symbol, fg="blue")
        if check_winner(player_symbol):
            messagebox.showinfo("Congratulations", "You Win!")
            disable_all()
            game_over = True
            player_score += 1
            update_scoreboard()
        elif is_draw():
            messagebox.showinfo("Draw", "It's a draw!")
            disable_all()
            game_over = True
        else:
            robot_move()

def reset_game():
    global board, game_over
    board = [""] * 9
    game_over = False
    for btn in buttons:
        btn.config(text="", state="normal")


score_frame = tk.Frame(window, bg="#d0e6a5", pady=10)
score_frame.pack(fill="x")

player_score_label = tk.Label(score_frame, text="Player (X): 0", font=("Arial", 14), bg="#d0e6a5")
player_score_label.pack(side="left", padx=20)

robot_score_label = tk.Label(score_frame, text="Robot (O): 0", font=("Arial", 14), bg="#d0e6a5")
robot_score_label.pack(side="right", padx=20)


frame = tk.Frame(window)
frame.pack(pady=20)

for i in range(9):
    btn = tk.Button(frame, text="", width=6, height=3,
                    font=("Arial", 24), command=lambda i=i: on_click(i),
                    bg="#ffffff", relief="raised")
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)


reset_btn = tk.Button(window, text="Restart Game", command=reset_game,
                      font=("Arial", 14), bg="#4caf50", fg="white", padx=10, pady=5)
reset_btn.pack(pady=10)

window.mainloop()
