import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("At least one option must be selected.")
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_password_button():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than zero.")
            return
        
        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()
        
        if not (use_letters or use_numbers or use_symbols):
            messagebox.showerror("Error", "You must select at least one option (letters, numbers, or symbols).")
            return
        
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        password_display.config(state=tk.NORMAL)
        password_display.delete(0, tk.END)
        password_display.insert(0, password)
        password_display.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")  

center_window(root, 400, 300)

length_label = tk.Label(root, text="Password length:", font=("Arial", 12))
length_label.pack(pady=10)

length_entry = tk.Entry(root, font=("Arial", 12), width=10)
length_entry.pack(pady=5)

checkbox_frame = tk.Frame(root)
checkbox_frame.pack(pady=10)

letters_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

letters_check = tk.Checkbutton(checkbox_frame, text="Letters", variable=letters_var, font=("Arial", 12))
letters_check.pack(anchor='w')

numbers_check = tk.Checkbutton(checkbox_frame, text="Numbers", variable=numbers_var, font=("Arial", 12))
numbers_check.pack(anchor='w')

symbols_check = tk.Checkbutton(checkbox_frame, text="Symbols", variable=symbols_var, font=("Arial", 12))
symbols_check.pack(anchor='w')

generate_button = tk.Button(root, text="Generate Password", command=generate_password_button, font=("Arial", 12), width=20)
generate_button.pack(pady=15)

password_display = tk.Entry(root, font=("Arial", 12), state=tk.DISABLED, width=30)
password_display.pack(pady=5)

root.mainloop()
