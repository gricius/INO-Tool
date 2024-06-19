import tkinter as tk
from tkinter import messagebox

# Define a global variable to store the tasks
todo_entries = ["Task 1", "Task 2", "Task 3"]  # Example entries; replace with actual loading logic

def show_todo(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="To-Do List").pack(pady=5)

    todo_listbox = tk.Listbox(frame, width=50, height=20)
    todo_listbox.pack(pady=5)

    for entry in todo_entries:
        todo_listbox.insert(tk.END, entry)

    def add_task():
        task = task_entry.get()
        if task:
            todo_listbox.insert(tk.END, task)
            todo_entries.append(task)  # Add to the global list
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def remove_task():
        try:
            selected_task_index = todo_listbox.curselection()[0]
            todo_listbox.delete(selected_task_index)
            del todo_entries[selected_task_index]  # Remove from the global list
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

    task_entry = tk.Entry(frame, width=50)
    task_entry.pack(pady=5)

    button_frame = tk.Frame(frame)
    button_frame.pack(pady=5)

    add_button = tk.Button(button_frame, text="Add Task", command=add_task)
    add_button.pack(side=tk.LEFT, padx=5)

    remove_button = tk.Button(button_frame, text="Remove Task", command=remove_task)
    remove_button.pack(side=tk.LEFT, padx=5)
