import tkinter as tk
import os

def show_home(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="Disclaimer: This application shall not be used for operations. Can be used only for testing purposes.").pack(pady=5)
    tk.Label(frame, text="The following was updated recently:").pack(pady=5)

    news_file = os.path.join(os.path.dirname(__file__), '..', 'news.txt')
    with open(news_file, 'r') as file:
        news_content = file.read()

    tk.Label(frame, text=news_content).pack(pady=5)
