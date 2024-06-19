import tkinter as tk
import json

def show_abbreviation_tool(root, main_frame):
    # Clear the main frame
    for widget in main_frame.winfo_children():
        widget.destroy()

    frame = tk.Frame(main_frame)
    frame.pack(fill="both", expand=True)

    search_frame = tk.Frame(frame)
    search_frame.pack(fill="x", pady=10)

    search_label = tk.Label(search_frame, text="Search Abbreviation:")
    search_label.pack(side=tk.LEFT, padx=5)

    search_entry = tk.Entry(search_frame)
    search_entry.pack(side=tk.LEFT, padx=5)

    result_text = tk.Text(frame, height=20, width=80)
    result_text.pack(padx=5, pady=5)

    def search_abbreviations():
        search_term = search_entry.get().lower()
        try:
            with open("abbreviation.json", "r") as file:
                data = json.load(file)
                abbreviations = data.get("abbreviations", [])
                filtered_abbr = [abbr for abbr in abbreviations if search_term in abbr.get("name", "").lower()]
                result_text.delete("1.0", tk.END)
                for abbr in filtered_abbr:
                    result_text.insert(tk.END, f"Name: {abbr['name']}, Email: {abbr['email']}\n")
        except FileNotFoundError:
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, "No abbreviation file found.")

    search_button = tk.Button(search_frame, text="Search", command=search_abbreviations)
    search_button.pack(side=tk.LEFT, padx=5)
