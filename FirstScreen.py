# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_screen.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pyrebase
import Database
import Jobs

class Ui_MainWindow(object):



    def __init__(self, config):

        self.database = Database.Database(config)
        self.jobs_collection = self.database.getChildData("Jobs")
        self.user_collection = self.database.getChildData("Users")
        self.joblist = list()



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1179, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.comboBox_campus = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_campus.setObjectName("comboBox_campus")
        self.verticalLayout_3.addWidget(self.comboBox_campus)
        self.comboBox_user = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_user.setObjectName("comboBox_user")
        self.verticalLayout_3.addWidget(self.comboBox_user)
        self.dateEdit_start = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_start.setObjectName("dateEdit_start")
        self.verticalLayout_3.addWidget(self.dateEdit_start)
        self.dateEdit_end = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_end.setObjectName("dateEdit_end")
        self.verticalLayout_3.addWidget(self.dateEdit_end)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setObjectName("search")
        self.horizontalLayout_4.addWidget(self.search)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_4.addWidget(self.listWidget)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pixmap1 = QtWidgets.QLabel(self.centralwidget)
        self.pixmap1.setText("")
        self.pixmap1.setObjectName("pixmap1")
        self.horizontalLayout_3.addWidget(self.pixmap1)
        self.pixmap2 = QtWidgets.QLabel(self.centralwidget)
        self.pixmap2.setObjectName("pixmap2")
        self.horizontalLayout_3.addWidget(self.pixmap2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pixmap3 = QtWidgets.QLabel(self.centralwidget)
        self.pixmap3.setObjectName("pixmap3")
        self.horizontalLayout_2.addWidget(self.pixmap3)
        self.pixmap4 = QtWidgets.QLabel(self.centralwidget)
        self.pixmap4.setObjectName("pixmap4")
        self.horizontalLayout_2.addWidget(self.pixmap4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.download_image = QtWidgets.QPushButton(self.centralwidget)
        self.download_image.setObjectName("download_image")
        self.verticalLayout_2.addWidget(self.download_image)
        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setObjectName("description")
        self.verticalLayout_2.addWidget(self.description)
        self.place = QtWidgets.QLabel(self.centralwidget)
        self.place.setObjectName("place")
        self.verticalLayout_2.addWidget(self.place)
        self.time = QtWidgets.QLabel(self.centralwidget)
        self.time.setObjectName("time")
        self.verticalLayout_2.addWidget(self.time)
        self.user = QtWidgets.QLabel(self.centralwidget)
        self.user.setText("")
        self.user.setObjectName("user")
        self.verticalLayout_2.addWidget(self.user)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1179, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.listWidget.itemClicked.connect(self.listwidgetclicked)

        self.list()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search.setText(_translate("MainWindow", "Bul"))
        self.pushButton.setText(_translate("MainWindow", "Rapor"))

        self.download_image.setText(_translate("MainWindow", "Fotoğrafları Yükle"))


    def listwidgetclicked(self, item):

        self.selectedItem = self.listWidget.selectedIndexes()[0].row()
        job = self.joblist[self.selectedItem]
        self.description.setText(job.get_single_info("description"))
        self.place.setText(job.get_single_info("place"))
        self.time.setText(job.get_single_info("date"))
        self.user.setText(job.get_single_info("username")),

    def list(self):

        for i in self.jobs_collection:
            if type(i) is dict:

                self.joblist.append(Jobs.Jobs(i, self.user_collection[int(i["user_id"])]["name"]))

        for i in self.joblist:
            self.listWidget.addItem(i.get_single_info("description"))
