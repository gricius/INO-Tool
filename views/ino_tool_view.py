import tkinter as tk
from utils import paste_from_clipboard

def show_ino_tool(root, main_frame):
    # Clear the main frame
    for widget in main_frame.winfo_children():
        widget.destroy()

    frame = tk.Frame(main_frame)
    frame.pack(fill="both", expand=True)

    input_frame = tk.Frame(frame)
    input_frame.pack(fill="x", pady=10)

    source_text = tk.Text(input_frame, height=5, width=80)
    source_text.pack(padx=5, pady=5)

    paste_button = tk.Button(input_frame, text="Paste", command=lambda: paste_from_clipboard(root, source_text, original_text, sorted_text, original_canvas, sorted_canvas))
    paste_button.pack(side=tk.LEFT, padx=5)

    original_text = tk.Text(frame, height=5, width=80)
    original_text.pack(padx=5, pady=5)

    sorted_text = tk.Text(frame, height=5, width=80)
    sorted_text.pack(padx=5, pady=5)

    canvas_frame = tk.Frame(frame)
    canvas_frame.pack(fill="x", pady=10)

    original_canvas = tk.Canvas(canvas_frame, bg="white", width=400, height=400)
    original_canvas.pack(side=tk.LEFT, padx=5, pady=5)

    sorted_canvas = tk.Canvas(canvas_frame, bg="white", width=400, height=400)
    sorted_canvas.pack(side=tk.LEFT, padx=5, pady=5)
