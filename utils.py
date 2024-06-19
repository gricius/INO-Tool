# utils.py
import tkinter as tk
import re

def extract_coordinates(text):
    # Regular expressions to match coordinates
    patterns = [
        r'(\d{2})(\d{2})(\d{2})N(\d{3})(\d{2})(\d{2})E',  # DDMMSSNDDDMMSSSE
        r'(\d{2})(\d{2})(\d{2})N(\d{3})(\d{2})(\d{2})W',  # DDMMSSNDDDMMSSSW
        r'(\d{2})(\d{2})(\d{2})S(\d{3})(\d{2})(\d{2})E',  # DDMMSSSDDDMMSSSE
        r'(\d{2})(\d{2})(\d{2})S(\d{3})(\d{2})(\d{2})W',  # DDMMSSSDDDMMSSSW
        r'(\d{2})(\d{2})N(\d{3})(\d{2})E',               # DDMMNDDDMME
        r'(\d{2})(\d{2})N(\d{3})(\d{2})W',               # DDMMNDDDMMW
        r'(\d{2})(\d{2})S(\d{3})(\d{2})E',               # DDMMSSSDDDMME
        r'(\d{2})(\d{2})S(\d{3})(\d{2})W'                # DDMMSSSDDDMMW
    ]
    
    coords = []
    for pattern in patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            coords.append(''.join(match))  # Ensure match is iterable
    return coords

def paste_from_clipboard(frame, source_text, original_text, sorted_text, original_canvas, sorted_canvas):
    clipboard_text = frame.clipboard_get()
    source_text.delete("1.0", tk.END)
    source_text.insert(tk.END, clipboard_text)

    coords = extract_coordinates(clipboard_text)
    if coords:
        draw_coordinates(coords, original_canvas)
        draw_coordinates(sorted(coords), sorted_canvas)

        original_text.delete("1.0", tk.END)
        original_text.insert(tk.END, "\n".join(coords))

        sorted_text.delete("1.0", tk.END)
        sorted_text.insert(tk.END, "\n".join(sorted(coords)))
    else:
        original_text.delete("1.0", tk.END)
        sorted_text.delete("1.0", tk.END)
        original_text.insert(tk.END, "No valid coordinates found.")
        sorted_text.insert(tk.END, "No valid coordinates found.")

def draw_coordinates(coords, canvas):
    canvas.delete("all")
    
    # Ensure coords are non-empty before proceeding
    if not coords:
        return

    lats = []
    lons = []
    for coord in coords:
        if len(coord) == 14:  # DDMMSSNDDDMMSSSE or DDMMSSNDDDMMSSSW
            lats.append(int(coord[:2]) + int(coord[2:4])/60 + int(coord[4:6])/3600)
            lons.append(int(coord[7:10]) + int(coord[10:12])/60 + int(coord[12:])/3600)
        elif len(coord) == 10:  # DDMMNDDDMME or DDMMNDDDMMW
            lats.append(int(coord[:2]) + int(coord[2:4])/60)
            lons.append(int(coord[5:8]) + int(coord[8:])/60)

    width = canvas.winfo_width()
    height = canvas.winfo_height()
    max_lat = max(lats)
    min_lat = min(lats)
    max_lon = max(lons)
    min_lon = min(lons)

    def transform(lat, lon):
        x = (lon - min_lon) / (max_lon - min_lon) * width
        y = height - (lat - min_lat) / (max_lat - min_lat) * height
        return x, y

    for i in range(len(coords) - 1):
        x1, y1 = transform(lats[i], lons[i])
        x2, y2 = transform(lats[i+1], lons[i+1])
        canvas.create_line(x1, y1, x2, y2, fill="blue")
