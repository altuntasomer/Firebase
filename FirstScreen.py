# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_screen.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
import pyrebase
from docxtpl import DocxTemplate

import Database
import Jobs
from pathlib import Path

class Ui_MainWindow(object):



    def __init__(self, config):

        self.database = Database.Database(config)
        self.jobs_collection = self.database.getChildData("Jobs")
        self.user_collection = self.database.getChildData("Users")
        self.joblist = list()
        self.jobIndexList = list()



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

        self.comboBox_user = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_user.setObjectName("comboBox_user")
        self.verticalLayout_3.addWidget(self.comboBox_user)
        self.dateEdit_start = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_start.setObjectName("dateEdit_start")
        self.dateEdit_start.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit_start.setCalendarPopup(True)
        self.verticalLayout_3.addWidget(self.dateEdit_start)
        self.dateEdit_end = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_end.setObjectName("dateEdit_end")
        self.dateEdit_end.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit_end.setCalendarPopup(True)
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
        self.pixmaps = [self.pixmap1, self.pixmap2, self.pixmap3, self.pixmap4]

        MainWindow.setStatusBar(self.statusbar)



        self.listWidget.itemClicked.connect(self.listwidgetclicked)
        self.pushButton.clicked.connect(self.report)
        self.search.clicked.connect(self.filter)
        self.download_image.clicked.connect(self.show_file)
        self.list()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search.setText(_translate("MainWindow", "Bul"))
        self.pushButton.setText(_translate("MainWindow", "Rapor"))
        self.download_image.setText(_translate("MainWindow", "Fotoğrafları Yükle"))
        self.comboBox_user.addItem("Tümü")
        self.comboBox_user.addItem("Hüseyin ALTUNTAŞ")
        self.comboBox_user.addItem("Şevket ŞAHİN")
        self.comboBox_user.addItem("Hasan UYAR")
        self.comboBox_user.addItem("Hüseyin ER")
        self.comboBox_user.addItem("Fatih GÖKTAŞ")
        self.comboBox_user.addItem("Aydın İMRAK")
        self.comboBox_user.addItem("Murat TAMKOÇ")
        self.comboBox_user.addItem("Gökçin KÜÇÜKGÖKSU")
        self.comboBox_user.addItem("Ahmet AKDEMİR")
        self.comboBox_user.addItem("Kemal KARACAKAYA")


    def listwidgetclicked(self, item):

        self.selectedItem = self.listWidget.selectedIndexes()[0].row()
        job = self.joblist[self.jobIndexList[self.selectedItem]]
        self.description.setText(job.get_single_info("description"))
        self.place.setText(job.get_single_info("place"))
        self.time.setText(job.get_single_info("date"))
        self.user.setText(job.get_single_info("username")),

    def list(self):
        j = 0
        for i in self.jobs_collection:
            if type(i) is dict:

                self.joblist.append(Jobs.Jobs(i, self.user_collection[int(i["user_id"])]["name"], self.user_collection[int(i["user_id"])]["campus"]))
                self.jobIndexList.append(j)
                j+=1

        for i in self.jobIndexList:
            self.listWidget.addItem(self.joblist[i].get_single_info("description"))

    def filter(self):

        start_date = self.dateEdit_start.date().toPyDate()
        end_date = self.dateEdit_end.date().toPyDate()
        start_date = datetime.datetime(start_date.year, start_date.month, start_date.day)
        end_date = datetime.datetime(end_date.year, end_date.month, end_date.day)
        user = self.comboBox_user.currentIndex()
        self.jobIndexList.clear()
        j = 0
        for i in self.joblist:

            date = datetime.datetime.strptime(i.get_single_info("date"), "%d.%m.%Y,%H:%M")
            if date >= start_date and date <= end_date :
                self.jobIndexList.append(j)

            j += 1

        self.listWidget.clear()
        for i in self.jobIndexList:
            print(i)
            self.listWidget.addItem(self.joblist[i].get_single_info("description"))

    def report(self):
        size = len(self.jobIndexList)
        j = 0
        #doc = DocxTemplate('/home/omer/Desktop/sablona.docx')
        for i in self.jobIndexList:
            print(str(j), ' / ', str(size))
            contex = self.joblist[i].report()
            path = self.joblist[i].get_filepath('r') + ".docx"
            Path(path).mkdir(parents=True, exist_ok=True)
            j+=1
            print(path)
            #doc.render(contex)
            #doc.save(path)

    def show_file(self):
        job = self.joblist[self.jobIndexList[self.selectedItem]]
        path = job.get_filepath('f')
        self.database.downloadImage(path)
        for i in range(0,4):
            try:
                pathT = path + "/" + str(i) + ".jpg"
                print(pathT)
                self.pixmaps[i].setPixmap(QtGui.QPixmap(pathT).scaled(200, 200, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation))
            except Exception as e:
                print(e)
