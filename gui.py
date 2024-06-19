import tkinter as tk
from views.home_view import show_home
from views.ino_tool_view import show_ino_tool
from views.abbreviation_tool_view import show_abbreviation_tool
from views.notepad_view import show_notepad
from views.todo_view import show_todo

def create_main_window():
    root = tk.Tk()
    root.title("Main Application")

    menubar = tk.Menu(root)

    def show_home_page():
        show_home(main_frame)

    def show_ino_tool_page():
        show_ino_tool(main_frame)

    def show_abbreviation_tool_page():
        show_abbreviation_tool(main_frame)

    def show_notepad_page():
        show_notepad(main_frame)

    def show_todo_page():
        show_todo(main_frame)

    menubar.add_command(label="Home", command=show_home_page)
    menubar.add_command(label="INO Tool", command=show_ino_tool_page)
    menubar.add_command(label="Abbreviation Tool", command=show_abbreviation_tool_page)
    menubar.add_command(label="Notepad", command=show_notepad_page)
    menubar.add_command(label="ToDo", command=show_todo_page)

    root.config(menu=menubar)

    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True)

    # Show the home page by default
    show_home_page()

    return root

if __name__ == "__main__":
    root = create_main_window()
    root.mainloop()
