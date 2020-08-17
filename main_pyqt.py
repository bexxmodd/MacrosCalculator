from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('user_interface.ui', self)

        # Locate Exit button and link close method to it
        self.exit_button = self.findChild(QtWidgets.QPushButton, 'exit_button')
        self.print_button = self.findChild(QtWidgets.QPushButton, 'calculate_button')
        self.print_button.clicked.connect(self.printButtonPressed)
        self.exit_button.clicked.connect(lambda:self.close())

        # Read height from input
        self.height = self.findChild(QtWidgets.QLineEdit, 'height_input')

        self.show()

    def printButtonPressed(self):
        print('height is: ' + self.height.text())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()