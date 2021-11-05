import sys
import types
import Jobs
import pyrebase
import json
import FirstScreen
from PyQt5.QtWidgets import QApplication, QMainWindow

firebase_config = {
        #project keys

        "serviceAccount": "serviceAccountKey.json"
        }



app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = FirstScreen.Ui_MainWindow(firebase_config)
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())