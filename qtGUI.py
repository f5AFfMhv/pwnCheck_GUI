# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './pwnCheck.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(481, 320)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(481, 320))
        MainWindow.setMaximumSize(QtCore.QSize(481, 320))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 481, 321))
        self.tabWidget.setToolTip(_fromUtf8(""))
        self.tabWidget.setStyleSheet(_fromUtf8("Log\n"
"color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:0.19397 rgba(0, 0, 0, 255), stop:0.202312 rgba(122, 97, 0, 255), stop:0.495514 rgba(76, 58, 0, 255), stop:0.504819 rgba(255, 255, 255, 255), stop:0.79 rgba(255, 255, 255, 255), stop:1 rgba(255, 158, 158, 255));\n"
"color: rgb(174, 255, 239);\n"
"font: 75 italic 9pt \"Noto Sans\";"))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.mainTab = QtGui.QWidget()
        self.mainTab.setObjectName(_fromUtf8("mainTab"))
        self.checkButton = QtGui.QPushButton(self.mainTab)
        self.checkButton.setGeometry(QtCore.QRect(380, 150, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkButton.setFont(font)
        self.checkButton.setObjectName(_fromUtf8("checkButton"))
        self.resultLabel = QtGui.QLabel(self.mainTab)
        self.resultLabel.setGeometry(QtCore.QRect(10, 190, 451, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier 10 Pitch"))
        font.setPointSize(10)
        self.resultLabel.setFont(font)
        self.resultLabel.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.resultLabel.setAutoFillBackground(True)
        self.resultLabel.setStyleSheet(_fromUtf8(""))
        self.resultLabel.setFrameShape(QtGui.QFrame.Panel)
        self.resultLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.resultLabel.setText(_fromUtf8(""))
        self.resultLabel.setTextFormat(QtCore.Qt.RichText)
        self.resultLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.resultLabel.setWordWrap(True)
        self.resultLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.resultLabel.setObjectName(_fromUtf8("resultLabel"))
        self.infoLabel = QtGui.QLabel(self.mainTab)
        self.infoLabel.setGeometry(QtCore.QRect(10, 10, 451, 131))
        self.infoLabel.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.infoLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.infoLabel.setObjectName(_fromUtf8("infoLabel"))
        self.passwordLineEdit = QtGui.QLineEdit(self.mainTab)
        self.passwordLineEdit.setGeometry(QtCore.QRect(10, 150, 361, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.passwordLineEdit.setAutoFillBackground(False)
        self.passwordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordLineEdit.setReadOnly(False)
        self.passwordLineEdit.setObjectName(_fromUtf8("passwordLineEdit"))
        self.tabWidget.addTab(self.mainTab, _fromUtf8(""))
        self.aboutTab = QtGui.QWidget()
        self.aboutTab.setObjectName(_fromUtf8("aboutTab"))
        self.aboutScrollArea = QtGui.QScrollArea(self.aboutTab)
        self.aboutScrollArea.setGeometry(QtCore.QRect(0, 0, 481, 291))
        self.aboutScrollArea.setWidgetResizable(True)
        self.aboutScrollArea.setObjectName(_fromUtf8("aboutScrollArea"))
        self.aboutScroll = QtGui.QWidget()
        self.aboutScroll.setGeometry(QtCore.QRect(0, 0, 466, 551))
        self.aboutScroll.setObjectName(_fromUtf8("aboutScroll"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.aboutScroll)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.aboutLabel = QtGui.QLabel(self.aboutScroll)
        self.aboutLabel.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.aboutLabel.setMouseTracking(True)
        self.aboutLabel.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.aboutLabel.setAutoFillBackground(True)
        self.aboutLabel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.aboutLabel.setLineWidth(1)
        self.aboutLabel.setTextFormat(QtCore.Qt.RichText)
        self.aboutLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.aboutLabel.setWordWrap(True)
        self.aboutLabel.setIndent(-1)
        self.aboutLabel.setOpenExternalLinks(False)
        self.aboutLabel.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.aboutLabel.setObjectName(_fromUtf8("aboutLabel"))
        self.horizontalLayout.addWidget(self.aboutLabel)
        self.aboutScrollArea.setWidget(self.aboutScroll)
        self.tabWidget.addTab(self.aboutTab, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.checkButton, self.tabWidget)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "pwnCheck", None))
        self.tabWidget.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\">Log</p></body></html>", None))
        self.checkButton.setText(_translate("MainWindow", "Check", None))
        self.infoLabel.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">How this program works:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:296;\">1. SHA1 hash calculated of  a password.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:296;\">2. Prefix variable is set to first 5 symbols of a hash.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:296;\">3. All hashes with matching prefix are pulled from </span><span style=\" font-weight:296; font-style:italic;\">pwnedpasswords.com </span><span style=\" font-weight:296;\">DB.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:296;\">4. Password hash match checked </span><span style=\" font-weight:600;\">localy</span><span style=\" font-weight:296;\"> on users PC.</span></p></body></html>", None))
        self.passwordLineEdit.setPlaceholderText(_translate("MainWindow", "Enter password", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainTab), _translate("MainWindow", "Main", None))
        self.aboutLabel.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">VERSION</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Version: 1.0</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Build date: 2019-03-28</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">DESCRIPTION</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This program is a graphical user interface for checking pwned passwords, it\'s writen with <span style=\" font-weight:600;\">python</span> and <span style=\" font-weight:600;\">pyQT4</span>. Program calculates password hash and then searches for matches with first 5 symbols (prefix) in <span style=\" font-style:italic;\">https://api.pwnedpasswords.com</span>, then full hash match is found localy on users PC.</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">CONTACTS</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copyright (C) 2019 Martynas J. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">f5AFfMhv@protonmail.com </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">https://github.com/f5AFfMhv</p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">LICENSE</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">pwnCheck</span> is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. <span style=\" font-weight:600;\">pwnCheck</span> is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with <span style=\" font-weight:600;\">pwnCheck</span>. If not, see &lt;https://www.gnu.org/licenses/&gt;.</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aboutTab), _translate("MainWindow", "About", None))

