# SQLmap_GUI
[BETA] Gui for SQLmap tool ( python 2., Tkinter, only for Linux )

# How to Install ?

x Change the pass of sqlmap in the right line. You can directly use sqlmap instead python /path/to/sqlmap.py.

x Install tkinter if not yet : sudo apt-get install python-tk (python 3: sudo apt-get install python3-tk)

x If you got the import error, change this:
Python 2             Python 3
Tkinter         →  tkinter
Tix             →  tkinter.tix
ttk             →  tkinter.ttk
tkMessageBox    →  tkinter.messagebox
tkColorChooser  →  tkinter.colorchooser
tkFileDialog    →  tkinter.filedialog
tkCommonDialog  →  tkinter.commondialog
tkSimpleDialog  →  tkinter.simpledialog
tkFont          →  tkinter.font
Tkdnd           →  tkinter.dnd
ScrolledText    →  tkinter.scrolledtext

x Run the .py
