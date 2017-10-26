#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont
from datetime import datetime, timedelta
import sys
from AlertWindow import AlertWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    w = AlertWindow(60)
    sys.exit(app.exec_())
