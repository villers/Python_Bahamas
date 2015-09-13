import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from TChatApplicationClient import *

def main():
    app = QtWidgets.QApplication(sys.argv)
    myapp = TChatApplicationClient()
    myapp.show()
    app.exec()
    return 1

if __name__ == "__main__":
    sys.exit(main())
