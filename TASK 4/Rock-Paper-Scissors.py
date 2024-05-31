import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "User"
    else:
        return "Computer"

def play(user_choice):
    global user_score, computer_score
    
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    
    winner = determine_winner(user_choice, computer_choice)
    
    if winner == "User":
        user_score += 1
    elif winner == "Computer":
        computer_score += 1
    elif winner == "Draw":
        user_score += 1
        computer_score += 1
    
    user_choice_label.config(text=f"You: {user_choice}")
    computer_choice_label.config(text=f"Computer: {computer_choice}")
    result_label.config(text=f"Result: {winner}")
    user_score_label.config(text=f"User: {user_score}")
    computer_score_label.config(text=f"Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_score_label.config(text="User: 0")
    computer_score_label.config(text="Computer: 0")
    result_label.config(text="")
    user_choice_label.config(text="You: ")
    computer_choice_label.config(text="Computer: ")

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("540x300")
root.configure(bg="#2e2e2e")
center_window(root, 540, 300)

user_score = 0
computer_score = 0

user_choice_label = tk.Label(root, text="You: ", font=("Arial", 14), width=15, anchor='w', bg="#2e2e2e", fg="white")
user_choice_label.grid(row=0, column=0, padx=20, pady=20)

computer_choice_label = tk.Label(root, text="Computer: ", font=("Arial", 14), width=15, anchor='w', bg="#2e2e2e", fg="white")
computer_choice_label.grid(row=0, column=2, padx=20, pady=20)

result_label = tk.Label(root, text="", font=("Arial", 14), width=25, anchor='center', bg="#2e2e2e", fg="white")
result_label.grid(row=1, column=0, columnspan=3, pady=10)

user_score_label = tk.Label(root, text="User: 0", font=("Arial", 14), width=15, anchor='w', bg="#2e2e2e", fg="white")
user_score_label.grid(row=2, column=0, padx=20, pady=10)

computer_score_label = tk.Label(root, text="Computer: 0", font=("Arial", 14), width=15, anchor='w', bg="#2e2e2e", fg="white")
computer_score_label.grid(row=2, column=2, padx=20, pady=10)

rock_button = tk.Button(root, text="Rock", command=lambda: play("Rock"), font=("Arial", 12), bg="#444444", fg="white")
rock_button.grid(row=3, column=0, padx=20, pady=10)

paper_button = tk.Button(root, text="Paper", command=lambda: play("Paper"), font=("Arial", 12), bg="#444444", fg="white")
paper_button.grid(row=3, column=1, padx=20, pady=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play("Scissors"), font=("Arial", 12), bg="#444444", fg="white")
scissors_button.grid(row=3, column=2, padx=20, pady=10)

reset_button = tk.Button(root, text="Play Again", command=reset_game, font=("Arial", 12), bg="#444444", fg="white")
reset_button.grid(row=4, column=1, padx=20, pady=20)

root.mainloop()
