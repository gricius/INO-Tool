# gui.py

import tkinter as tk
from tkinter import messagebox, scrolledtext
from utils import extract_coordinates, draw_coordinates

def open_page(page_name, root, ino_tool_frame, source_text, original_text, sorted_text, original_canvas, sorted_canvas):
    if page_name == "INO_helper.html":
        show_ino_tool(root, ino_tool_frame, source_text, original_text, sorted_text, original_canvas, sorted_canvas)
    elif page_name == "Refresh":
        refresh_view(source_text, original_text, sorted_text, original_canvas, sorted_canvas)

def refresh_view(source_text, original_text, sorted_text, original_canvas, sorted_canvas):
    source_text.delete('1.0', tk.END)
    original_text.delete('1.0', tk.END)
    sorted_text.delete('1.0', tk.END)
    original_canvas.delete('all')
    sorted_canvas.delete('all')

def paste_from_clipboard(root, source_text, original_text, sorted_text, original_canvas, sorted_canvas):
    refresh_view(source_text, original_text, sorted_text, original_canvas, sorted_canvas)
    
    try:
        clipboard_content = root.clipboard_get()
        source_text.insert(tk.END, clipboard_content)
        
        coords = extract_coordinates(clipboard_content)
        
        for coord in coords:
            original_text.insert(tk.END, coord + "\n")
        
        unique_sorted_coords = sorted(set(coords))
        for coord in unique_sorted_coords:
            sorted_text.insert(tk.END, coord + "\n")
        
        draw_coordinates(coords, original_canvas)
        draw_coordinates(unique_sorted_coords, sorted_canvas)
    except tk.TclError:
        messagebox.showwarning("Warning", "No content in clipboard")

def transform(source_text, sorted_text):
    source_content = source_text.get("1.0", tk.END).strip()
    if source_content:
        sorted_text.delete("1.0", tk.END)
        sorted_text.insert(tk.END, source_content[::-1])

def clear_text(source_text):
    source_text.delete('1.0', tk.END)

def format_d(source_text):
    input_string = source_text.get("1.0", tk.END).strip()
    formatted_string = input_string.replace(" ", "")
    source_text.delete('1.0', tk.END)
    source_text.insert(tk.END, formatted_string)

def copy_coords(root):
    coords = "4447N03354E"
    root.clipboard_clear()
    root.clipboard_append(coords)
    messagebox.showinfo("Info", f"Copied to clipboard: {coords}")

def show_ino_tool(root, ino_tool_frame, source_text, original_text, sorted_text, original_canvas, sorted_canvas):
    for widget in ino_tool_frame.winfo_children():
        widget.pack_forget()
    ino_tool_frame.pack(pady=10, fill=tk.BOTH, expand=True)
    
    input_frame = tk.Frame(ino_tool_frame)
    input_frame.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

    paste_button = tk.Button(input_frame, text="Paste", command=lambda: paste_from_clipboard(root, source_text, original_text, sorted_text, original_canvas, sorted_canvas))
    paste_button.pack()

    source_text = scrolledtext.ScrolledText(input_frame, width=30, height=20)
    source_text.pack(fill=tk.BOTH, expand=True)

    buttons_frame = tk.Frame(input_frame)
    buttons_frame.pack(pady=10)

    transform_button = tk.Button(buttons_frame, text="Copy Min Max && Transform >", command=lambda: transform(source_text, sorted_text))
    transform_button.pack()

    clear_button = tk.Button(buttons_frame, text="Clear", command=lambda: clear_text(source_text))
    clear_button.pack()

    coords_button = tk.Button(buttons_frame, text="Copy Crimea COORD", command=lambda: copy_coords(root))
    coords_button.pack()

    format_button = tk.Button(buttons_frame, text="Format && <- copy YB times", command=lambda: format_d(source_text))
    format_button.pack()

    converters_frame = tk.Frame(ino_tool_frame)
    converters_frame.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

    tk.Label(converters_frame, text="KM").grid(row=0, column=0)
    km_entry = tk.Entry(converters_frame)
    km_entry.grid(row=0, column=1)

    tk.Label(converters_frame, text="NM").grid(row=0, column=2)
    nm_entry = tk.Entry(converters_frame)
    nm_entry.grid(row=0, column=3)

    results_frame = tk.Frame(ino_tool_frame)
    results_frame.pack(side=tk.LEFT, padx=10, fill=tk.BOTH, expand=True)

    tk.Label(results_frame, text="Original").pack()
    original_text = scrolledtext.ScrolledText(results_frame, width=30, height=10)
    original_text.pack(fill=tk.BOTH, expand=True)

    original_canvas = tk.Canvas(results_frame, width=300, height=300, bg='white')
    original_canvas.pack(fill=tk.BOTH, expand=True)

    tk.Label(results_frame, text="Sorted").pack()
    sorted_text = scrolledtext.ScrolledText(results_frame, width=30, height=10)
    sorted_text.pack(fill=tk.BOTH, expand=True)

    sorted_canvas = tk.Canvas(results_frame, width=300, height=300, bg='white')
    sorted_canvas.pack(fill=tk.BOTH, expand=True)
