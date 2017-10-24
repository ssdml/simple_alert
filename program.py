#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont
from datetime import datetime, timedelta
from time import sleep
import sys
from AlertWindow import AlertWindow
from Timer import Timer

def showWindow():
    app = QApplication(sys.argv)
    screenSize = app.primaryScreen().size()
    w = AlertWindow(screenSize)
    w.show()
    app.exec_()


if __name__ == '__main__':

    timer = Timer(timedelta(hours=1))

    while True:
        if timer.check():
            showWindow()
        sleep(5)

