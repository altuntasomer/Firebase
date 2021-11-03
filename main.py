import sys
import types
import Jobs
import pyrebase
import json
import FirstScreen
from PyQt5 import QtCore, QtGui, QtWidgets
firebase_config = {
        #add api here
        "serviceAccount": "serviceAccountKey.json"
        }



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = FirstScreen.Ui_MainWindow(firebase_config)
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())