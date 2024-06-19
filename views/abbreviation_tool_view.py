import tkinter as tk
import json
import os

def show_abbreviation_tool(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="Abbreviation Tool").pack(pady=5)

    filter_frame = tk.Frame(frame)
    filter_frame.pack(pady=5)

    tk.Label(filter_frame, text="Filter keyword:").pack(side=tk.LEFT, padx=5)
    keyword_entry = tk.Entry(filter_frame)
    keyword_entry.pack(side=tk.LEFT, padx=5)

    result_text = tk.Text(frame, wrap=tk.WORD, height=20, width=80)
    result_text.pack(pady=5)

    def search_abbreviations():
        keyword = keyword_entry.get()
        abbreviation_file = os.path.join(os.path.dirname(__file__), '..', 'abbreviation.json')
        with open(abbreviation_file, 'r') as file:
            data = json.load(file)

        filtered_abbr = [abbr for abbr in data['abbreviations'] if keyword.lower() in abbr['name'].lower()]

        result_text.delete("1.0", tk.END)
        for abbr in filtered_abbr:
            result_text.insert(tk.END, f"Name: {abbr['name']}, Email: {abbr['email']}\n")

    search_button = tk.Button(filter_frame, text="Search", command=search_abbreviations)
    search_button.pack(side=tk.LEFT, padx=5)
