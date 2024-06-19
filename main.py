# main.py

import tkinter as tk
from tkinter import scrolledtext
from gui import open_page, refresh_view, show_ino_tool

def main():
    root = tk.Tk()
    root.title("Navigation Menu")
    root.geometry("1200x800")

    menu_frame = tk.Frame(root)
    menu_frame.pack(pady=10)

    buttons = [
        ("INO Tool", "INO_helper.html"),
        ("Refresh", "Refresh")
    ]

    ino_tool_frame = tk.Frame(root)
    ino_tool_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    source_text = scrolledtext.ScrolledText(ino_tool_frame, width=30, height=20)
    original_text = scrolledtext.ScrolledText(ino_tool_frame, width=30, height=10)
    sorted_text = scrolledtext.ScrolledText(ino_tool_frame, width=30, height=10)
    original_canvas = tk.Canvas(ino_tool_frame, width=300, height=300, bg='white')
    sorted_canvas = tk.Canvas(ino_tool_frame, width=300, height=300, bg='white')

    for text, page in buttons:
        button = tk.Button(menu_frame, text=text, command=lambda p=page: open_page(p, root, ino_tool_frame, source_text, original_text, sorted_text, original_canvas, sorted_canvas))
        button.pack(side=tk.LEFT, padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()
