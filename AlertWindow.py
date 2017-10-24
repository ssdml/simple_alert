#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QFont

class AlertWindow(QWidget):

    width = 250
    height = 150

    def __init__(self, screenSize):
        super().__init__()
        self.initUI(screenSize)

    def initUI(self, screenSize):

        self.resize(self.width, self.height)
        self.move(screenSize.width() - self.width, screenSize.height() - self.height - 50)

        self.setWindowTitle('Перерыв')

        font = QFont("Calibri", 14, QFont.Bold) 

        self.lbl = QLabel(self)
        self.lbl.resize(self.width, self.height)
        self.lbl.setText('<center>Необходимо<br> сделать<br> перерыв</center>')

        self.lbl.setFont(font)
        
        
        
        
