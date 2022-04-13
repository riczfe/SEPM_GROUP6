from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtCore import QPropertyAnimation, QPoint
import sys
import random
islogoon = 0
isLogoCorner = 0
class Ui(QtWidgets.QMainWindow):
    

    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('ui/mainwin.ui', self) # Load the .ui file
        self.DynamicLogo.hide
        
        
        def activateLogo():
            global islogoon
            if islogoon == 0:
                self.MainLogo.setPixmap(QtGui.QPixmap("Assets\Logo\JulleeON.png"))
                self.setStyleSheet("background-color: rgb(0, 85, 127);")
                islogoon = 1
            else: 
                self.MainLogo.setPixmap(QtGui.QPixmap("Assets\Logo\JulleeOFF.png"))
                self.setStyleSheet("background-color: rgb(50, 50, 50);")
                islogoon = 0

        def moveLogo1():
            #ANIMATION TEST
            self.MainLogo.anim = QPropertyAnimation(self.MainLogo, b"pos")
            self.MainLogo.anim.setEndValue(QPoint(610, 10))
            self.MainLogo.anim.setDuration(100)
            self.MainLogo.anim.start()
            self.DynamicLogo.show
        def moveLogo2():
            #ANIMATION TEST
            self.DynamicLogo.hide
            self.MainLogo.anim = QPropertyAnimation(self.MainLogo, b"pos")
            self.MainLogo.anim.setEndValue(QPoint(280, 180))
            self.MainLogo.anim.setDuration(100)
            self.MainLogo.anim.start()

        def changeLogo(logo):
            self.DynamicLogo.setPixmap(QtGui.QPixmap(logo))

        #def DisplayText(): #UNDER CONSTRUCTION


        #DEBUG BUTTONS
        self.Debug_1.clicked.connect(lambda: moveLogo1())
        self.Debug_2.clicked.connect(lambda: moveLogo2())
        self.Debug_3.clicked.connect(lambda: activateLogo())
        #Logo Change sets
        self.Button_FB.clicked.connect(lambda: changeLogo("Assets\Logo\FB.png"))
        self.Button_Google.clicked.connect(lambda: changeLogo("Assets\Logo\Google.png"))
        self.Button_Music.clicked.connect(lambda: changeLogo("Assets\Logo\Music.png"))
        self.Button_News.clicked.connect(lambda: changeLogo("Assets\Logo\\News.png"))
        self.Button_Time.clicked.connect(lambda: changeLogo("Assets\Logo\Time.png"))
        self.Button_Weather.clicked.connect(lambda: changeLogo("Assets\Logo\Weather.png"))
        self.Button_Who.clicked.connect(lambda: changeLogo("Assets\Logo\Who.png"))
        self.Button_Wiki.clicked.connect(lambda: changeLogo("Assets\Logo\Wiki.png"))
        self.Button_Youtube.clicked.connect(lambda: changeLogo("Assets\Logo\Youtube.png"))

        self.show() # Show the GUI  

    

#FOR DEBUGGING ONLY
app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application
