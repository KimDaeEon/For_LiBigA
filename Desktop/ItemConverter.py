import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic
import win32com.client

form_class = uic.loadUiType("ItemConverter.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__() 
        self.setupUi(self)
        self.connect(self.pushButton, SIGNAL("clicked()"), self.btn_clicked)
        self.inCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")

    def btn_clicked(self):
        text = self.lineEdit.text()
        name = self.inCpCodeMgr.CodeToName(text)
        self.label.setText(name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()