# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainRVYOKe.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from qt_core import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(433, 572)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drop_shadow_frame = QLabel(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setGeometry(QRect(0, 0, 431, 571))
        self.drop_shadow_frame.setStyleSheet(u"background-color: rgb(72, 72, 72);\n"
"border-radius: 20px;")
        self.title_bar = QLabel(self.centralwidget)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setGeometry(QRect(0, 0, 61, 571))
        self.title_bar.setStyleSheet(u"QLabel {\n"
"	background-color: rgb(0, 0, 0);		\n"
"	border-top-left-radius: 20px; \n"
"	border-bottom-left-radius: 20px; \n"
"}")
        self.btn_close = QPushButton(self.centralwidget)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(20, 20, 16, 16))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;	\n"
"	background-color: rgb(157, 0, 0);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        self.btn_minimize = QPushButton(self.centralwidget)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setGeometry(QRect(20, 50, 16, 16))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;	\n"
"	background-color: rgb(56, 167, 82);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgb(85, 255, 127);\n"
"}")
        self.github_i = QLabel(self.centralwidget)
        self.github_i.setObjectName(u"github_i")
        self.github_i.setGeometry(QRect(10, 510, 41, 41))
        self.github_i.setStyleSheet(u"")
        self.github_i.setPixmap(QPixmap(u"git-g.png"))
        self.github_i.setScaledContents(True)
        self.spotify_logo = QLabel(self.centralwidget)
        self.spotify_logo.setObjectName(u"spotify_logo")
        self.spotify_logo.setGeometry(QRect(90, 60, 291, 291))
        self.spotify_logo.setPixmap(QPixmap(u"logo.png"))
        self.spotify_logo.setScaledContents(True)
        self.label_audioformat = QLabel(self.centralwidget)
        self.label_audioformat.setObjectName(u"label_audioformat")
        self.label_audioformat.setGeometry(QRect(70, 400, 111, 17))
        self.label_url = QLabel(self.centralwidget)
        self.label_url.setObjectName(u"label_url")
        self.label_url.setGeometry(QRect(70, 340, 51, 21))
        self.status_bk = QLabel(self.centralwidget)
        self.status_bk.setObjectName(u"status_bk")
        self.status_bk.setGeometry(QRect(130, 470, 201, 21))
        self.status_bk.setStyleSheet(u"background-color: rgb(139, 139, 139);\n"
"border-radius : 10px;")
        self.stat = QLabel(self.centralwidget)
        self.stat.setObjectName(u"stat")
        self.stat.setGeometry(QRect(240, 470, 111, 21))
        self.Downlaodbt = QPushButton(self.centralwidget)
        self.Downlaodbt.setObjectName(u"Downlaodbt")
        self.Downlaodbt.setGeometry(QRect(146, 508, 171, 41))
        self.Downlaodbt.released.connect(self.dl)
        self.spotify_text = QLabel(self.centralwidget)
        self.spotify_text.setObjectName(u"spotify_text")
        self.spotify_text.setGeometry(QRect(60, 20, 351, 41))
        self.select_format = QComboBox(self.centralwidget)
        self.select_format.addItem("")
        self.select_format.addItem("")
        self.select_format.addItem("")
        self.select_format.addItem("")
        self.select_format.addItem("")
        self.select_format.addItem("")
        self.select_format.setObjectName(u"select_format")
        self.select_format.setGeometry(QRect(70, 420, 151, 31))
        self.select_format.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(143, 143, 143);\n"
"color: rgb(255, 255, 255);\n"
"text-align:center;")
        self.input_url = QLineEdit(self.centralwidget)
        self.input_url.setObjectName(u"input_url")
        self.input_url.setGeometry(QRect(70, 360, 351, 31))
        self.input_url.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(143, 143, 143);\n"
"color: rgb(255, 255, 255);")
        self.ver = QLabel(self.centralwidget)
        self.ver.setObjectName(u"ver")
        self.ver.setGeometry(QRect(180, 470, 61, 21))
        self.folder_path = QLineEdit(self.centralwidget)
        self.folder_path.setObjectName(u"folder_path")
        self.folder_path.setGeometry(QRect(230, 420, 151, 31))
        self.folder_path.setStyleSheet(u"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"\n"
"background-color: rgb(143, 143, 143);\n"
"color: rgb(255, 255, 255);")
        self.select_folder = QPushButton(self.centralwidget)
        self.select_folder.setObjectName(u"select_folder")
        self.select_folder.setGeometry(QRect(390, 420, 31, 31))
        self.select_folder.clicked.connect(self.open_folder)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 400, 101, 17))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.drop_shadow_frame.setText("")
        self.title_bar.setText("")
        self.btn_close.setText("")
        self.btn_minimize.setText("")
        self.github_i.setText("")
        self.spotify_logo.setText("")
        self.label_audioformat.setText(QCoreApplication.translate("MainWindow", u"AUDIO FORMAT:", None))
        self.label_url.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">URL:</span></p></body></html>", None))
        self.status_bk.setText("")
        self.stat.setText(QCoreApplication.translate("MainWindow", u"  v1.0", None))
        self.Downlaodbt.setText(QCoreApplication.translate("MainWindow", u"Downlaod", None))
        self.spotify_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Spotify Downloader</span></p></body></html>", None))
        self.select_format.setItemText(0, QCoreApplication.translate("MainWindow", u"mp3", None))
        self.select_format.setItemText(1, QCoreApplication.translate("MainWindow", u"wav", None))
        self.select_format.setItemText(2, QCoreApplication.translate("MainWindow", u"flac", None))
        self.select_format.setItemText(3, QCoreApplication.translate("MainWindow", u"ogg", None))
        self.select_format.setItemText(4, QCoreApplication.translate("MainWindow", u"m4a", None))
        self.select_format.setItemText(5, QCoreApplication.translate("MainWindow", u"opus", None))

        self.ver.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">VERSION:</span></p></body></html>", None))
        self.select_folder.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"OUTPUT PATH:", None))
    # retranslateUi


    def open_folder(self):
        path_fol = QFileDialog.getExistingDirectory()
        print(path_fol)
        self.folder_path.setText(path_fol)

    def dl(self):
        print("Your URL: " + self.input_url.text())
        audio_format = self.select_format.currentText()
        self.p = QProcess()
        self.p.startDetached("spotdl " + "--output-format " + audio_format + " " + "-o " + self.folder_path.text() + " " + self.input_url.text())








