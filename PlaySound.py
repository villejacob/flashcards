import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from pathlib import Path #for checking file exist

class PlaySound(QWidget):

    wav_path = 'default' #file path
    is_exist = False #for debugging purpose

    def __init__(self, wav):
        # wav is the file path

        super().__init__(self)

        #check if file exist
        my_file = Path(wav)
        if my_file.is_file():
            play_sound.is_exist = True
        else:
            print('file NOT exist')

        play_sound.wav_path = wav
        self.initUI()

    def initUI(self):
        self.setMinimumSize(32,32)
        self.b1 = QPushButton("Play", self)
        self.b1.clicked.connect(self.Play)

    def Play(self):
        QSound.play( play_sound.wav_path)
