from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtCore import QPropertyAnimation, QPoint, QThread
import sys
import audiospectrumQT as AuQT

from juleev1 import JULEE 
#for testing text box
#import AnimatedText


isMicOn = 0
isLogoCorner = 0
isActivated = False

class Ui(QtWidgets.QMainWindow):
    

    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('ui/main.ui', self) # Load the .ui file
        #self.DynamicLogo.hide()
        #self.thread={}
        #self.setDebugButtons()
        self.show() # Show the GUI  
        
    #def activateLogo(self):
    #    global isActivated 
    #    if isActivated == True:
    #        self.MainLogo.setPixmap(QtGui.QPixmap("Assets\Logo\JulleeOFF.png"))
    #        self.setStyleSheet("background-color: rgb(50, 50, 50);")
    #        isActivated = False
    #    else:
    #        self.MainLogo.setPixmap(QtGui.QPixmap("Assets\Logo\JulleeON.png"))
    #        self.setStyleSheet("background-color: rgb(0, 85, 127);")
    #        isActivated = True

    #def moveLogo1(self):
    #    #ANIMATION TEST
    #    self.MainLogo.anim = QPropertyAnimation(self.MainLogo, b"pos")
    #    self.MainLogo.anim.setEndValue(QPoint(610, 10))
    #    self.MainLogo.anim.setDuration(100)
    #    self.MainLogo.anim.start()
    #    self.DynamicLogo.show

    #def moveLogo2(self):
    #    #ANIMATION TEST
    #    self.DynamicLogo.hide
    #    self.MainLogo.anim = QPropertyAnimation(self.MainLogo, b"pos")
    #    self.MainLogo.anim.setEndValue(QPoint(280, 180))
    #    self.MainLogo.anim.setDuration(100)
    #    self.MainLogo.anim.start()

    #def changeLogo(self, logo):
    #    self.DynamicLogo.setPixmap(QtGui.QPixmap(logo))

    #def DisplayText(self, insertText): #UNDER CONSTRUCTION
    #    self.TextBox.setText(insertText)

    #def DisplayText2(self, insertText): #UNDER CONSTRUCTION
    #    self.TextBox_2.setText(insertText)

    #def micFunction(self): #UNDER CONSTRUCTION
    #    self.Button_mic.setIcon(QtGui.QPixmap("Assets\Logo\Mic_On.png"))


    #def activateMic(self):
    #    global isMicOn
    #    if isMicOn == 0:
    #        self.Button_mic.setIcon(QtGui.QIcon("Assets\Logo\Mic_On.png"))
    #        #self.MainLogo.setPixmap(QtGui.QPixmap("Assets\Logo\JulleeON.png"))
    #        isMicOn = 1
    #    else: 
    #        self.Button_mic.setIcon(QtGui.QIcon("Assets\Logo\Mic.png"))
    #        isMicOn = 0
           
    def runJullee(self):
        self.thread = QThread()
        self.julee = JULEE()
        self.julee.moveToThread(self.thread)
        #Slot Assign
        self.thread.started.connect(self.julee.run)
        audio_app = AuQT.AudioStream()
        audio_app.animation()
        #self.julee.finished.connect(self.thread.quit)
        #self.julee.finished.connect(self.julee.deleteLater)
        #self.thread.finished.connect(self.thread.deleteLater)
        ##self.julee.speech_julee.connect(self.DisplayText)
        ##self.julee.speech_user.connect(self.DisplayText2)
        #self.julee.flag_on.connect(self.activateLogo)
        #self.julee.flag_off.connect(self.activateLogo)
        self.thread.start()
        







    #def setDebugButtons(self):
    #    #DEBUG BUTTONS
    #    self.Debug_1.clicked.connect(lambda: self.moveLogo1())
    #    self.Debug_2.clicked.connect(lambda: self.moveLogo2())
    #    self.Debug_3.clicked.connect(lambda: self.activateLogo())
    #    self.Debug_4.clicked.connect(lambda: self.DisplayText(loremText))
    #    self.Button_mic.clicked.connect(lambda: self.activateMic())
    #    #Logo Change sets
    #    self.Button_FB.clicked.connect(lambda: self.changeLogo("Assets\Logo\FB.png"))
    #    self.Button_Google.clicked.connect(lambda: self.changeLogo("Assets\Logo\Google.png"))
    #    self.Button_Music.clicked.connect(lambda: self.changeLogo("Assets\Logo\Music.png"))
    #    self.Button_News.clicked.connect(lambda: self.changeLogo("Assets\Logo\\News.png"))
    #    self.Button_Time.clicked.connect(lambda: self.changeLogo("Assets\Logo\Time.png"))
    #    self.Button_Weather.clicked.connect(lambda: self.changeLogo("Assets\Logo\Weather.png"))
    #    self.Button_Who.clicked.connect(lambda: self.changeLogo("Assets\Logo\Who.png"))
    #    self.Button_Wiki.clicked.connect(lambda: self.changeLogo("Assets\Logo\Wiki.png"))
    #    self.Button_Youtube.clicked.connect(lambda: self.changeLogo("Assets\Logo\Youtube.png"))
    #    loremText = lorem.paragraph()
        

    

#FOR DEBUGGING ONLY
app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
window.runJullee()
app.exec_() # Start the application
