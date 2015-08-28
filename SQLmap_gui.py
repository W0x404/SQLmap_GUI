#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  SQLmap_gui.py
#  
#  Copyright 2015 W. Twitter : < @W0x404 >
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from Tkinter import * 
from tkMessageBox import *
import os

def main():
	
	def set_option():
		query = 'python /home/anonymous/Documents/SECU/sqlmap/sqlmap.py ' + tor_var.get() + "-u '" + website.get() +"' "+ dump_var.get() + dbs_var.get() + tables_var.get() + random_var.get() + threads_var.get() + users_var.get() + passwords_var.get()
		os.system('xterm -sb -e "%s|less" ' % (query) )
		
	#tkinter windows
	fenetre = Tk()
	fenetre.title = "SLQMap GUI"
	
	# frame address
	FrameAddress = LabelFrame(fenetre, text="Field", borderwidth=2, relief=GROOVE)
	FrameAddress.pack(side=LEFT, padx=30, pady=30)

	# frame option
	FrameOption = LabelFrame(fenetre, text="Options", borderwidth=2, relief=GROOVE)
	FrameOption.pack(side=LEFT, padx=10, pady=10)
	
	# frame website
	FrameWebsite = LabelFrame(FrameAddress, text="Website adress*", borderwidth=2, relief=GROOVE)
	FrameWebsite.pack(padx=10, pady=10)
	
	# frame database
	FrameDatabase = LabelFrame(FrameAddress, text="Database Name", borderwidth=2, relief=GROOVE)
	FrameDatabase.pack(padx=10, pady=10)
	
	# frame tables
	FrameTables = LabelFrame(FrameAddress, text="Table Name", borderwidth=2, relief=GROOVE)
	FrameTables.pack(padx=10, pady=10)
	
	#website field
	website_var = StringVar() 
	website_var.set("")
	website = Entry(FrameWebsite, textvariable=website_var, width=30)
	website.pack()
	
	#database field
	database_var = StringVar() 
	database_var.set("")
	database = Entry(FrameDatabase, textvariable=database_var, width=30)
	database.pack()
	
	#tables field
	tables_var = StringVar() 
	tables_var.set("")
	tables = Entry(FrameTables, textvariable=tables_var, width=30)
	tables.pack()
	
	#tor field
	tor_var = StringVar()
	tor_checkbox = Checkbutton(FrameOption, text="tor", variable=tor_var, onvalue=" --tor --tor-type=SOCKS5 ")
	tor_checkbox.pack()
	
	#dump field
	dump_var = StringVar()
	dump_checkbox = Checkbutton(FrameOption, text="dump", variable=dump_var, onvalue=" --dump ", offvalue="")
	dump_checkbox.pack()
	
	#dbs field
	dbs_var = StringVar()
	dbs_checkbox = Checkbutton(FrameOption, text="dbs", variable=dbs_var, onvalue=" --dbs ", offvalue="")
	dbs_checkbox.pack()
	
	#tables field
	tables_var = StringVar()
	tables_checkbox = Checkbutton(FrameOption, text="tables", variable=tables_var, onvalue=" --tables ", offvalue="")
	tables_checkbox.pack()
	
	#random field
	random_var = StringVar()
	random_checkbox = Checkbutton(FrameOption, text="random", variable=random_var, onvalue=" --random-agent ", offvalue="")
	random_checkbox.pack()
	
	#threads field
	threads_var = StringVar()
	threads_checkbox = Checkbutton(FrameOption, text="threads", variable=threads_var, onvalue=" --threads 10", offvalue="")
	threads_checkbox.pack()
	
	#users field
	users_var = StringVar()
	users_checkbox = Checkbutton(FrameOption, text="users", variable=users_var, onvalue=" --users", offvalue="")
	users_checkbox.pack()
	
	#passwords field
	passwords_var = StringVar()
	passwords_checkbox = Checkbutton(FrameOption, text="passwords", variable=passwords_var, onvalue=" --passwords", offvalue="")
	passwords_checkbox.pack()
	

	#engine start
	bouton = Button(FrameAddress, text="Start", command=set_option)
	bouton.pack()
	
	
	fenetre.mainloop()
	return 0

if __name__ == '__main__':
	main()
