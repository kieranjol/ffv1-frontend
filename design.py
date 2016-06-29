# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kieranjol/cork/ffv1-gui/design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        MainWindow.resize(783, 424)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.dirname_text = QtGui.QLineEdit(self.centralwidget)
        self.dirname_text.setObjectName(_fromUtf8("dirname_text"))
        self.gridLayout.addWidget(self.dirname_text, 1, 1, 1, 1)
        self.container_selection = QtGui.QComboBox(self.centralwidget)
        self.container_selection.setObjectName(_fromUtf8("container_selection"))
        self.container_selection.addItem(_fromUtf8(""))
        self.container_selection.addItem(_fromUtf8(""))
        self.container_selection.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.container_selection, 4, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 8, 1, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout.addWidget(self.checkBox_2, 7, 0, 1, 1)
        self.btnBrowse = QtGui.QPushButton(self.centralwidget)
        self.btnBrowse.setObjectName(_fromUtf8("btnBrowse"))
        self.gridLayout.addWidget(self.btnBrowse, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 4, 0, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 6, 0, 1, 2)
        self.filename_text = QtGui.QLineEdit(self.centralwidget)
        self.filename_text.setMinimumSize(QtCore.QSize(450, 0))
        self.filename_text.setObjectName(_fromUtf8("filename_text"))
        self.gridLayout.addWidget(self.filename_text, 0, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 2, 1, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 783, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen_single_file = QtGui.QAction(MainWindow)
        self.actionOpen_single_file.setObjectName(_fromUtf8("actionOpen_single_file"))
        self.actionOpen_Directory_Batch = QtGui.QAction(MainWindow)
        self.actionOpen_Directory_Batch.setObjectName(_fromUtf8("actionOpen_Directory_Batch"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionOpen_single_file)
        self.menuFile.addAction(self.actionOpen_Directory_Batch)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "FFV1 Transcoder v0.1 - 2016", None))
        self.container_selection.setItemText(0, _translate("MainWindow", ".mkv", None))
        self.container_selection.setItemText(1, _translate("MainWindow", ".mov", None))
        self.container_selection.setItemText(2, _translate("MainWindow", ".avi", None))
        self.pushButton.setText(_translate("MainWindow", "Encode", None))
        self.checkBox_2.setText(_translate("MainWindow", "Generate whole file md5 manifest", None))
        self.btnBrowse.setText(_translate("MainWindow", "Select file (single input)", None))
        self.lineEdit.setText(_translate("MainWindow", "Select Container: (MKV by default)", None))
        self.checkBox.setText(_translate("MainWindow", "Disable Framemd5 Lossless Verification (Speed Increase - NOT RECOMMENDED)", None))
        self.pushButton_2.setText(_translate("MainWindow", "Select Directory Input (batch process)", None))
        self.pushButton_3.setText(_translate("MainWindow", "Select Output Directory (Sidecar by default)", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionOpen_single_file.setText(_translate("MainWindow", "Open Single File", None))
        self.actionOpen_Directory_Batch.setText(_translate("MainWindow", "Open Directory (Batch)", None))
        self.actionSettings.setText(_translate("MainWindow", "Settings", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

