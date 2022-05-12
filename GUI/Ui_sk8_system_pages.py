# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sk8_system_pages.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.resize(1328, 875)
        StackedWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        StackedWidget.setMouseTracking(True)
        StackedWidget.setTabletTracking(False)
        StackedWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        StackedWidget.setStyleSheet("")
        self.menu_page = QtWidgets.QWidget()
        self.menu_page.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.menu_page.setMouseTracking(True)
        self.menu_page.setStyleSheet("border-image: url(:/images/menu.JPG);")
        self.menu_page.setObjectName("menu_page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.menu_page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 248, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 248, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.btn1 = QtWidgets.QPushButton(self.menu_page)
        self.btn1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy)
        self.btn1.setMinimumSize(QtCore.QSize(0, 0))
        self.btn1.setMaximumSize(QtCore.QSize(500, 100))
        font = QtGui.QFont()
        font.setFamily("Gloucester MT Extra Condensed")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn1.setFont(font)
        self.btn1.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn1.setMouseTracking(True)
        self.btn1.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btn1.setToolTip("")
        self.btn1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn1.setAutoFillBackground(False)
        self.btn1.setStyleSheet("font: 28pt \"Gloucester MT Extra Condensed\";\n"
"border-image: url(:/images/btn.JPG);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.btn1.setObjectName("btn1")
        self.verticalLayout_5.addWidget(self.btn1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.btn2 = QtWidgets.QPushButton(self.menu_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy)
        self.btn2.setMaximumSize(QtCore.QSize(500, 100))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.btn2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Gloucester MT Extra Condensed")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn2.setFont(font)
        self.btn2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn2.setMouseTracking(True)
        self.btn2.setTabletTracking(True)
        self.btn2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btn2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn2.setAutoFillBackground(False)
        self.btn2.setStyleSheet("font: 28pt \"Gloucester MT Extra Condensed\";\n"
"border-image: url(:/images/btn.JPG);\n"
"color: rgb(0, 0, 0);")
        self.btn2.setObjectName("btn2")
        self.verticalLayout_5.addWidget(self.btn2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.btn3 = QtWidgets.QPushButton(self.menu_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy)
        self.btn3.setMaximumSize(QtCore.QSize(500, 100))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.btn3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Gloucester MT Extra Condensed")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn3.setFont(font)
        self.btn3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn3.setMouseTracking(True)
        self.btn3.setTabletTracking(True)
        self.btn3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btn3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn3.setAutoFillBackground(False)
        self.btn3.setStyleSheet("font: 28pt \"Gloucester MT Extra Condensed\";\n"
"border-image: url(:/images/btn.JPG);\n"
"color: rgb(0, 0, 0);")
        self.btn3.setObjectName("btn3")
        self.verticalLayout_5.addWidget(self.btn3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem7 = QtWidgets.QSpacerItem(338, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        StackedWidget.addWidget(self.menu_page)
        self.about_page = QtWidgets.QWidget()
        self.about_page.setMouseTracking(True)
        self.about_page.setStyleSheet("border-image: url(:/images/about.JPG);")
        self.about_page.setObjectName("about_page")
        self.gridLayout = QtWidgets.QGridLayout(self.about_page)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem9)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem10)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem12)
        self.btn4 = QtWidgets.QPushButton(self.about_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy)
        self.btn4.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn4.setMouseTracking(True)
        self.btn4.setTabletTracking(True)
        self.btn4.setStyleSheet("border-image: url(:/images/btn.JPG);\n"
"font: 28pt \"Gloucester MT Extra Condensed\";")
        self.btn4.setObjectName("btn4")
        self.horizontalLayout.addWidget(self.btn4)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem13)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem14)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem15)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        StackedWidget.addWidget(self.about_page)
        self.manual_page = QtWidgets.QWidget()
        self.manual_page.setStyleSheet("border-image: url(:/images/manual.JPG);")
        self.manual_page.setObjectName("manual_page")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.manual_page)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem16)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem17)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem18)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem19)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem20)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem21)
        self.btn6 = QtWidgets.QPushButton(self.manual_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn6.sizePolicy().hasHeightForWidth())
        self.btn6.setSizePolicy(sizePolicy)
        self.btn6.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn6.setMouseTracking(True)
        self.btn6.setTabletTracking(True)
        self.btn6.setStyleSheet("border-image: url(:/images/btn.JPG);\n"
"font: 28pt \"Gloucester MT Extra Condensed\";")
        self.btn6.setObjectName("btn6")
        self.horizontalLayout_5.addWidget(self.btn6)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem22)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem23)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem24)
        self.verticalLayout_8.addLayout(self.verticalLayout_9)
        self.verticalLayout_7.addLayout(self.verticalLayout_8)
        self.verticalLayout_6.addLayout(self.verticalLayout_7)
        self.gridLayout_6.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        StackedWidget.addWidget(self.manual_page)
        self.jude_page = QtWidgets.QWidget()
        self.jude_page.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.jude_page.setMouseTracking(False)
        self.jude_page.setTabletTracking(False)
        self.jude_page.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.jude_page.setStyleSheet("border-image: url(:/images/yuna.jpg);")
        self.jude_page.setObjectName("jude_page")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.jude_page)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.jude_page)
        self.label_2.setStyleSheet("border-image: url(:/images/blue1.PNG);\n"
"font: 22pt \"Gloucester MT Extra Condensed\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 5, 9, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_4.addItem(spacerItem25, 4, 11, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem26, 3, 11, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.jude_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setStyleSheet("border-image: url(:/images/JudgeTitle.PNG);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 1, 8, 3, 2)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem27, 18, 6, 1, 1)
        self.stop_btn = QtWidgets.QPushButton(self.jude_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_btn.sizePolicy().hasHeightForWidth())
        self.stop_btn.setSizePolicy(sizePolicy)
        self.stop_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stop_btn.setMouseTracking(True)
        self.stop_btn.setTabletTracking(True)
        self.stop_btn.setStyleSheet("border-image: url(:/images/orange.PNG);\n"
"font: 24pt \"Gloucester MT Extra Condensed\";")
        self.stop_btn.setObjectName("stop_btn")
        self.gridLayout_4.addWidget(self.stop_btn, 16, 6, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_4.addItem(spacerItem28, 0, 11, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_4.addItem(spacerItem29, 13, 11, 1, 1)
        spacerItem30 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_4.addItem(spacerItem30, 10, 11, 1, 1)
        self.mistake_bool = QtWidgets.QLineEdit(self.jude_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mistake_bool.sizePolicy().hasHeightForWidth())
        self.mistake_bool.setSizePolicy(sizePolicy)
        self.mistake_bool.setStyleSheet("border-image: url(:/images/displayInfoColor.PNG);\n"
"color: rgb(0, 0, 255);\n"
"font: 18pt \"Gloucester MT Extra Condensed\";")
        self.mistake_bool.setAlignment(QtCore.Qt.AlignCenter)
        self.mistake_bool.setObjectName("mistake_bool")
        self.gridLayout_4.addWidget(self.mistake_bool, 12, 9, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.jude_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("border-image: url(:/images/blue1.PNG);\n"
"font: 22pt \"Gloucester MT Extra Condensed\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 11, 9, 1, 1)
        spacerItem31 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_4.addItem(spacerItem31, 0, 3, 1, 1)
        self.num_of_turns = QtWidgets.QLineEdit(self.jude_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num_of_turns.sizePolicy().hasHeightForWidth())
        self.num_of_turns.setSizePolicy(sizePolicy)
        self.num_of_turns.setStyleSheet("border-image: url(:/images/displayInfoColor.PNG);\n"
"color: rgb(0, 0, 255);\n"
"font: 18pt \"Gloucester MT Extra Condensed\";")
        self.num_of_turns.setAlignment(QtCore.Qt.AlignCenter)
        self.num_of_turns.setObjectName("num_of_turns")
        self.gridLayout_4.addWidget(self.num_of_turns, 9, 9, 1, 1)
        self.jump_name = QtWidgets.QLineEdit(self.jude_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jump_name.sizePolicy().hasHeightForWidth())
        self.jump_name.setSizePolicy(sizePolicy)
        self.jump_name.setStyleSheet("border-image: url(:/images/displayInfoColor.PNG);\n"
"color: rgb(0, 0, 255);\n"
"font: 18pt \"Gloucester MT Extra Condensed\";")
        self.jump_name.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.jump_name.setAlignment(QtCore.Qt.AlignCenter)
        self.jump_name.setObjectName("jump_name")
        self.gridLayout_4.addWidget(self.jump_name, 6, 9, 1, 1)
        spacerItem32 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_4.addItem(spacerItem32, 7, 11, 1, 1)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem33, 5, 7, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.upload_btn = QtWidgets.QPushButton(self.jude_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upload_btn.sizePolicy().hasHeightForWidth())
        self.upload_btn.setSizePolicy(sizePolicy)
        self.upload_btn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.upload_btn.setMouseTracking(True)
        self.upload_btn.setTabletTracking(True)
        self.upload_btn.setStyleSheet("font: 26pt \"Gloucester MT Extra Condensed\";\n"
"border-image: url(:/images/yellow.PNG);")
        self.upload_btn.setObjectName("upload_btn")
        self.horizontalLayout_4.addWidget(self.upload_btn)
        spacerItem34 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem34)
        self.analysis_btn = QtWidgets.QPushButton(self.jude_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analysis_btn.sizePolicy().hasHeightForWidth())
        self.analysis_btn.setSizePolicy(sizePolicy)
        self.analysis_btn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.analysis_btn.setMouseTracking(True)
        self.analysis_btn.setTabletTracking(True)
        self.analysis_btn.setStyleSheet("font: 26pt \"Gloucester MT Extra Condensed\";\n"
"border-image: url(:/images/yellow.PNG);")
        self.analysis_btn.setObjectName("analysis_btn")
        self.horizontalLayout_4.addWidget(self.analysis_btn)
        spacerItem35 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem35)
        self.save_btn = QtWidgets.QPushButton(self.jude_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy)
        self.save_btn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.save_btn.setMouseTracking(True)
        self.save_btn.setTabletTracking(True)
        self.save_btn.setStyleSheet("font: 26pt \"Gloucester MT Extra Condensed\";\n"
"border-image: url(:/images/yellow.PNG);")
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_4.addWidget(self.save_btn)
        spacerItem36 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem36)
        self.audio_btn = QtWidgets.QPushButton(self.jude_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.audio_btn.sizePolicy().hasHeightForWidth())
        self.audio_btn.setSizePolicy(sizePolicy)
        self.audio_btn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.audio_btn.setMouseTracking(True)
        self.audio_btn.setTabletTracking(True)
        self.audio_btn.setStyleSheet("font: 26pt \"Gloucester MT Extra Condensed\";\n"
"border-image: url(:/images/yellow.PNG);")
        self.audio_btn.setObjectName("audio_btn")
        self.horizontalLayout_4.addWidget(self.audio_btn)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem37)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 1, 1, 1, 7)
        spacerItem38 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem38, 18, 1, 1, 1)
        self.vid_wget = QVideoWidget(self.jude_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vid_wget.sizePolicy().hasHeightForWidth())
        self.vid_wget.setSizePolicy(sizePolicy)
        self.vid_wget.setStyleSheet("border-image: url(:/images/black.PNG);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.vid_wget.setObjectName("vid_wget")
        self.gridLayout_4.addWidget(self.vid_wget, 2, 1, 14, 6)
        spacerItem39 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_4.addItem(spacerItem39, 19, 11, 1, 1)
        spacerItem40 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_4.addItem(spacerItem40, 19, 4, 1, 1)
        spacerItem41 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_4.addItem(spacerItem41, 17, 4, 1, 1)
        spacerItem42 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem42, 7, 8, 2, 1)
        spacerItem43 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem43, 7, 0, 2, 1)
        spacerItem44 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.gridLayout_4.addItem(spacerItem44, 16, 11, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.jude_page)
        self.label_6.setStyleSheet("border-image: url(:/images/blue1.PNG);\n"
"font: 22pt \"Gloucester MT Extra Condensed\";")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 17, 9, 1, 1)
        self.take_off_edge = QtWidgets.QLineEdit(self.jude_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.take_off_edge.sizePolicy().hasHeightForWidth())
        self.take_off_edge.setSizePolicy(sizePolicy)
        self.take_off_edge.setStyleSheet("border-image: url(:/images/displayInfoColor.PNG);\n"
"color: rgb(0, 0, 255);\n"
"font: 18pt \"Gloucester MT Extra Condensed\";")
        self.take_off_edge.setAlignment(QtCore.Qt.AlignCenter)
        self.take_off_edge.setObjectName("take_off_edge")
        self.gridLayout_4.addWidget(self.take_off_edge, 18, 9, 1, 1)
        self.take_off_foot = QtWidgets.QLineEdit(self.jude_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.take_off_foot.sizePolicy().hasHeightForWidth())
        self.take_off_foot.setSizePolicy(sizePolicy)
        self.take_off_foot.setStyleSheet("border-image: url(:/images/displayInfoColor.PNG);\n"
"color: rgb(0, 0, 255);\n"
"font: 18pt \"Gloucester MT Extra Condensed\";")
        self.take_off_foot.setAlignment(QtCore.Qt.AlignCenter)
        self.take_off_foot.setObjectName("take_off_foot")
        self.gridLayout_4.addWidget(self.take_off_foot, 15, 9, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.jude_page)
        self.label_5.setStyleSheet("border-image: url(:/images/blue1.PNG);\n"
"font: 22pt \"Gloucester MT Extra Condensed\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 14, 9, 1, 1)
        self.btn5 = QtWidgets.QPushButton(self.jude_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn5.sizePolicy().hasHeightForWidth())
        self.btn5.setSizePolicy(sizePolicy)
        self.btn5.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn5.setMouseTracking(True)
        self.btn5.setTabletTracking(True)
        self.btn5.setStyleSheet("border-image: url(:/images/btn.JPG);\n"
"font: 24pt \"Gloucester MT Extra Condensed\";")
        self.btn5.setObjectName("btn5")
        self.gridLayout_4.addWidget(self.btn5, 18, 3, 1, 1)
        spacerItem45 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem45, 16, 4, 1, 1)
        self.pause_btn = QtWidgets.QPushButton(self.jude_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pause_btn.sizePolicy().hasHeightForWidth())
        self.pause_btn.setSizePolicy(sizePolicy)
        self.pause_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pause_btn.setMouseTracking(True)
        self.pause_btn.setTabletTracking(True)
        self.pause_btn.setStyleSheet("border-image: url(:/images/orange.PNG);\n"
"font: 24pt \"Gloucester MT Extra Condensed\";")
        self.pause_btn.setObjectName("pause_btn")
        self.gridLayout_4.addWidget(self.pause_btn, 16, 3, 1, 1)
        spacerItem46 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem46, 16, 2, 1, 1)
        self.play_btn = QtWidgets.QPushButton(self.jude_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play_btn.sizePolicy().hasHeightForWidth())
        self.play_btn.setSizePolicy(sizePolicy)
        self.play_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.play_btn.setMouseTracking(True)
        self.play_btn.setTabletTracking(True)
        self.play_btn.setStyleSheet("border-image: url(:/images/orange.PNG);\n"
"font: 24pt \"Gloucester MT Extra Condensed\";")
        self.play_btn.setObjectName("play_btn")
        self.gridLayout_4.addWidget(self.play_btn, 16, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.jude_page)
        self.label_4.setStyleSheet("border-image: url(:/images/blue1.PNG);\n"
"font: 22pt \"Gloucester MT Extra Condensed\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 8, 9, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        StackedWidget.addWidget(self.jude_page)

        self.retranslateUi(StackedWidget)
        StackedWidget.setCurrentIndex(3)
        self.btn1.clicked.connect(StackedWidget.setFocus)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)

    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        StackedWidget.setWindowTitle(_translate("StackedWidget", "Figure_Skating_Judging_System"))
        self.btn1.setText(_translate("StackedWidget", "About"))
        self.btn2.setText(_translate("StackedWidget", "Manual"))
        self.btn3.setText(_translate("StackedWidget", "Judge"))
        self.btn4.setText(_translate("StackedWidget", "Back"))
        self.btn6.setText(_translate("StackedWidget", "Back"))
        self.label_2.setText(_translate("StackedWidget", "Jump Name"))
        self.stop_btn.setText(_translate("StackedWidget", "Stop"))
        self.mistake_bool.setText(_translate("StackedWidget", "N/A"))
        self.label_3.setText(_translate("StackedWidget", "Mistake"))
        self.num_of_turns.setText(_translate("StackedWidget", "N/A"))
        self.jump_name.setText(_translate("StackedWidget", "N/A"))
        self.upload_btn.setText(_translate("StackedWidget", "Upload"))
        self.analysis_btn.setText(_translate("StackedWidget", "Analysis"))
        self.save_btn.setText(_translate("StackedWidget", "Save"))
        self.audio_btn.setText(_translate("StackedWidget", "Audio Guide"))
        self.label_6.setText(_translate("StackedWidget", "Take-off Edge"))
        self.take_off_edge.setText(_translate("StackedWidget", "N/A"))
        self.take_off_foot.setText(_translate("StackedWidget", "N/A"))
        self.label_5.setText(_translate("StackedWidget", "Take-off Foot "))
        self.btn5.setText(_translate("StackedWidget", "Back"))
        self.pause_btn.setText(_translate("StackedWidget", "Pause"))
        self.play_btn.setText(_translate("StackedWidget", "Play"))
        self.label_4.setText(_translate("StackedWidget", "Number Of Turns"))

from PyQt5.QtMultimediaWidgets import QVideoWidget
import picture_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StackedWidget = QtWidgets.QStackedWidget()
    ui = Ui_StackedWidget()
    ui.setupUi(StackedWidget)
    StackedWidget.show()
    sys.exit(app.exec_())
