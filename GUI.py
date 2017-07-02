# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys 
import create_xml; 
import MainProgram

class Music(QtGui.QMainWindow):

	def __init__(self):
		super(Music,self).__init__() 
		self.setGeometry(0,0,500,500)
		self.setWindowTitle("GrabMusic")
		self.setWindowIcon(QtGui.QIcon("icon.jpg"))
		self.setFixedSize(400,300)
		self.setupUi()

	def setupUi(self):

		addSong = QtGui.QPushButton("addSong",self)
		addSong.setGeometry(290, 20, 101, 28)
		addSong.clicked.connect(self.addSong)

		download = QtGui.QPushButton("download",self)
		download.setGeometry(290, 80, 101, 28)
		download.clicked.connect(self.download)

		self.songName = QtGui.QLineEdit("song",self)
		self.songName.setGeometry(10, 20, 241, 30)
		
		self.artist = QtGui.QLineEdit("artist",self)
		self.artist.setGeometry(10, 80, 241, 30)

		self.process = QtGui.QLineEdit("PROCESS",self)
		self.process.setGeometry(70, 180, 251, 78)

		self.show();

	def download(self): 
		self.process.setText("DOWNLOADING")
		MainProgram.download()
		self.process.setText("DOWNLOADED ALL SONG")

	def addSong(self):
		create_xml.addsongs(self.songName.text(), self.artist.text())
		self.process.setText("SONG ADDED: "+self.songName.text() +" - "+self.artist.text())
	
	def delSong(self):
		print(self.songName.text())
		create_xml.delSong(self.songName.text())
		self.process.setText("SONG DELETED: "+self.songName.text())
	
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ui = Music()
    sys.exit(app.exec_())
