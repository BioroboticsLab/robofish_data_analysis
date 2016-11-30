from gui.visualizer import Visualizer

import sys
from PyQt4 import QtCore, QtGui



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainwin = Visualizer()
    mainwin.show()
    sys.exit(app.exec_())