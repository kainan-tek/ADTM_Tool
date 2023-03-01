# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guide.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QTextEdit, QWidget)

class Ui_UserGuide(object):
    def setupUi(self, UserGuide):
        if not UserGuide.objectName():
            UserGuide.setObjectName(u"UserGuide")
        UserGuide.resize(381, 151)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UserGuide.sizePolicy().hasHeightForWidth())
        UserGuide.setSizePolicy(sizePolicy)
        UserGuide.setMinimumSize(QSize(381, 151))
        UserGuide.setMaximumSize(QSize(381, 151))
        font = QFont()
        font.setPointSize(10)
        UserGuide.setFont(font)
        self.guideTextEdit = QTextEdit(UserGuide)
        self.guideTextEdit.setObjectName(u"guideTextEdit")
        self.guideTextEdit.setGeometry(QRect(0, 0, 381, 151))
        sizePolicy.setHeightForWidth(self.guideTextEdit.sizePolicy().hasHeightForWidth())
        self.guideTextEdit.setSizePolicy(sizePolicy)
        self.guideTextEdit.setFont(font)
        self.guideTextEdit.setStyleSheet(u"background-color: rgb(231, 234, 237);")
        self.guideTextEdit.setReadOnly(True)

        self.retranslateUi(UserGuide)

        QMetaObject.connectSlotsByName(UserGuide)
    # setupUi

    def retranslateUi(self, UserGuide):
        UserGuide.setWindowTitle(QCoreApplication.translate("UserGuide", u"User Guide", None))
    # retranslateUi

