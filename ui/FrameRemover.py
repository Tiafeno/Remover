from PyQt5 import QtCore, QtGui, QtWidgets
import abc

class Ui_MainWindow(QtWidgets.QMainWindow):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)

        self.setObjectName("MainWindow")
        self.resize(470, 263)
        self.setFixedSize(470, 263)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        self.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/dvd.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("QMainWindow{\n"
"background:#2a2b2c;\n"
"}\n"
"QMainWindow .QWidget{\n"
"background:#2a2b2c;\n"
"}\n"
"QMainWindow .QComboBox QAbstractItemView{\n"
"selection-background-color:#0c7daf !important; \n"
"\n"
"}\n"
"\n"
".Qmenu{\n"
"    background:red;\n"
"}\n"
".Qmenu::item{\n"
"    background:red;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_clean = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clean.setGeometry(QtCore.QRect(30, 70, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.btn_clean.setFont(font)
        self.btn_clean.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_clean.setStyleSheet("border:none;\n"
"background: #BE1E2D;\n"
"padding: 9px;\n"
"color: #FFF;")
        self.btn_clean.setAutoDefault(True)
        self.btn_clean.setDefault(True)
        self.btn_clean.setFlat(False)
        self.btn_clean.setObjectName("btn_clean")

        self.comboBox_drives = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_drives.setGeometry(QtCore.QRect(30, 30, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.comboBox_drives.setFont(font)
        self.comboBox_drives.setObjectName("comboBox_drives")
        self.label_logical = QtWidgets.QLabel(self.centralwidget)
        self.label_logical.setGeometry(QtCore.QRect(30, 10, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setBold(True)
        font.setWeight(75)
        self.label_logical.setFont(font)
        self.label_logical.setStyleSheet("border-radius:20px;\n"
"background: #0c7daf;\n"
"padding-left:5px;\n"
"color: #FFF;")
        self.label_logical.setObjectName("label_logical")
        self.btn_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.btn_refresh.setGeometry(QtCore.QRect(164, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.btn_refresh.setFont(font)
        self.btn_refresh.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_refresh.setStyleSheet("border:none;\n"
"background: #EF4136;\n"
"padding: 9px;\n"
"color: #FFF;")
        self.btn_refresh.setAutoDefault(True)
        self.btn_refresh.setDefault(True)
        self.btn_refresh.setFlat(False)
        self.btn_refresh.setObjectName("btn_refresh")
        self.btn_opendriver = QtWidgets.QPushButton(self.centralwidget)
        self.btn_opendriver.setGeometry(QtCore.QRect(230, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.btn_opendriver.setFont(font)
        self.btn_opendriver.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_opendriver.setStyleSheet("border:none;\n"
"background: #0c7daf;\n"
"padding: 9px;\n"
"color: #FFF;")
        self.btn_opendriver.setAutoDefault(True)
        self.btn_opendriver.setDefault(True)
        self.btn_opendriver.setFlat(False)
        self.btn_opendriver.setObjectName("btn_opendriver")
        self.TextEditlogs = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.TextEditlogs.setGeometry(QtCore.QRect(30, 110, 421, 71))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(8)
        self.TextEditlogs.setFont(font)
        self.TextEditlogs.setStyleSheet("background: #000;\n"
"padding-left:5px;\n"
"color: #FFF;\n"
"border:6px solid #000;")
        self.TextEditlogs.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TextEditlogs.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TextEditlogs.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.TextEditlogs.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.TextEditlogs.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.TextEditlogs.setReadOnly(True)
        self.TextEditlogs.setCenterOnScroll(True)
        self.TextEditlogs.setObjectName("TextEditlogs")
        self.btn_openlogs = QtWidgets.QPushButton(self.centralwidget)
        self.btn_openlogs.setGeometry(QtCore.QRect(380, 180, 71, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(10)
        self.btn_openlogs.setFont(font)
        self.btn_openlogs.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_openlogs.setStyleSheet("border:none;\n"
"background: #0c7daf;\n"
"padding: 4px;\n"
"color: #FFF;")
        self.btn_openlogs.setAutoDefault(True)
        self.btn_openlogs.setDefault(True)
        self.btn_openlogs.setFlat(False)
        self.btn_openlogs.setObjectName("btn_openlogs")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 470, 21))
        self.menubar.setObjectName("menubar")
        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionA_propos = QtWidgets.QAction(self)
        self.actionA_propos.setObjectName("actionA_propos")
        self.menuAide.addAction(self.actionA_propos)
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi()
        self.comboBox_drives.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "QRemover by T.Finel"))
        self.btn_clean.setText(_translate("MainWindow", "Clean"))

        self.label_logical.setText(_translate("MainWindow", "Logical drives"))
        self.btn_refresh.setText(_translate("MainWindow", "Refresh"))
        self.btn_opendriver.setToolTip(_translate("MainWindow", "<html><head/><body><p>Explorer le disque amovible</p></body></html>"))
        self.btn_opendriver.setText(_translate("MainWindow", "Open"))
        self.TextEditlogs.setPlainText(_translate("MainWindow", " "))
        self.btn_openlogs.setToolTip(_translate("MainWindow", "<html><head/><body><p>Afficher les contenues de votre disque amovible</p></body></html>"))
        self.btn_openlogs.setText(_translate("MainWindow", "Logs"))
        self.menuAide.setTitle(_translate("MainWindow", "Help"))
        self.actionA_propos.setText(_translate("MainWindow", "About me"))