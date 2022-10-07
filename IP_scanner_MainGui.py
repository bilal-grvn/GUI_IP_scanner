from PyQt5.QtWidgets import *
from IP_scanner import *
import time
from subprocess import Popen
import os
import sys
import socket

class AnaPencere(QtWidgets.QMainWindow, Ui_MainWindow_IP_scan):

    def __init__(self, parent=None):

        super(AnaPencere, self).__init__(parent=parent)

        if True: 
            self.anapencere = Ui_MainWindow_IP_scan()
            self.anapencere.setupUi(self)
            self.ubuntu = self.anapencere.radioButton_ubuntu.isChecked()
            self.window = self.anapencere.radioButton_ubuntu.isChecked()

            self.anapencere.tableWidget_IP_list.setColumnWidth(0, 250)
            self.anapencere.tableWidget_IP_list.setColumnWidth(1, 60)
            self.anapencere.pushButton_exit.clicked.connect(self.exit_ap)
            self.anapencere.pushButton_scan.clicked.connect(self.IP_listing)

            self.anapencere.radioButton_ubuntu.toggled.connect(self.os_select)
            self.anapencere.radioButton_window.toggled.connect(self.os_select)


    def exit_ap(self):
        try:
            self.close()
        except Exception as e:
            print("programi_kapat ERROR", "")
        pass

    def os_select(self):
        try:
            rb = self.sender()
            if rb.isChecked():
                if rb.text() == "For UBUNTU":
                    self.ubuntu = True
                else:
                    self.ubuntu = False

                if rb.text() == "For WINDOW":
                    self.window = True
                else:
                    self.window = False

        except Exception as e:
            print("os_select ERROR", "")
        pass

    def IP_listing(self):
        try:
            self.hostname()
            if self.ubuntu:
                devnull = open(os.devnull, 'wb')
                no_1 = self.anapencere.lineEdit_no_1.text()
                no_2 = self.anapencere.lineEdit_no_2.text()
                no_3 = self.anapencere.lineEdit_no_3.text()

                #ip_araligi_deger = ("192.168."+no_1)
                ip_araligi_deger = (no_1 +"."+ no_2 +"."+ no_3)

                if no_1 == "" or no_2 == "" or no_3 == "":
                    uyari_1 = "missing IP"
                    print(uyari_1)
                    self.anapencere.lineEdit_uyari.setText(uyari_1)
                else:
                    list = []
                    p = []
                    aktif = 0
                    yanit_yok = 0
                    pasif = 0
                    for aralik in range(0, 255):
                        ip = ip_araligi_deger + ".%d" % aralik
                        p.append((ip, Popen(['ping', '-c', '3', ip], stdout=devnull)))
                    while p:
                        for i, (ip, proc) in enumerate(p[:]):
                            if proc.poll() is not None:
                                p.remove((ip, proc))
                                if proc.returncode == 0:
                                    aktif = aktif + 1
                                    list.append(ip)
                                elif proc.returncode == 2:
                                    aktif = yanit_yok + 1
                                else:
                                    pasif = pasif + 1
                        time.sleep(.04)
                    devnull.close()
                    ip_sayisi=len(list)
                    row = 0
                    self.anapencere.lineEdit_total_IP.setText(str(ip_sayisi))
                    self.anapencere.tableWidget_IP_list.setRowCount(ip_sayisi)
                    self.anapencere.lineEdit_uyari.setText(str(ip_sayisi) + " IP active")
                    for i in range (ip_sayisi):
                        self.anapencere.tableWidget_IP_list.setItem(row, 0, QtWidgets.QTableWidgetItem((str(list[i]))))
                        row=row+1

            elif self.window:
                uyari_2 = "not active yet"
                print(uyari_2)
                self.anapencere.lineEdit_uyari.setText(uyari_2)

            else:
                uyari_3 = "select OS"
                print(uyari_3)
                self.anapencere.lineEdit_uyari.setText(uyari_3)

        except Exception as e:
            self.log_yaz("IP_listing ERROR", str(e))
            pass

    def hostname(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('10.0.0.0', 0))
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            self.anapencere.lineEdit_host.setText(hostname)
            #self.anapencere.lineEdit_myIP.setText(s.getsockname()[0])
            self.anapencere.lineEdit_myIP.setText("192.168.2.***")
            """
            print("IP Address: ", s.getsockname()[0])
            print(f"Hostname: {hostname}")
            print(f"LOCAL IP Address: {ip_address}")
            """
        except Exception as e:
            self.log_yaz("hostname ERROR : ", str(e))
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = AnaPencere()
    mainWindow.show()
    sys.exit(app.exec_())