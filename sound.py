import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import * # from QT5 class PyQt5.QtMultimedia.QSound
from pathlib import Path #for checking file exist

class play_sound(QMainWindow):
    
    wav_path = 'default' #file path 
    is_exist = False #for debugging purpose
    
    def __init__(self, wav):
        # wav is the file path
        
        QMainWindow.__init__(self)
        
        #check if file exist        
        my_file = Path(wav)
        if my_file.is_file():
            play_sound.is_exist = True
        else:
            print('file NOT exist')
            
        play_sound.wav_path = wav
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,200,200)
        self.b1 = QPushButton("Play", self)        
        self.b1.clicked.connect(self.Play)
        self.b1.move(50, 80)

    def Play(self):
        QSound.play( play_sound.wav_path)
        
    



    

app = QApplication(sys.argv)

sound_path = 'goat.wav'
test_sound = play_sound(sound_path)
test_sound.show()

sys.exit(app.exec_())







