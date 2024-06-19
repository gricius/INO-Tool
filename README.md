# Initial Update
## Initial Update Directory  Structure
INOTool_py/ app to help in daily INO processing
│
├── main.py Entry point for the application.
├── gui.py Contains the functions to set up and manage the GUI.
├── utils.py Utility functions used across the application.
├── views/ A directory containing separate modules for each view.
│   ├── __init__.py can be empty. Python recognizes views as a package by adding an __init__.py file to the views directory.
│   ├── home_view.py contains a disclaimer and a content of news.txt
│   ├── ino_tool_view.py coordinates extractor from a text in Widnows clipboard, formating in to INO Polygon function accepted formats - DDMMSSNDDDMMSSE or DDMMNDDDMME.
│   ├── abbreviation_tool_view.py search for ICAO and national or military abbreviations
│   ├── notepad_view.py notepad with find and replace
│   └── todo_view.py task list or notes list
├── news.txt a file containing an info for a user
└── abbreviation.json compilation of all known abbreviations by ICAO and others



## ToDo: add maximum possible patterns to:
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

## ToDo: Copy to Windows Clipboard