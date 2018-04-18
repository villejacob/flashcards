from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
        QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
from PyQt5.QtWidgets import QMainWindow,QWidget, QPushButton, QAction
from PyQt5.QtGui import QIcon
import sys
 
class VideoWindow(QMainWindow):

    where = 'default'
 
    def __init__(self, video):
        
        self.where = video
        super(VideoWindow, self).__init__(None)
        self.setWindowTitle(video) 
        
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
 
        videoWidget = QVideoWidget()
 
        self.playButton = QPushButton()
        self.playButton.setEnabled(True) 
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.stopButton = QPushButton()
        self.stopButton.setEnabled(True) 
        self.stopButton.setIcon(self.style().standardIcon(QStyle.SP_MediaStop))
        self.stopButton.clicked.connect(self.exitCall)
 
        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)
 
        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
 

      
 
        # Create exit action
        exitAction = QAction(QIcon('exit.png'), '&Stop', self)       
        exitAction.triggered.connect(self.exitCall)
 
        # Create menu bar and add action
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        
        #fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)
 
        # Create a widget for window contents
        wid = QWidget(self)
        self.setCentralWidget(wid)
 
        # Create layouts to place inside widget
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.stopButton)
        controlLayout.addWidget(self.positionSlider)
 
        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addWidget(self.errorLabel)
 
        # Set widget to contain window contents
        wid.setLayout(layout)
 
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError) 

 
    def exitCall(self):
        self.mediaPlayer.setVolume(0)
        self.mediaPlayer.stop()
        
    def play(self):
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(self.where)))
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.setVolume(100)
            self.mediaPlayer.play()
 
    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))
 
    def positionChanged(self, position):
        self.positionSlider.setValue(position)
 
    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)
 
    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)
 
    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoWindow('goat.avi')
    player.resize(640, 480)
    player.show()
    sys.exit(app.exec_())
