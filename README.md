[![Social](https://img.shields.io/badge/Twitter-W0x404-blue.svg?style=flat-square)](http://www.twitter.com/W0x404)

# SQLmap_GUI
![Version](https://img.shields.io/badge/Version-0.2-lightgrey.svg?style=flat-square) 
Gui for SQLmap tool ( python 2.7, Tkinter, only for Linux )

Help you to start a terminal with the right options. You keep using SQLmap in CLI but you start the tool easily & fastly.

*Save time. Keep the control.*

# How to Install ?

* Change the pass of sqlmap in the right line. You can directly use sqlmap instead python /path/to/sqlmap.py.

* Install tkinter if not yet : `sudo apt-get install python-tk` (**python 3**: `sudo apt-get install python3-tk`)

* If you got the import error, change this:

|Python 2|Python 3|
|-------|-----------|
|Tkinter          |tkinter|
|Tix             |tkinter.tix|
|ttk             |tkinter.ttk|
|tkMessageBox    |tkinter.messagebox|
|tkColorChooser  |tkinter.colorchooser|
|tkFileDialog    |tkinter.filedialog|
|tkCommonDialog  |tkinter.commondialog|
|tkSimpleDialog  |tkinter.simpledialog|
|tkFont          |tkinter.font|
|Tkdnd           |tkinter.dnd|
|ScrolledText    |tkinter.scrolledtext|

* Run the .py
