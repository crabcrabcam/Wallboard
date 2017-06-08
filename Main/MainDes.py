# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(515, 435)
        self.verticalLayout = QtWidgets.QVBoxLayout(MainWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnOpenFile = QtWidgets.QPushButton(MainWindow)
        self.btnOpenFile.setObjectName("btnOpenFile")
        self.horizontalLayout.addWidget(self.btnOpenFile)
        self.btnSaveFile = QtWidgets.QPushButton(MainWindow)
        self.btnSaveFile.setObjectName("btnSaveFile")
        self.horizontalLayout.addWidget(self.btnSaveFile)
        self.btnSendEmail = QtWidgets.QPushButton(MainWindow)
        self.btnSendEmail.setObjectName("btnSendEmail")
        self.horizontalLayout.addWidget(self.btnSendEmail)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.txtEditMain = QtWidgets.QTextEdit(MainWindow)
        self.txtEditMain.setObjectName("txtEditMain")
        self.verticalLayout.addWidget(self.txtEditMain)
        self.btnClear = QtWidgets.QPushButton(MainWindow)
        self.btnClear.setObjectName("btnClear")
        self.verticalLayout.addWidget(self.btnClear)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wallboard"))
        self.btnOpenFile.setText(_translate("MainWindow", "Open File"))
        self.btnSaveFile.setText(_translate("MainWindow", "Save to File"))
        self.btnSendEmail.setText(_translate("MainWindow", "Send Email"))
        self.btnClear.setText(_translate("MainWindow", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

