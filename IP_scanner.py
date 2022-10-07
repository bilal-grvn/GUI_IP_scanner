# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IP_scanner.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_IP_scan(object):
    def setupUi(self, MainWindow_IP_scan):
        MainWindow_IP_scan.setObjectName("MainWindow_IP_scan")
        MainWindow_IP_scan.resize(540, 370)
        MainWindow_IP_scan.setMinimumSize(QtCore.QSize(540, 370))
        MainWindow_IP_scan.setMaximumSize(QtCore.QSize(540, 370))
        self.centralwidget = QtWidgets.QWidget(MainWindow_IP_scan)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 521, 341))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(10, 10, 270, 320))
        self.frame.setMinimumSize(QtCore.QSize(270, 320))
        self.frame.setMaximumSize(QtCore.QSize(270, 320))
        self.frame.setObjectName("frame")
        self.tableWidget_IP_list = QtWidgets.QTableWidget(self.frame)
        self.tableWidget_IP_list.setGeometry(QtCore.QRect(10, 10, 250, 300))
        self.tableWidget_IP_list.setMinimumSize(QtCore.QSize(250, 300))
        self.tableWidget_IP_list.setMaximumSize(QtCore.QSize(250, 300))
        self.tableWidget_IP_list.setStyleSheet("border-radius: 6px;    \n"
"background-color: rgb(93, 93, 154);\n"
"color: #FFFFFF;\n"
"")
        self.tableWidget_IP_list.setObjectName("tableWidget_IP_list")
        self.tableWidget_IP_list.setColumnCount(1)
        self.tableWidget_IP_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_IP_list.setHorizontalHeaderItem(0, item)
        self.frame1 = QtWidgets.QFrame(self.frame_2)
        self.frame1.setGeometry(QtCore.QRect(280, 10, 231, 321))
        self.frame1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 211, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(50, 0))
        self.label_4.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.lineEdit_myIP = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_myIP.setStyleSheet("border-radius: 6px;    \n"
"background-color: rgb(93, 93, 154);\n"
"color: #FFFFFF;\n"
"")
        self.lineEdit_myIP.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_myIP.setObjectName("lineEdit_myIP")
        self.gridLayout.addWidget(self.lineEdit_myIP, 5, 1, 1, 4)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(50, 0))
        self.label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 7, 0, 1, 1)
        self.lineEdit_total_IP = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_total_IP.setStyleSheet("border-radius: 6px;    \n"
"background-color: rgb(93, 93, 154);\n"
"color: #FFFFFF;\n"
"")
        self.lineEdit_total_IP.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_total_IP.setObjectName("lineEdit_total_IP")
        self.gridLayout.addWidget(self.lineEdit_total_IP, 7, 1, 1, 4)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit_no_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_no_2.setMaximumSize(QtCore.QSize(33, 16777215))
        self.lineEdit_no_2.setStyleSheet("border-radius: 6px;    \n"
"background-color: rgb(93, 93, 154);\n"
"color: #FFFFFF;\n"
"")
        self.lineEdit_no_2.setText("")
        self.lineEdit_no_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_no_2.setObjectName("lineEdit_no_2")
        self.gridLayout.addWidget(self.lineEdit_no_2, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(50, 0))
        self.label_3.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.lineEdit_no_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_no_1.setMaximumSize(QtCore.QSize(33, 16777215))
        self.lineEdit_no_1.setStyleSheet("border-radius: 6px;    \n"
"background-color: rgb(93, 93, 154);\n"
"color: #FFFFFF;\n"
"")
        self.lineEdit_no_1.setText("")
        self.lineEdit_no_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_no_1.setObjectName("lineEdit_no_1")
        self.gridLayout.addWidget(self.lineEdit_no_1, 0, 1, 1, 1)
        self.lineEdit_no_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_no_3.setMaximumSize(QtCore.QSize(33, 16777215))
        self.lineEdit_no_3.setStyleSheet("border-radius: 6px;    \n"
"background-color: rgb(93, 93, 154);\n"
"color: #FFFFFF;\n"
"")
        self.lineEdit_no_3.setText("")
        self.lineEdit_no_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_no_3.setObjectName("lineEdit_no_3")
        self.gridLayout.addWidget(self.lineEdit_no_3, 0, 3, 1, 1)
        self.radioButton_window = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_window.setObjectName("radioButton_window")
        self.gridLayout.addWidget(self.radioButton_window, 3, 0, 1, 5)
        self.lineEdit_host = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_host.setStyleSheet("border-radius: 6px;    \n"
"background-color: rgb(93, 93, 154);\n"
"color: #FFFFFF;\n"
"")
        self.lineEdit_host.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_host.setObjectName("lineEdit_host")
        self.gridLayout.addWidget(self.lineEdit_host, 6, 1, 1, 4)
        self.radioButton_ubuntu = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_ubuntu.setChecked(False)
        self.radioButton_ubuntu.setObjectName("radioButton_ubuntu")
        self.gridLayout.addWidget(self.radioButton_ubuntu, 4, 0, 1, 5)
        self.lineEdit_no_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_no_4.setMaximumSize(QtCore.QSize(33, 16777215))
        self.lineEdit_no_4.setStyleSheet("border-radius: 6px;    \n"
"background-color: rgb(93, 93, 154);\n"
"color: #FFFFFF;\n"
"")
        self.lineEdit_no_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_no_4.setReadOnly(True)
        self.lineEdit_no_4.setObjectName("lineEdit_no_4")
        self.gridLayout.addWidget(self.lineEdit_no_4, 0, 4, 1, 1)
        self.lineEdit_uyari = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_uyari.setMinimumSize(QtCore.QSize(160, 50))
        self.lineEdit_uyari.setMaximumSize(QtCore.QSize(500, 40))
        self.lineEdit_uyari.setStyleSheet("border-radius: 6px;    \n"
"background-color: rgb(93, 93, 154);\n"
"color: #FFFFFF;\n"
"")
        self.lineEdit_uyari.setText("")
        self.lineEdit_uyari.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_uyari.setReadOnly(True)
        self.lineEdit_uyari.setObjectName("lineEdit_uyari")
        self.gridLayout.addWidget(self.lineEdit_uyari, 2, 0, 1, 5)
        self.pushButton_scan = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_scan.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_scan.setMaximumSize(QtCore.QSize(500, 16777215))
        self.pushButton_scan.setStyleSheet("border-radius: 6px;    \n"
"background-color: rgb(85, 170, 255);\n"
"color: #FFFFFF;\n"
"")
        self.pushButton_scan.setObjectName("pushButton_scan")
        self.gridLayout.addWidget(self.pushButton_scan, 1, 0, 1, 3)
        self.pushButton_exit = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_exit.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_exit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.pushButton_exit.setStyleSheet("border-radius: 6px;    \n"
"color: #FFFFFF;\n"
"background-color: rgb(164, 0, 0);\n"
"")
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.gridLayout.addWidget(self.pushButton_exit, 1, 3, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 350, 521, 16))
        font = QtGui.QFont()
        font.setFamily("Sarai")
        font.setItalic(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(93, 93, 154);\n"
"color: #FFFFFF;")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        MainWindow_IP_scan.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_IP_scan)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_IP_scan)

    def retranslateUi(self, MainWindow_IP_scan):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_IP_scan.setWindowTitle(_translate("MainWindow_IP_scan", "MainWindow"))
        item = self.tableWidget_IP_list.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow_IP_scan", "IP Number"))
        self.label_4.setText(_translate("MainWindow_IP_scan", "Host"))
        self.label.setText(_translate("MainWindow_IP_scan", "Total IP"))
        self.label_5.setText(_translate("MainWindow_IP_scan", "<html><head/><body><p align=\"justify\">Search</p></body></html>"))
        self.label_3.setText(_translate("MainWindow_IP_scan", "<html><head/><body><p align=\"justify\">My IP</p></body></html>"))
        self.radioButton_window.setText(_translate("MainWindow_IP_scan", "For WINDOW"))
        self.radioButton_ubuntu.setText(_translate("MainWindow_IP_scan", "For UBUNTU"))
        self.lineEdit_no_4.setText(_translate("MainWindow_IP_scan", "0"))
        self.pushButton_scan.setText(_translate("MainWindow_IP_scan", "SCAN"))
        self.pushButton_exit.setText(_translate("MainWindow_IP_scan", "EXIT"))
        self.label_2.setText(_translate("MainWindow_IP_scan", "@ By Bilal GUREVIN   "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_IP_scan = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_IP_scan()
    ui.setupUi(MainWindow_IP_scan)
    MainWindow_IP_scan.show()
    sys.exit(app.exec_())
