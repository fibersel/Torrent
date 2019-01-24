#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import design
import bencode
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QMenu, QShortcut, QFileDialog
from PyQt5.QtGui import QIcon, QKeySequence

from tkinter import Tk
from tkinter.filedialog import askopenfilename


class Window(QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.actionAdd.triggered.connect(self.open_dialog)
        self.actionExit.triggered.connect(self.close)
        self.shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.shortcut.activated.connect(self.close)
    
    def open_dialog(self):
        name = QFileDialog.getOpenFileName(self, 'open ', "/home/fibersell/desktop", "Torrent Files (*.Torrent)")
        f = open(name[0], 'rb')
        bt = bencode.decode(f.read())
        f.close()
        print(bt.keys())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    GUI = Window()
    GUI.show()
    sys.exit(app.exec_())