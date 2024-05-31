import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("600x500")
        self.root.configure(bg='white')
        self.tasks = []
        self.create_widgets()
        self.center_window()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Task List", bg='white', fg='black', font=('Helvetica', 18))
        self.title_label.pack(pady=10)

        self.task_listbox = tk.Listbox(self.root, bg='white', fg='black', font=('Helvetica', 12))
        self.task_listbox.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        self.entry_frame = tk.Frame(self.root, bg='white')
        self.entry_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.entry_frame, bg='white', fg='black', font=('Helvetica', 12))
        self.task_entry.pack(side=tk.LEFT, padx=10)

        self.date_entry = DateEntry(self.entry_frame, bg='white', fg='black', font=('Helvetica', 12), date_pattern='y-mm-dd')
        self.date_entry.pack(side=tk.LEFT, padx=10)

        self.hour_spinbox = tk.Spinbox(self.entry_frame, from_=0, to=23, wrap=True, width=2, format="%02.0f", font=('Helvetica', 12))
        self.hour_spinbox.pack(side=tk.LEFT, padx=5)
        
        self.minute_spinbox = tk.Spinbox(self.entry_frame, from_=0, to=59, wrap=True, width=2, format="%02.0f", font=('Helvetica', 12))
        self.minute_spinbox.pack(side=tk.LEFT, padx=5)

        self.add_task_button = tk.Button(self.entry_frame, text="Add Task", bg='lightgrey', fg='black', command=self.add_task)
        self.add_task_button.pack(side=tk.LEFT)

        self.button_frame = tk.Frame(self.root, bg='white')
        self.button_frame.pack(pady=10)
        
        self.update_task_button = tk.Button(self.button_frame, text="Update Task", bg='lightgrey', fg='black', width=20, command=self.update_task)
        self.update_task_button.grid(row=0, column=0, padx=5, pady=5)

        self.delete_task_button = tk.Button(self.button_frame, text="Delete Task", bg='lightgrey', fg='black', width=20, command=self.delete_task)
        self.delete_task_button.grid(row=0, column=1, padx=5, pady=5)

        self.delete_all_tasks_button = tk.Button(self.button_frame, text="Delete All Tasks", bg='lightgrey', fg='black', width=20, command=self.delete_all_tasks)
        self.delete_all_tasks_button.grid(row=1, column=0, padx=5, pady=5)

        self.exit_button = tk.Button(self.button_frame, text="Exit", bg='lightgrey', fg='black', width=20, command=self.exit_app)
        self.exit_button.grid(row=1, column=1, padx=5, pady=5)
        
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get()
        date = self.date_entry.get()
        hour = self.hour_spinbox.get()
        minute = self.minute_spinbox.get()
        if task:
            task_with_datetime = f"{task} (due on {date} at {hour}:{minute})"
            self.tasks.append(task_with_datetime)
            self.task_listbox.insert(tk.END, task_with_datetime)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Attention", "Please enter a task.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            new_task = self.task_entry.get()
            new_date = self.date_entry.get()
            new_hour = self.hour_spinbox.get()
            new_minute = self.minute_spinbox.get()
            if new_task:
                updated_task_with_datetime = f"{new_task} (due on {new_date} at {new_hour}:{new_minute})"
                self.tasks[selected_task_index[0]] = updated_task_with_datetime
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, updated_task_with_datetime)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Attention", "Please enter a task.")
        else:
            messagebox.showwarning("Attention", "Please select a task to update.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            del self.tasks[selected_task_index[0]]
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Attention", "Please select a task to delete.")

    def delete_all_tasks(self):
        if messagebox.askyesno("Confirmation", "Are you sure you want to delete all tasks?"):
            self.tasks.clear()
            self.task_listbox.delete(0, tk.END)

    def load_tasks(self):
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
    
    def exit_app(self):
        self.root.quit()

    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
