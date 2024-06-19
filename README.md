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
└── todo.json list of todo



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

### Supprted extraction and display of coords (ccordinates litst (without any other text) and format shall be DDMMSSNDDDMMSSE, DDMMSSSDDDMMSSE, DDMMSSNDDDMMSSW, DDMMSSSDDMMSSW and if seconds are not provided then DDMMNDDDMME, DDMMSDDDMME, DDMMNDDDMMW, DDMMSDDMMW) from the following three samples:

DUE TO MIL STNR ALT RESERVATION ALONG (OAK ALPHA) WI THE NEW YORK 
OCEANIC CTA/FIR, NEW YORK OCEANIC WILL NOT ACCEPT IFR FLT WI AN 
AREA DEFINED AS 384600N0723000W TO 390700N0715300W TO 
384100N0715500W TO 382000N0695700W TO 383000N0690000W TO 
370000N0690000W TO 370000N0724000W TO 371500N0724000W TO 
375700N0730000W TO 382000N0724800W TO POINT OF ORIGIN.

ZONE 1 PIDPID     422513S/0734716W RDO(RADIUS) 0.44NM
ZONE 2 PIDPID     422443S/0734800W RDO 0.14NM
ZONE 3 PIDPID     422435S/0734717W RDO 0.27NM
ZONE 4 PIDPID     422428S/0734858W RDO 1.20NM
ZONE 5 PIRUQUINA  422247S/0734817W RDO 3.58NM
ZONE 6 RIO GRANDE 421817S/0734555W RDO 1.37NM
INSTRUCTIONS:PUERTO MONTT RDR 119.5MHZ
             CHILOE TWR       118.4MHZ


TEMPORARY RESTRICTED AREA IMPLEMENTED AS FOLLOW:
3750N01228E-3750N01226E-3753N01225E-
3754N01227E-3750N01228E/STAGNONE DI MARSALA-SW TRAPANI/
ELEV 40M AGL DUE TO CIV UNMANNED ACFT ACTIVITY