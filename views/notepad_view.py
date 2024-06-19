import tkinter as tk

def show_notepad(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="Notepad").pack(pady=5)

    input_frame = tk.Frame(frame)
    input_frame.pack(pady=5)

    paste_button = tk.Button(input_frame, text="Paste", command=lambda: paste_text(text_widget))
    paste_button.pack(pady=5)

    text_widget = tk.Text(input_frame, wrap=tk.WORD, width=80, height=20)
    text_widget.pack(pady=5)

    def paste_text(widget):
        clipboard_text = frame.clipboard_get()
        widget.insert(tk.END, clipboard_text)

    find_replace_frame = tk.Frame(frame)
    find_replace_frame.pack(pady=5)

    tk.Label(find_replace_frame, text="Find:").pack(side=tk.LEFT, padx=5)
    find_entry = tk.Entry(find_replace_frame)
    find_entry.pack(side=tk.LEFT, padx=5)

    tk.Label(find_replace_frame, text="Replace:").pack(side=tk.LEFT, padx=5)
    replace_entry = tk.Entry(find_replace_frame)
    replace_entry.pack(side=tk.LEFT, padx=5)

    def find_replace():
        find_text = find_entry.get()
        replace_text = replace_entry.get()
        content = text_widget.get("1.0", tk.END)
        updated_content = content.replace(find_text, replace_text)
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, updated_content)

    replace_button = tk.Button(find_replace_frame, text="Replace", command=find_replace)
    replace_button.pack(side=tk.LEFT, padx=5)
