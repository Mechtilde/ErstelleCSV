#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  ErstelleCSV.py
#  
#  Copyright 2013 Mechtilde Stehmann <ooo@mechtilde.de>
#  Copyright 2013 Johannes Spielmann <jps@shezi.de>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  any later version.
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

from tkinter import filedialog
from tkinter import *


class LineReplacer(object):
    """Replaces substrings in a list of strings."""

    def __init__(self, lines=None, replacements=None):
        
        if lines is None:
            lines = []
        if replacements is None:
            replacements = (
                ("‖", "\t\""),
                ("\t20", "\t\"\t20"),
                ("\t\t", "\t"),
                ("\t\t\"\t20", "\"\t20"),
            )
        
        self.lineslist = lines
        self.replacements = replacements

    def do_replacement(self):
        """Executes all replacements on all lines and returns the resulting list."""

        for oldstr, newstr in self.replacements:
            
            self.replaceStrings(oldstr, newstr)
            
        return self.lineslist
        

    def replaceStrings(self, oldstring, newstring):
        """Ersetzen der Zeichen"""
        i = 0 # Zähler für die Zeilen
        for line in self.lineslist:
            line = line.replace(oldstring, newstring)
            self.lineslist[i] = line
            i = i + 1

        return(self.lineslist)




class ErsetzenCSV(object):
	"""Ersetzt Strings durch andere und speichert in neuer Datei ab."""
	def __init__(self,filename):

		self.filename = filename
		self.fileOpenR()
		self.readLines()
		self.fileClose()

	def fileOpenR(self):
		self.fobj = open(self.filename, "r")
		"""Oeffnet eine Datei zum Lesen z.B. KeyIDLocalize20121126.sdf"""

	def fileClose(self):
		self.fobj.close()
		"""Schließt eine Datei"""

	def readLines(self):
		"""Lese zeilenweise aus"""
		# self.lineslist = [] # Leere Liste erzeugen
		# for line in self.fobj:
		# 	self.lineslist.append(line)
		"""Verwenung von redlines()"""
		self.lineslist = self.fobj.readlines()

		return(self.lineslist)

	def writeNewFile(self):
		filesplit = self.filename.split(".")
		newfilename = filesplit[0]+ "_New" + ".csv"
		self.fobj = open(newfilename, "w")
		# for line in self.lineslist:
		# 	self.fobj.write(line)
		self.fobj.writelines(self.lineslist)

class Dialog(object):
	"""Klasse, um den Dialog zu erstellen"""

	def __init__(self):
		dia = Tk()
		dia.title("SDF2CSV")
		lb = Label(dia,text = "Program transforms SDF into CSV")
		lb.grid(row=0, column=0)

	def fileOpenDialog(self):
		filename = filedialog.askopenfilename(filetypes = [('SDF-Files','*.sdf'),('all files','*.*')],title ="Suche nach *.sdf Dateien")
		if filename == "":
			filename = "XXX"
		return(filename)

#def main():
#	dia = Dialog()
#	filename = dia.fileOpenDialog()
#	if filename != "XXX":
#		escsv = ErsetzenCSV(filename)
#		escsv.replaceStrings("‖","\t\"")
#		escsv.replaceStrings("\t\t","\t")
#		escsv.replaceStrings("\t20","\t\"\t20")
#		escsv.replaceStrings("\t\t\"\t20","\"\t20")
#		escsv.writeNewFile()
#	return 0

if __name__ == '__main__':
	main()

