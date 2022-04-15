from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtCore import QPropertyAnimation, QPoint
import sys
import lorem #for testing text box
import AnimatedText

islogoon = 0
isLogoCorner = 0
class Ui(QtWidgets.QMainWindow):
    

    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('ui/mainwin.ui', self) # Load the .ui file
        self.DynamicLogo.hide
        self.setDebugButtons()
        self.show() # Show the GUI  
        
    def activateLogo(self):
        global islogoon
        if islogoon == 0:
            self.MainLogo.setPixmap(QtGui.QPixmap("Assets\Logo\JulleeON.png"))
            self.setStyleSheet("background-color: rgb(0, 85, 127);")
            islogoon = 1
        else: 
            self.MainLogo.setPixmap(QtGui.QPixmap("Assets\Logo\JulleeOFF.png"))
            self.setStyleSheet("background-color: rgb(50, 50, 50);")
            islogoon = 0

    def moveLogo1(self):
        #ANIMATION TEST
        self.MainLogo.anim = QPropertyAnimation(self.MainLogo, b"pos")
        self.MainLogo.anim.setEndValue(QPoint(610, 10))
        self.MainLogo.anim.setDuration(100)
        self.MainLogo.anim.start()
        self.DynamicLogo.show

    def moveLogo2(self):
        #ANIMATION TEST
        self.DynamicLogo.hide
        self.MainLogo.anim = QPropertyAnimation(self.MainLogo, b"pos")
        self.MainLogo.anim.setEndValue(QPoint(280, 180))
        self.MainLogo.anim.setDuration(100)
        self.MainLogo.anim.start()

    def changeLogo(self, logo):
        self.DynamicLogo.setPixmap(QtGui.QPixmap(logo))

    def DisplayText(self, insertText): #UNDER CONSTRUCTION
        self.TextBox.setText(insertText)
           

    def setDebugButtons(self):
        #DEBUG BUTTONS
        self.Debug_1.clicked.connect(lambda: self.moveLogo1())
        self.Debug_2.clicked.connect(lambda: self.moveLogo2())
        self.Debug_3.clicked.connect(lambda: self.activateLogo())
        self.Debug_4.clicked.connect(lambda: self.DisplayText(loremText))
        #Logo Change sets
        self.Button_FB.clicked.connect(lambda: self.changeLogo("Assets\Logo\FB.png"))
        self.Button_Google.clicked.connect(lambda: self.changeLogo("Assets\Logo\Google.png"))
        self.Button_Music.clicked.connect(lambda: self.changeLogo("Assets\Logo\Music.png"))
        self.Button_News.clicked.connect(lambda: self.changeLogo("Assets\Logo\\News.png"))
        self.Button_Time.clicked.connect(lambda: self.changeLogo("Assets\Logo\Time.png"))
        self.Button_Weather.clicked.connect(lambda: self.changeLogo("Assets\Logo\Weather.png"))
        self.Button_Who.clicked.connect(lambda: self.changeLogo("Assets\Logo\Who.png"))
        self.Button_Wiki.clicked.connect(lambda: self.changeLogo("Assets\Logo\Wiki.png"))
        self.Button_Youtube.clicked.connect(lambda: self.changeLogo("Assets\Logo\Youtube.png"))
        loremText = lorem.paragraph() + lorem.paragraph() + lorem.paragraph() + lorem.paragraph()
        

    

    

###FOR DEBUGGING ONLY
#app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
#window = Ui() # Create an instance of our class
#app.exec_() # Start the application
