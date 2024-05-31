import tkinter as tk
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x500")
        self.center_window(400, 500)
        self.equation_text = ""
        self.equation_label = tk.StringVar()
        self.create_widgets()

    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

    def create_widgets(self):
        label = tk.Label(self, textvariable=self.equation_label, font=('Arial', 24), fg="white", bg="black", width=24, height=2, borderwidth=3, relief="ridge")
        label.pack(pady=15, padx=10)
        buttons_frame = tk.Frame(self, bg="black")
        buttons_frame.pack()
        button_texts = [
            ("exp", 0, 0), ("ln", 0, 1), ("^2", 0, 2), ("π", 0, 3), ("Clear", 0, 4),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3), ("Del", 1, 4),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3), (")", 2, 4),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3), ("(", 3, 4),
            (".", 4, 0), ("0", 4, 1), ("/", 4, 2), ("%", 4, 3), ("=", 4, 4)
        ]
        for text, row, column in button_texts:
            button = tk.Button(buttons_frame, text=text, height=2, width=5, font=('Arial', 14), fg="white", bg="black", command=lambda t=text: self.button_press(t))
            button.grid(row=row, column=column, padx=5, pady=5)

    def button_press(self, num):
        if num == "=":
            self.equals()
        elif num == "Del":
            self.equation_text = self.equation_text[:-1]
            self.equation_label.set(self.equation_text)
        elif num == "%":
            self.equation_text += "*" + str(0.01)
            self.equation_label.set(self.equation_text)
        elif num == "exp":
            self.equation_text += "exp("
            self.equation_label.set(self.equation_text)
        elif num == "ln":
            self.equation_text += "ln("
            self.equation_label.set(self.equation_text)
        elif num == "^2":
            self.equation_text += "^2"
            self.equation_label.set(self.equation_text)
        elif num == "π":
            self.equation_text += "π"
            self.equation_label.set(self.equation_text)
        elif num == "Clear":
            self.clear()
        else:
            self.equation_text += str(num)
            self.equation_label.set(self.equation_text)

    def equals(self):
        try:
            expression = self.equation_text.replace('exp', 'math.exp').replace('ln', 'math.log').replace('π', 'math.pi').replace('^2', '**2')
            total = str(eval(expression))
            self.equation_label.set(total)
            self.equation_text = total
        except (SyntaxError, ZeroDivisionError, ValueError):
            self.equation_label.set("Error")
            self.equation_text = ""

    def clear(self):
        self.equation_label.set("")
        self.equation_text = ""

if __name__ == "__main__":
    app = Calculator()
    app.configure(bg="black")
    app.mainloop()

