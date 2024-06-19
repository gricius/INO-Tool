# views/ino_tool_view.py
import tkinter as tk
from utils import paste_from_clipboard

def show_ino_tool(frame):
    # Clear the frame
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="INO Tool").grid(row=0, column=0, columnspan=2, pady=5)

    input_frame = tk.Frame(frame)
    input_frame.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

    output_frame = tk.Frame(frame)
    output_frame.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

    # Input frame
    paste_button = tk.Button(input_frame, text="Paste", command=lambda: paste_from_clipboard(frame, source_text, original_text, sorted_text, original_canvas, sorted_canvas))
    paste_button.grid(row=0, column=0, pady=5)
    
    source_text = tk.Text(input_frame, wrap=tk.WORD, width=50, height=10)
    source_text.grid(row=1, column=0, padx=5, pady=5)

    # Output frame
    original_label = tk.Label(output_frame, text="Original Text")
    original_label.grid(row=0, column=0, pady=5)
    original_text = tk.Text(output_frame, wrap=tk.WORD, width=50, height=10)
    original_text.grid(row=1, column=0, padx=5, pady=5)

    sorted_label = tk.Label(output_frame, text="Sorted Text")
    sorted_label.grid(row=2, column=0, pady=5)
    sorted_text = tk.Text(output_frame, wrap=tk.WORD, width=50, height=10)
    sorted_text.grid(row=3, column=0, padx=5, pady=5)

    # Canvases
    original_canvas = tk.Canvas(output_frame, width=200, height=200, bg="white")
    original_canvas.grid(row=4, column=0, pady=5)

    sorted_canvas = tk.Canvas(output_frame, width=200, height=200, bg="white")
    sorted_canvas.grid(row=5, column=0, pady=5)
