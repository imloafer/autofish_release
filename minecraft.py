# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'minecraft.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AutoFish(object):
    def setupUi(self, AutoFish):
        AutoFish.setObjectName("AutoFish")
        AutoFish.resize(554, 265)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/fishing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AutoFish.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(AutoFish)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gBox_color = QtWidgets.QGroupBox(self.centralwidget)
        self.gBox_color.setObjectName("gBox_color")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.gBox_color)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_red = QtWidgets.QLabel(self.gBox_color)
        self.label_red.setObjectName("label_red")
        self.verticalLayout.addWidget(self.label_red)
        self.label_green = QtWidgets.QLabel(self.gBox_color)
        self.label_green.setObjectName("label_green")
        self.verticalLayout.addWidget(self.label_green)
        self.label_blue = QtWidgets.QLabel(self.gBox_color)
        self.label_blue.setObjectName("label_blue")
        self.verticalLayout.addWidget(self.label_blue)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.spinBox_R1 = QtWidgets.QSpinBox(self.gBox_color)
        self.spinBox_R1.setMaximum(255)
        self.spinBox_R1.setProperty("value", 80)
        self.spinBox_R1.setObjectName("spinBox_R1")
        self.verticalLayout_2.addWidget(self.spinBox_R1)
        self.spinBox_G1 = QtWidgets.QSpinBox(self.gBox_color)
        self.spinBox_G1.setMaximum(255)
        self.spinBox_G1.setProperty("value", 10)
        self.spinBox_G1.setObjectName("spinBox_G1")
        self.verticalLayout_2.addWidget(self.spinBox_G1)
        self.spinBox_B1 = QtWidgets.QSpinBox(self.gBox_color)
        self.spinBox_B1.setMaximum(255)
        self.spinBox_B1.setProperty("value", 10)
        self.spinBox_B1.setObjectName("spinBox_B1")
        self.verticalLayout_2.addWidget(self.spinBox_B1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.gBox_color)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_5 = QtWidgets.QLabel(self.gBox_color)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.gBox_color)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.spinBox_R2 = QtWidgets.QSpinBox(self.gBox_color)
        self.spinBox_R2.setMaximum(255)
        self.spinBox_R2.setProperty("value", 90)
        self.spinBox_R2.setObjectName("spinBox_R2")
        self.verticalLayout_4.addWidget(self.spinBox_R2)
        self.spinBox_G2 = QtWidgets.QSpinBox(self.gBox_color)
        self.spinBox_G2.setMaximum(255)
        self.spinBox_G2.setProperty("value", 13)
        self.spinBox_G2.setObjectName("spinBox_G2")
        self.verticalLayout_4.addWidget(self.spinBox_G2)
        self.spinBox_B2 = QtWidgets.QSpinBox(self.gBox_color)
        self.spinBox_B2.setMaximum(255)
        self.spinBox_B2.setProperty("value", 13)
        self.spinBox_B2.setObjectName("spinBox_B2")
        self.verticalLayout_4.addWidget(self.spinBox_B2)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_8.addWidget(self.gBox_color)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_counter = QtWidgets.QLabel(self.centralwidget)
        self.label_counter.setObjectName("label_counter")
        self.horizontalLayout_4.addWidget(self.label_counter)
        self.lcd_counter = QtWidgets.QLCDNumber(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lcd_counter.setFont(font)
        self.lcd_counter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcd_counter.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcd_counter.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_counter.setObjectName("lcd_counter")
        self.horizontalLayout_4.addWidget(self.lcd_counter)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_ttl_time = QtWidgets.QLabel(self.centralwidget)
        self.label_ttl_time.setObjectName("label_ttl_time")
        self.horizontalLayout_5.addWidget(self.label_ttl_time)
        self.lcd_time = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_time.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcd_time.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcd_time.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_time.setObjectName("lcd_time")
        self.horizontalLayout_5.addWidget(self.lcd_time)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.NoButton)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.groupBox_pic = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_pic.setObjectName("groupBox_pic")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_pic)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_picture = QtWidgets.QLabel(self.groupBox_pic)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_picture.sizePolicy().hasHeightForWidth())
        self.label_picture.setSizePolicy(sizePolicy)
        self.label_picture.setMinimumSize(QtCore.QSize(256, 128))
        self.label_picture.setMaximumSize(QtCore.QSize(256, 128))
        self.label_picture.setText("")
        self.label_picture.setObjectName("label_picture")
        self.verticalLayout_6.addWidget(self.label_picture)
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_pic)
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(99)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setPageStep(100)
        self.horizontalSlider.setProperty("value", 50)
        self.horizontalSlider.setSliderPosition(50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_6.addWidget(self.horizontalSlider)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalSlider = QtWidgets.QSlider(self.groupBox_pic)
        self.verticalSlider.setMaximum(99)
        self.verticalSlider.setPageStep(100)
        self.verticalSlider.setProperty("value", 50)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.horizontalLayout_3.addWidget(self.verticalSlider)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6.addWidget(self.groupBox_pic)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        AutoFish.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AutoFish)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menuHelp.setFont(font)
        self.menuHelp.setObjectName("menuHelp")
        AutoFish.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AutoFish)
        self.statusbar.setObjectName("statusbar")
        AutoFish.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(AutoFish)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.actionAbout.setFont(font)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHow = QtWidgets.QAction(AutoFish)
        self.actionHow.setCheckable(True)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.actionHow.setFont(font)
        self.actionHow.setObjectName("actionHow")
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionHow)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(AutoFish)
        QtCore.QMetaObject.connectSlotsByName(AutoFish)

    def retranslateUi(self, AutoFish):
        _translate = QtCore.QCoreApplication.translate
        AutoFish.setWindowTitle(_translate("AutoFish", "Auto-fishing for Minecraft"))
        self.gBox_color.setTitle(_translate("AutoFish", "Color Range"))
        self.label_red.setText(_translate("AutoFish", "red range:"))
        self.label_green.setText(_translate("AutoFish", "green range:"))
        self.label_blue.setText(_translate("AutoFish", "blue range:"))
        self.label.setText(_translate("AutoFish", "-"))
        self.label_5.setText(_translate("AutoFish", "-"))
        self.label_6.setText(_translate("AutoFish", "-"))
        self.label_counter.setText(_translate("AutoFish", "Total times:"))
        self.label_ttl_time.setText(_translate("AutoFish", "Total time elapse:"))
        self.groupBox_pic.setTitle(_translate("AutoFish", "Snapshot preview"))
        self.menuHelp.setTitle(_translate("AutoFish", "Help"))
        self.actionAbout.setText(_translate("AutoFish", "About"))
        self.actionHow.setText(_translate("AutoFish", "Always on Top"))
import minecraft_rc
