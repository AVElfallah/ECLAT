# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QListView,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(479, 740)
        MainWindow.setMinimumSize(QSize(479, 740))
        MainWindow.setMaximumSize(QSize(479, 740))
        MainWindow.setStyleSheet(u"background-color:teal;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(9, 9, 461, 671))
        self.scrollArea.setMinimumSize(QSize(461, 671))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 459, 669))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.database_text = QLabel(self.scrollAreaWidgetContents)
        self.database_text.setObjectName(u"database_text")
        self.database_text.setMinimumSize(QSize(161, 34))
        font = QFont()
        self.database_text.setFont(font)
        self.database_text.setStyleSheet(u"text-align:center;\n"
"font-size:18px;")

        self.verticalLayout.addWidget(self.database_text)

        self.load_database_button = QPushButton(self.scrollAreaWidgetContents)
        self.load_database_button.setObjectName(u"load_database_button")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_database_button.sizePolicy().hasHeightForWidth())
        self.load_database_button.setSizePolicy(sizePolicy)
        self.load_database_button.setMinimumSize(QSize(437, 51))
        self.load_database_button.setMaximumSize(QSize(240, 51))
        self.load_database_button.setStyleSheet(u"background-color:balck;\n"
"color:white;\n"
"font-weight:bold;\n"
"border-radius:25px;")

        self.verticalLayout.addWidget(self.load_database_button)

        self.container = QGroupBox(self.scrollAreaWidgetContents)
        self.container.setObjectName(u"container")
        self.container.setMinimumSize(QSize(431, 291))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.container.setFont(font1)
        self.label = QLabel(self.container)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 251, 31))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color:white;\n"
"font-size:20;\n"
"font-weight:bold;")
        self.transaction_num = QLabel(self.container)
        self.transaction_num.setObjectName(u"transaction_num")
        self.transaction_num.setGeometry(QRect(260, 30, 161, 31))
        self.transaction_num.setFont(font2)
        self.transaction_num.setStyleSheet(u"color:white;\n"
"font-size:20;\n"
"font-weight:bold;")
        self.label_2 = QLabel(self.container)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 70, 181, 31))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color:white;\n"
"font-size:20;\n"
"font-weight:bold;")
        self.mini_support = QTextEdit(self.container)
        self.mini_support.setObjectName(u"mini_support")
        self.mini_support.setGeometry(QRect(90, 180, 241, 31))
        self.mini_support.setFont(font2)
        self.mini_support.setPlaceholderText(u"set minimum support")
        self.label_3 = QLabel(self.container)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 140, 181, 31))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color:white;\n"
"font-size:20;\n"
"font-weight:bold;")
        self.db_limit = QTextEdit(self.container)
        self.db_limit.setObjectName(u"db_limit")
        self.db_limit.setGeometry(QRect(90, 100, 241, 31))
        self.db_limit.setFont(font2)
        self.db_limit.setPlaceholderText(u"set limit")
        self.do_eclat = QPushButton(self.container)
        self.do_eclat.setObjectName(u"do_eclat")
        self.do_eclat.setGeometry(QRect(120, 230, 171, 51))
        self.do_eclat.setStyleSheet(u"background-color:balck;\n"
"color:white;\n"
"font-weight:bold;\n"
"border-radius:25px;")

        self.verticalLayout.addWidget(self.container)

        self.res_label = QLabel(self.scrollAreaWidgetContents)
        self.res_label.setObjectName(u"res_label")
        self.res_label.setFont(font2)
        self.res_label.setStyleSheet(u"color:white;\n"
"font-size:20;\n"
"font-weight:bold;")

        self.verticalLayout.addWidget(self.res_label)

        self.listView = QListView(self.scrollAreaWidgetContents)
        self.listView.setObjectName(u"listView")

        self.verticalLayout.addWidget(self.listView)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 479, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.database_text.setText("")
        self.load_database_button.setText(QCoreApplication.translate("MainWindow", u"Load Database .csv", None))
        self.container.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Number of Transactions in db:", None))
        self.transaction_num.setText(QCoreApplication.translate("MainWindow", u"00000000", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Set Transactions limit", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Set Minimum Support", None))
        self.do_eclat.setText(QCoreApplication.translate("MainWindow", u"Run ECLAT Algorithm", None))
        self.res_label.setText(QCoreApplication.translate("MainWindow", u"Result OF ECLAT", None))
    # retranslateUi

