# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
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
        MainWindow.resize(1153, 798)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, -50, 501, 541))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 490, 487, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.playBtn = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.playBtn.setMinimumSize(QtCore.QSize(78, 32))
        self.playBtn.setObjectName(_fromUtf8("playBtn"))
        self.horizontalLayout_2.addWidget(self.playBtn)
        self.backBtn = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.backBtn.setObjectName(_fromUtf8("backBtn"))
        self.horizontalLayout_2.addWidget(self.backBtn)
        self.nextBtn = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.nextBtn.setObjectName(_fromUtf8("nextBtn"))
        self.horizontalLayout_2.addWidget(self.nextBtn)
        self.label_14 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_2.addWidget(self.label_14)
        self.stepSize = QtGui.QSpinBox(self.horizontalLayoutWidget_2)
        self.stepSize.setMinimum(1)
        self.stepSize.setMaximum(99)
        self.stepSize.setProperty("value", 1)
        self.stepSize.setObjectName(_fromUtf8("stepSize"))
        self.horizontalLayout_2.addWidget(self.stepSize)
        self.frameID = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.frameID.setObjectName(_fromUtf8("frameID"))
        self.horizontalLayout_2.addWidget(self.frameID)
        self.sptBtn = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.sptBtn.setObjectName(_fromUtf8("sptBtn"))
        self.horizontalLayout_2.addWidget(self.sptBtn)
        self.verticalLayoutWidget = QtGui.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 481, 431))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.showVideo = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.showVideo.sizePolicy().hasHeightForWidth())
        self.showVideo.setSizePolicy(sizePolicy)
        self.showVideo.setText(_fromUtf8(""))
        self.showVideo.setObjectName(_fromUtf8("showVideo"))
        self.verticalLayout.addWidget(self.showVideo)
        self.playerSlider = QtGui.QSlider(self.verticalLayoutWidget)
        self.playerSlider.setOrientation(QtCore.Qt.Horizontal)
        self.playerSlider.setObjectName(_fromUtf8("playerSlider"))
        self.verticalLayout.addWidget(self.playerSlider)
        self.drawTabWidget = QtGui.QTabWidget(self.centralwidget)
        self.drawTabWidget.setGeometry(QtCore.QRect(20, 510, 391, 231))
        self.drawTabWidget.setObjectName(_fromUtf8("drawTabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.formLayoutWidget_2 = QtGui.QWidget(self.tab)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 251, 91))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.gridLayout = QtGui.QGridLayout(self.formLayoutWidget_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.fishFormComboBox = QtGui.QComboBox(self.formLayoutWidget_2)
        self.fishFormComboBox.setObjectName(_fromUtf8("fishFormComboBox"))
        self.fishFormComboBox.addItem(_fromUtf8(""))
        self.fishFormComboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.fishFormComboBox, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.formLayoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.showID_CheckBox = QtGui.QCheckBox(self.formLayoutWidget_2)
        self.showID_CheckBox.setText(_fromUtf8(""))
        self.showID_CheckBox.setObjectName(_fromUtf8("showID_CheckBox"))
        self.gridLayout.addWidget(self.showID_CheckBox, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.trackerVersion = QtGui.QComboBox(self.formLayoutWidget_2)
        self.trackerVersion.setObjectName(_fromUtf8("trackerVersion"))
        self.trackerVersion.addItem(_fromUtf8(""))
        self.trackerVersion.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.trackerVersion, 2, 2, 1, 1)
        self.drawTabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.fishList = QtGui.QListWidget(self.tab_2)
        self.fishList.setGeometry(QtCore.QRect(10, 0, 191, 121))
        self.fishList.setObjectName(_fromUtf8("fishList"))
        self.label_test = QtGui.QLabel(self.tab_2)
        self.label_test.setGeometry(QtCore.QRect(260, 40, 81, 61))
        self.label_test.setObjectName(_fromUtf8("label_test"))
        self.changeColorBtn = QtGui.QPushButton(self.tab_2)
        self.changeColorBtn.setGeometry(QtCore.QRect(250, 20, 110, 32))
        self.changeColorBtn.setObjectName(_fromUtf8("changeColorBtn"))
        self.drawTabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(580, -20, 511, 511))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.widget = QtGui.QWidget(self.groupBox_2)
        self.widget.setGeometry(QtCore.QRect(10, 30, 491, 471))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(430, 530, 206, 80))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.analyseComboBox = QtGui.QComboBox(self.formLayoutWidget)
        self.analyseComboBox.setObjectName(_fromUtf8("analyseComboBox"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.analyseComboBox)
        self.showPlotBtn = QtGui.QPushButton(self.formLayoutWidget)
        self.showPlotBtn.setObjectName(_fromUtf8("showPlotBtn"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.showPlotBtn)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.analyse_widget = QtGui.QWidget(self.centralwidget)
        self.analyse_widget.setGeometry(QtCore.QRect(670, 530, 221, 131))
        self.analyse_widget.setObjectName(_fromUtf8("analyse_widget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1153, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoadCsv = QtGui.QAction(MainWindow)
        self.actionLoadCsv.setObjectName(_fromUtf8("actionLoadCsv"))
        self.actionLoadVideo = QtGui.QAction(MainWindow)
        self.actionLoadVideo.setObjectName(_fromUtf8("actionLoadVideo"))
        self.actionLoadAnalyseResult = QtGui.QAction(MainWindow)
        self.actionLoadAnalyseResult.setObjectName(_fromUtf8("actionLoadAnalyseResult"))
        self.menuFile.addAction(self.actionLoadCsv)
        self.menuFile.addAction(self.actionLoadVideo)
        self.menuFile.addAction(self.actionLoadAnalyseResult)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.drawTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox", None))
        self.playBtn.setText(_translate("MainWindow", "Pause", None))
        self.backBtn.setText(_translate("MainWindow", "<", None))
        self.nextBtn.setText(_translate("MainWindow", ">", None))
        self.label_14.setText(_translate("MainWindow", "step size", None))
        self.frameID.setText(_translate("MainWindow", "ID", None))
        self.sptBtn.setText(_translate("MainWindow", "Switch", None))
        self.fishFormComboBox.setItemText(0, _translate("MainWindow", "thin", None))
        self.fishFormComboBox.setItemText(1, _translate("MainWindow", "fat", None))
        self.label.setText(_translate("MainWindow", "Fish Form", None))
        self.label_2.setText(_translate("MainWindow", "Show ID", None))
        self.label_3.setText(_translate("MainWindow", "Tracker Version", None))
        self.trackerVersion.setItemText(0, _translate("MainWindow", "old", None))
        self.trackerVersion.setItemText(1, _translate("MainWindow", "latest", None))
        self.drawTabWidget.setTabText(self.drawTabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1", None))
        self.label_test.setText(_translate("MainWindow", "Color", None))
        self.changeColorBtn.setText(_translate("MainWindow", "Change Color", None))
        self.drawTabWidget.setTabText(self.drawTabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox", None))
        self.label_4.setText(_translate("MainWindow", "Analyse:", None))
        self.showPlotBtn.setText(_translate("MainWindow", "False", None))
        self.label_5.setText(_translate("MainWindow", "ShowPlot:", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionLoadCsv.setText(_translate("MainWindow", "LoadCsv", None))
        self.actionLoadVideo.setText(_translate("MainWindow", "LoadVideo", None))
        self.actionLoadAnalyseResult.setText(_translate("MainWindow", "LoadAnalyseResult", None))

