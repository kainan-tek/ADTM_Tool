# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(520, 280)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(520, 280))
        MainWindow.setMaximumSize(QSize(520, 280))
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.actionOpen_Log = QAction(MainWindow)
        self.actionOpen_Log.setObjectName(u"actionOpen_Log")
        self.actionOpen_Log.setFont(font)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionExit.setFont(font)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAbout.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 521, 241))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.tabWidget.setFont(font1)
        self.MainTab = QWidget()
        self.MainTab.setObjectName(u"MainTab")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.MainTab.setFont(font2)
        self.label = QLabel(self.MainTab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 51, 31))
        self.label.setFont(font2)
        self.logEdit = QLineEdit(self.MainTab)
        self.logEdit.setObjectName(u"logEdit")
        self.logEdit.setGeometry(QRect(70, 20, 331, 31))
        self.logEdit.setFont(font2)
        self.logEdit.setReadOnly(True)
        self.selectButton = QPushButton(self.MainTab)
        self.selectButton.setObjectName(u"selectButton")
        self.selectButton.setGeometry(QRect(420, 20, 71, 31))
        self.selectButton.setFont(font2)
        self.line = QFrame(self.MainTab)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 70, 521, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_2 = QLabel(self.MainTab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 100, 81, 31))
        self.label_2.setFont(font2)
        self.periodEdit = QLineEdit(self.MainTab)
        self.periodEdit.setObjectName(u"periodEdit")
        self.periodEdit.setGeometry(QRect(100, 100, 121, 31))
        self.periodEdit.setFont(font2)
        self.periodEdit.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.label_3 = QLabel(self.MainTab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(280, 100, 81, 31))
        self.label_3.setFont(font2)
        self.bufferEdit = QLineEdit(self.MainTab)
        self.bufferEdit.setObjectName(u"bufferEdit")
        self.bufferEdit.setGeometry(QRect(370, 100, 121, 31))
        self.bufferEdit.setFont(font2)
        self.label_4 = QLabel(self.MainTab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 160, 71, 31))
        self.label_4.setFont(font2)
        self.drawButton = QPushButton(self.MainTab)
        self.drawButton.setObjectName(u"drawButton")
        self.drawButton.setGeometry(QRect(420, 160, 71, 31))
        self.drawButton.setFont(font2)
        self.comboBox = QComboBox(self.MainTab)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(90, 160, 311, 31))
        self.comboBox.setFont(font2)
        self.tabWidget.addTab(self.MainTab, "")
        self.UserGuideTab = QWidget()
        self.UserGuideTab.setObjectName(u"UserGuideTab")
        self.tabWidget.addTab(self.UserGuideTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 520, 23))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuLogging = QMenu(self.menubar)
        self.menuLogging.setObjectName(u"menuLogging")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuLogging.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menuLogging.addAction(self.actionOpen_Log)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ADTM Tool", None))
        self.actionOpen_Log.setText(QCoreApplication.translate("MainWindow", u"Open Log", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Log File", None))
        self.selectButton.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Period Time", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Buffer Time", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Alsa Node", None))
        self.drawButton.setText(QCoreApplication.translate("MainWindow", u"Draw", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MainTab), QCoreApplication.translate("MainWindow", u"Main", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.UserGuideTab), QCoreApplication.translate("MainWindow", u"User Guide", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuLogging.setTitle(QCoreApplication.translate("MainWindow", u"Logging", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

