# -*- coding: utf-8 -*-

from win32con import SW_HIDE
from win32file import GetDriveType
from win32api import GetEnvironmentVariable, GetLogicalDriveStrings, WinExec
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
import ui.FrameRemover as FRemover
from time import strftime
from os import walk, unlink, path
from sys import argv, exit
import ui.QRCremover

class Remover(FRemover.Ui_MainWindow):
    def __init__(self, parent=None):
        self.app = QtWidgets.QApplication( argv )
        FRemover.Ui_MainWindow.__init__( self )

        self.ComSpec = GetEnvironmentVariable('ComSpec')
        self.Disk = GetLogicalDriveStrings()
        self.IndexDrives = []
        self.TextLogs = ''
        self.currentSelected = None
        self.Disks = self.EvtRefreshAmovible()
        self.EventsUI()

        FRemover.Ui_MainWindow.show(self)

        exit( self.app.exec_() )

    def EventsUI(self):
        self.btn_opendriver.clicked.connect( self.EvtOpenDrive )
        self.btn_refresh.clicked.connect( self.EvtRefreshAmovible )
        self.btn_openlogs.clicked.connect( self.EvtOpenLogs )
        self.btn_clean.clicked.connect( self.EvtCleanAmovible )
        self.comboBox_drives.currentIndexChanged[ 'QString' ]\
            .connect(lambda : self.EvtIndexChanged( self.comboBox_drives.currentIndex() ))

    @pyqtSlot()
    def EvtRefreshAmovible(self):
        SplitDisk, j = None, 0
        self.Disk = GetLogicalDriveStrings()
        self.comboBox_drives.clear()
        if isinstance(self.Disk, str):
            SplitDisk = self.Disk.split('\\\x00')
            self.Disks = SplitDisk #['C:', 'D:', 'E:', 'F:', 'G:', '']
            for i in self.Disks:
                self.setComboContent(j, i)
                j += 1
            self.currentSelected = SplitDisk[0]
            del SplitDisk
        else: return self.RefreshAmovible()

    def setComboContent(self, j, i=None):
        if i is not None and i is not '':
            self.comboBox_drives.addItem("")
            self.comboBox_drives.setItemText(j, "Lecteur "+str(i))
            self.IndexDrives.append([j, i])

    @pyqtSlot()
    def EvtOpenDrive(self):
        for k in self.IndexDrives:
            if k[0] == self.comboBox_drives.currentIndex():
                WinExec('Explorer '+str(k[1]))
        del k

    @pyqtSlot()
    def EvtOpenLogs(self):
        WinExec(self.ComSpec+" /c dir "+self.currentSelected+"\ > "+self.currentSelected+"\Resultat.txt",SW_HIDE)
        ret = QtWidgets.QMessageBox.information(self, "Confirmation",
            '''Voulez-vous voir un aperçu sur le contenu de votre Flash disk ?''', QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Cancel)

        if ret == QtWidgets.QMessageBox.Ok:
            WinExec("Explorer "+self.currentSelected+"\Resultat.txt", SW_HIDE)
        else:
            pass

    @pyqtSlot()
    def EvtIndexChanged(self, Disq):
        if isinstance(Disq, int):
            for k in self.IndexDrives:
                if k[0] == self.comboBox_drives.currentIndex():
                    self.currentSelected = k[1]

    @pyqtSlot()
    def EvtCleanAmovible(self):
        global ListVirus
        if GetDriveType(self.currentSelected) == 2:
            WinExec(self.ComSpec+" /c attrib -s -h -r "+self.currentSelected+"\*.* /D /S", SW_HIDE)
            for root, dirs, files in walk(self.currentSelected+"/"):
                for file in files:
                    f = file.split('.')
                    if len(f) > 1:
                        if f[1].upper() == "LNK":
                            unlink(root+"\\"+file)

            for Virus in ListVirus:
                if path.exists(self.currentSelected + "\\"+Virus):
                    WinExec(self.ComSpec+" /C cd \ & del " + self.currentSelected + "\\" + Virus + "/f /q /a", SW_HIDE)
                    self.TextLogs += strftime("%H:%M:%S")+" [Clean]    Les Virus "+Virus+" ont ètè supprimè avec succés\n"
                    self.TextEditlogs.setPlainText(self.TextLogs)

            self.TextLogs += strftime("%H:%M:%S")+" [Clean]    FlashDisk nettoyée avec succés\n"
            self.TextEditlogs.setPlainText(self.TextLogs)
        else:
            self.TextLogs += strftime("%H:%M:%S")+" [Clean]    Ceci n'est pas Votre Clé USB Personnelle!\n"
            self.TextEditlogs.setPlainText(self.TextLogs)

if __name__ == "__main__":
    __author__ = 'Finel'
    ListVirus = ["ntde1ect.com","semo2x.exe","avpo.exe","ntdelect.com.txt","ntdeiect.com","amvo.exe",
                "rtlip.exe","x.exe","ert.dll","help.exe","copy.exe"]

    Rm = Remover()
