#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QDesktopWidget
from PyQt5.QtGui import QFont
from Timer import Timer
from datetime import timedelta
from time import sleep

class AlertWindow(QWidget):

    width = 250
    height = 150

    def __init__(self, inputMinutes):
        super().__init__()
        sizeObject = QDesktopWidget().screenGeometry(-1)
        self.initUI(sizeObject)
        self.timer = Timer(timedelta(minutes=inputMinutes))
        self.beginWait()



    def initUI(self, screenSize):

        self.resize(self.width, self.height)
        self.move(screenSize.width() - self.width, screenSize.height() - self.height - 50)
        self.setWindowTitle('Перерыв')
        self.setStyleSheet("background-color: #f16d95")

        self.font = QFont("Calibri", 14, QFont.Bold) 
        self.initLabel()
        self.initButton()

    def initLabel(self):

        self.lbl = QLabel(self)
        self.lbl.resize(self.width, int(self.height / 2))
        self.lbl.setText('<center>Необходимо<br> сделать<br> перерыв</center>')

        self.lbl.setFont(self.font)

    def initButton(self):
        self.btn = QPushButton(self)
        self.btn.setText("Перерыв")
        self.btn.setFont(self.font)
        self.btn.resize(self.width - 40, 30)
        self.btn.move(20, int(self.height / 2 + 10))
        self.btn.setStyleSheet("background-color: #f13c73")
        self.btn.clicked.connect(self.beginWait)

    def beginWait(self):
        self.hide()
        self.timer.beginTimer()
        while True:
            if self.timer.check():
                self.show()
                return
            sleep(5)
        
        
        
        
