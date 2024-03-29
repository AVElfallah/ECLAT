# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\oldData\project\dr.kazim\view\app_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import config.config as cf
from repos.functions import doECLAT, loadDataFromCSV




class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(479, 740)
                MainWindow.setMinimumSize(QtCore.QSize(479, 740))
                MainWindow.setMaximumSize(QtCore.QSize(479, 740))
                MainWindow.setStyleSheet("background-color:teal;")
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
                self.scrollArea.setGeometry(QtCore.QRect(9, 9, 461, 671))
                self.scrollArea.setMinimumSize(QtCore.QSize(461, 671))
                self.scrollArea.setWidgetResizable(True)
                self.scrollArea.setObjectName("scrollArea")
                self.scrollAreaWidgetContents = QtWidgets.QWidget()
                self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 459, 669))
                self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
                self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
                self.verticalLayout.setObjectName("verticalLayout")
                self.database_text = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.database_text.setMinimumSize(QtCore.QSize(161, 34))
                font = QtGui.QFont()
                font.setPointSize(-1)
                self.database_text.setFont(font)
                self.database_text.setStyleSheet("text-align:center;\n""font-size:18px;")
                self.database_text.setText("")
                self.database_text.setObjectName("database_text")
                self.verticalLayout.addWidget(self.database_text)
                self.load_database_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.load_database_button.sizePolicy().hasHeightForWidth())
                self.load_database_button.setSizePolicy(sizePolicy)
                self.load_database_button.setMinimumSize(QtCore.QSize(437, 51))
                self.load_database_button.setMaximumSize(QtCore.QSize(240, 51))
                self.load_database_button.setStyleSheet("background-color:balck;\n"
        "color:white;\n"
        "font-weight:bold;\n"
        "border-radius:25px;")
                self.load_database_button.setObjectName("load_database_button")
                self.verticalLayout.addWidget(self.load_database_button)
                self.container = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
                self.container.setMinimumSize(QtCore.QSize(431, 291))
                font = QtGui.QFont()
                font.setPointSize(16)
                font.setBold(True)
                font.setWeight(75)
                self.container.setFont(font)
                self.container.setTitle("")
                self.container.setObjectName("container")
                self.label = QtWidgets.QLabel(self.container)
                self.label.setGeometry(QtCore.QRect(10, 30, 251, 31))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setStyleSheet("color:white;\n"
        "font-size:20;\n"
        "font-weight:bold;")
                self.label.setObjectName("label")
                self.transaction_num = QtWidgets.QLabel(self.container)
                self.transaction_num.setGeometry(QtCore.QRect(260, 30, 161, 31))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.transaction_num.setFont(font)
                self.transaction_num.setStyleSheet("color:white;\n"
        "font-size:20;\n"
        "font-weight:bold;")
                self.transaction_num.setObjectName("transaction_num")
                self.label_2 = QtWidgets.QLabel(self.container)
                self.label_2.setGeometry(QtCore.QRect(120, 70, 181, 31))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_2.setFont(font)
                self.label_2.setStyleSheet("color:white;\n"
        "font-size:20;\n"
        "font-weight:bold;")
                self.label_2.setObjectName("label_2")
                self.mini_support = QtWidgets.QTextEdit(self.container)
                self.mini_support.setGeometry(QtCore.QRect(90, 180, 241, 31))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.mini_support.setFont(font)
                self.mini_support.setPlaceholderText("set minimum support")
                self.mini_support.setObjectName("mini_support")
                self.label_3 = QtWidgets.QLabel(self.container)
                self.label_3.setGeometry(QtCore.QRect(120, 140, 181, 31))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_3.setFont(font)
                self.label_3.setStyleSheet("color:white;\n"
        "font-size:20;\n"
        "font-weight:bold;")
                self.label_3.setObjectName("label_3")
                self.db_limit = QtWidgets.QTextEdit(self.container)
                self.db_limit.setGeometry(QtCore.QRect(90, 100, 241, 31))
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.db_limit.setFont(font)
                self.db_limit.setPlaceholderText("set limit")
                self.db_limit.setObjectName("db_limit")
                self.do_eclat = QtWidgets.QPushButton(self.container)
                self.do_eclat.setGeometry(QtCore.QRect(120, 230, 171, 51))
                self.do_eclat.setStyleSheet("background-color:balck;\n"
        "color:white;\n"
        "font-weight:bold;\n"
        "border-radius:25px;")
                self.do_eclat.setObjectName("do_eclat")
                self.verticalLayout.addWidget(self.container)
                self.res_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                font = QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.res_label.setFont(font)
                self.res_label.setStyleSheet("color:white;\n"
        "font-size:20;\n"
        "font-weight:bold;")
                self.container.hide();
                self.res_label.hide();
                self.res_label.setObjectName("res_label")
                self.verticalLayout.addWidget(self.res_label)
                self.listView = QtWidgets.QListWidget(self)
                self.listView.setObjectName("listView")
                self.verticalLayout.addWidget(self.listView)
                self.scrollArea.setWidget(self.scrollAreaWidgetContents)
                MainWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(MainWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 479, 21))
                self.menubar.setObjectName("menubar")
                MainWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
                self.listView.hide()
                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                        _translate = QtCore.QCoreApplication.translate
                        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                        self.load_database_button.setText(_translate("MainWindow", "Load Database .csv"))
                        self.label.setText(_translate("MainWindow", "Number of Transactions in db:"))
                        self.transaction_num.setText(_translate("MainWindow", "00000000"))
                        self.label_2.setText(_translate("MainWindow", "Set Transactions limit"))
                        self.label_3.setText(_translate("MainWindow", "Set Minimum Support"))
                        self.do_eclat.setText(_translate("MainWindow", "Run ECLAT Algorithm"))
                        self.res_label.setText(_translate("MainWindow", "Result OF ECLAT"))
        def setEvents(self,):
                ## open dialog to load database from csv file and save it to config
                def openDialogToLoadCSV():
                        ## check if file is loaded to change app visability
                        check=  loadDataFromCSV()
                        if(check):
                                ## display file name in ui
                                self.database_text.setText(cf.databaseFileName)
                                ## show container
                                self.container.show()
                                ## count database rows and display it to ui
                                self.transaction_num.setText(str(len(cf.dataList)))
                                ## show all
                                self.res_label.show()
                                self.listView.show()
                
                ## set event to button
                self.load_database_button.clicked.connect(openDialogToLoadCSV)
                ## do eclat algorithm function
                def doEc():
                        ## get database limit from ui
                        limits =int(self.db_limit.toPlainText())
                        ## get mini support form ui
                        mini =int(self.mini_support.toPlainText())
                        ## eclat 
                        doECLAT(limits=limits,mini=mini)
                        ## add items to list view
                        for i in cf.eclatReport:
                                self.listView.addItem(str(i))

                ## set event to button
                self.do_eclat.clicked.connect(doEc)
                
