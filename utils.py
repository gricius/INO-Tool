import tkinter as tk

def paste_from_clipboard(root, source_text, original_text=None, sorted_text=None, original_canvas=None, sorted_canvas=None):
    try:
        clipboard_content = root.clipboard_get()
        source_text.delete("1.0", tk.END)
        source_text.insert(tk.END, clipboard_content)
        if original_text is not None:
            coords = extract_coordinates(clipboard_content)
            original_text.delete("1.0", tk.END)
            original_text.insert(tk.END, "\n".join(coords))
        if sorted_text is not None:
            coords = extract_coordinates(clipboard_content)
            sorted_coords = sorted(coords)
            sorted_text.delete("1.0", tk.END)
            sorted_text.insert(tk.END, "\n".join(sorted_coords))
            if original_canvas is not None and sorted_canvas is not None:
                draw_coordinates(coords, original_canvas)
                draw_coordinates(sorted_coords, sorted_canvas)
    except tk.TclError:
        print("Error: No text in clipboard")

def extract_coordinates(text):
    import re

    patterns = [
        re.compile(r'(\d{2})(\d{2})(\d{2}\.\d{2})([NS])(\d{3})(\d{2})(\d{2}\.\d{2})([EW])'),
        re.compile(r'(\d{2})(\d{2})(\d{2})([NS])(\d{3})(\d{2})(\d{2})([EW])'),
        re.compile(r'(\d{2})(\d{2})([NS])(\d{3})(\d{2})([EW])'),
        re.compile(r'(\d{2})(\d{2})(\d{2})([NS])/(\d{3})(\d{2})(\d{2})([EW])')  # New pattern
    ]

    coords = []
    for pattern in patterns:
        matches = pattern.findall(text)
        for match in matches:
            if len(match) == 8:
                lat_deg = match[0]
                lat_min = match[1]
                lat_sec = match[2]
                lat_dir = match[3]
                lon_deg = match[4]
                lon_min = match[5]
                lon_sec = match[6]
                lon_dir = match[7]

                formatted_coord = f"{lat_deg}{lat_min}{lat_sec}{lat_dir}{lon_deg}{lon_min}{lon_sec}{lon_dir}"
                coords.append(formatted_coord)
            elif len(match) == 6:
                lat_deg = match[0]
                lat_min = match[1]
                lat_dir = match[2]
                lon_deg = match[3]
                lon_min = match[4]
                lon_dir = match[5]

                formatted_coord = f"{lat_deg}{lat_min}{lat_dir}{lon_deg}{lon_min}{lon_dir}"
                coords.append(formatted_coord)
            elif len(match) == 7:
                lat_deg = match[0]
                lat_min = match[1]
                lat_sec = match[2]
                lat_dir = match[3]
                lon_deg = match[4]
                lon_min = match[5]
                lon_sec = match[6]
                lon_dir = match[7]

                formatted_coord = f"{lat_deg}{lat_min}{lat_sec}{lat_dir}{lon_deg}{lon_min}{lon_sec}{lon_dir}"
                coords.append(formatted_coord)
    return coords

def draw_coordinates(coords, canvas):
    canvas.delete("all")
    if not coords:
        return

    lats, lons = zip(*[parse_coordinate(coord) for coord in coords])
    max_lat = max(lats)
    min_lat = min(lats)
    max_lon = max(lons)
    min_lon = min(lons)

    def transform(lat, lon):
        x = (lon - min_lon) / (max_lon - min_lon) * canvas.winfo_width()
        y = (max_lat - lat) / (max_lat - min_lat) * canvas.winfo_height()
        return x, y

    for lat, lon in zip(lats, lons):
        x, y = transform(lat, lon)
        canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="blue")

    for i in range(len(lats) - 1):
        x1, y1 = transform(lats[i], lons[i])
        x2, y2 = transform(lats[i + 1], lons[i + 1])
        canvas.create_line(x1, y1, x2, y2, fill="blue")

def parse_coordinate(coord):
    import re

    match = re.match(r'(\d{2})(\d{2})(\d{2})([NS])(\d{3})(\d{2})(\d{2})([EW])', coord)
    if match:
        lat_deg = int(match[1])
        lat_min = int(match[2])
        lat_sec = float(match[3])
        lat_dir = match[4]
        lon_deg = int(match[5])
        lon_min = int(match[6])
        lon_sec = float(match[7])
        lon_dir = match[8]

        lat = lat_deg + lat_min / 60 + lat_sec / 3600
        if lat_dir == 'S':
            lat = -lat
        lon = lon_deg + lon_min / 60 + lon_sec / 3600
        if lon_dir == 'W':
            lon = -lon

        return lat, lon
    match = re.match(r'(\d{2})(\d{2})([NS])(\d{3})(\d{2})([EW])', coord)
    if match:
        lat_deg = int(match[1])
        lat_min = int(match[2])
        lat_dir = match[3]
        lon_deg = int(match[4])
        lon_min = int(match[5])
        lon_dir = match[6]

        lat = lat_deg + lat_min / 60
        if lat_dir == 'S':
            lat = -lat
        lon = lon_deg + lon_min / 60
        if lon_dir == 'W':
            lon = -lon

        return lat, lon
    match = re.match(r'(\d{2})(\d{2})(\d{2})([NS])/(\d{3})(\d{2})(\d{2})([EW])', coord)
    if match:
        lat_deg = int(match[1])
        lat_min = int(match[2])
        lat_sec = int(match[3])
        lat_dir = match[4]
        lon_deg = int(match[5])
        lon_min = int(match[6])
        lon_sec = int(match[7])
        lon_dir = match[8]

        lat = lat_deg + lat_min / 60 + lat_sec / 3600
        if lat_dir == 'S':
            lat = -lat
        lon = lon_deg + lon_min / 60 + lon_sec / 3600
        if lon_dir == 'W':
            lon = -lon

        return lat, lon

    return None, None

def find_and_replace(text_widget, find_text, replace_text):
    content = text_widget.get("1.0", tk.END)
    new_content = content.replace(find_text, replace_text)
    text_widget.delete("1.0", tk.END)
    text_widget.insert(tk.END, new_content)
