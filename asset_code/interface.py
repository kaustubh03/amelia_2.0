from PyQt4 import QtCore, QtGui
import aiml
import os
import time
from gtts import gTTS
import subprocess


kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

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
        MainWindow.resize(804, 433)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.text1 = QtGui.QLineEdit(self.centralwidget)
        self.text1.setGeometry(QtCore.QRect(200, 340, 531, 61))
        self.text1.setObjectName(_fromUtf8("textEdit"))
        self.btn = QtGui.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(730, 340, 71, 61))
        self.btn.setObjectName(_fromUtf8("pushButton"))
        self.btn.clicked.connect(self.askfunc)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def askfunc(MainWindow, self):
            message = MainWindow.text1.text()
            message=str(message)
            if message == "quit" or message=="bye":
                print "Nice Talking to You, Bye"
                text2speak = "Nice Talking to You, Bye"
                tts = gTTS(text=text2speak, lang='en')
                tts.save("C:/{0}.ogg".format(text2speak))
                exit()
            elif message == "save":
                kernel.saveBrain("bot_brain.brn")

            else:
                output = subprocess.check_output(['python', filepath])
                print output
                print kernel.respond(message)
                text2speak = kernel.respond(message)
                tts = gTTS(text=text2speak, lang='en')
                tts.save("C:/{0}.mp3".format(text2speak))
                exit()


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btn.setText(_translate("MainWindow", "Send", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)

    splash_pix = QtGui.QPixmap('conti.jpg')
    splash = QtGui.QSplashScreen(splash_pix)
    splash.setMask(splash_pix.mask())
    splash.show()
    time.sleep(2)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())