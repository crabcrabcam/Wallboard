import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from MainDes import Ui_MainWindow
import webbrowser

class MainWindow(QtWidgets.QWidget, Ui_MainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)
        self.setupUi(self)
        self.btnOpenFile.clicked.connect(self.open_file)
        self.btnSaveFile.clicked.connect(self.save_file)
        self.btnSendEmail.clicked.connect(self.send_email)
        self.btnClear.clicked.connect(self.clear_text)

        self.btnClear.move(200, 200)


    def open_file(self):
        #Need the underscore apparently.
        name, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        if name != "":
            file = open(name, 'r')

            with file:
                text = file.read()
                self.txtEditMain.setText(text)

    def save_file(self):
        #Always need an _ with QFileDialog getters it seems
        name, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')
        if name != "":
            file = open(name, 'w')
            #Convert to plain text
            text = self.txtEditMain.toPlainText()
            file.write(text)
            file.close()

    def send_email(self):
        webbrowser.open(('mailto:?subject=From_The_Wallboard&body=%s' % self.txtEditMain.toPlainText()), new=1)
        pass

    def clear_text(self):
        #Create a messagebox with options
        choice = QtWidgets.QMessageBox.question(self, "Are you sure", "", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        #What's the option picked?
        if choice == QtWidgets.QMessageBox.Yes:
            #Close the app
            self.txtEditMain.clear()
        else:
            pass


#Launch the main section of the app
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
