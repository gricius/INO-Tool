# utils.py

import re

def extract_coordinates(text):
    pattern1 = r"\b\d{4,6}[NS]\d{5,7}[EW]\b"  # Handles 3750N01228E or 384600N0723000W
    pattern2 = r"\b[NS]\d{4,6}[EW]\d{5,7}\b"  # Handles N3750E01228 or N384600W0723000
    pattern3 = r"\b\d{4,6}[NS]/\d{5,7}[EW]\b"  # Handles 3750N/01228E or 422513S/0734716W
    
    coords1 = re.findall(pattern1, text)
    coords2 = re.findall(pattern2, text)
    coords3 = re.findall(pattern3, text)
    
    converted_coords2 = [convert_coord_format(coord) for coord in coords2]
    converted_coords3 = [convert_coord_format(coord.replace('/', '')) for coord in coords3]
    
    return coords1 + converted_coords2 + converted_coords3

def convert_coord_format(coord):
    if '/' in coord:
        coord = coord.replace('/', '')
    
    has_seconds = len(coord) == 15
    
    if has_seconds:
        lat_dir = coord[0]
        lat_deg = coord[1:3]
        lat_min = coord[3:5]
        lat_sec = coord[5:7]
        lon_dir = coord[7]
        lon_deg = coord[8:11]
        lon_min = coord[11:13]
        lon_sec = coord[13:15]
        return f"{lat_deg}{lat_min}{lat_sec}{lat_dir}{lon_deg}{lon_min}{lon_sec}{lon_dir}"
    else:
        lat_deg = coord[:2]
        lat_min = coord[2:4]
        lat_dir = coord[4]
        lon_deg = coord[5:8]
        lon_min = coord[8:10]
        lon_dir = coord[10]
        return f"{lat_deg}{lat_min}00{lat_dir}{lon_deg}{lon_min}00{lon_dir}"

def convert_to_decimal(coord):
    lat_deg = int(coord[:2])
    lat_min = int(coord[2:4])
    lat_sec = int(coord[4:6]) if len(coord) > 6 else 0
    lat_dir = coord[6] if len(coord) > 6 else coord[4]
    lon_deg = int(coord[7:10]) if len(coord) > 6 else int(coord[5:8])
    lon_min = int(coord[10:12]) if len(coord) > 6 else int(coord[8:10])
    lon_sec = int(coord[12:14]) if len(coord) > 6 else 0
    lon_dir = coord[14] if len(coord) > 6 else coord[10]
    
    lat = lat_deg + lat_min / 60 + lat_sec / 3600
    lon = lon_deg + lon_min / 60 + lon_sec / 3600
    
    if lat_dir == 'S':
        lat = -lat
    if lon_dir == 'W':
        lon = -lon
    
    return lat, lon

def draw_coordinates(coords, canvas):
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    
    if not coords:
        return
    
    decimal_coords = [convert_to_decimal(coord) for coord in coords]
    latitudes = [lat for lat, lon in decimal_coords]
    longitudes = [lon for lat, lon in decimal_coords]
    
    min_lat = min(latitudes)
    max_lat = max(latitudes)
    min_lon = min(longitudes)
    max_lon = max(longitudes)
    
    def scale(coord, min_val, max_val, size):
        return (coord - min_val) / (max_val - min_val) * size
    
    scaled_coords = [(scale(lat, min_lat, max_lat, canvas_height), 
                      scale(lon, min_lon, max_lon, canvas_width)) for lat, lon in decimal_coords]
    
    for i in range(len(scaled_coords) - 1):
        x1, y1 = scaled_coords[i]
        x2, y2 = scaled_coords[i + 1]
        canvas.create_line(y1, x1, y2, x2, fill="blue")
    
    for x, y in scaled_coords:
        canvas.create_oval(y - 2, x - 2, y + 2, x + 2, fill="red")
