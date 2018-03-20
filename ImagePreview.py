from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
import sys

class ImagePreview(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setMinimumSize(32,32)
        label = QLabel(self)

        #TODO: dynamic pathing
        pixmap = QPixmap('example.jpg')
        resize_pixmap = pixmap.scaled(32, 32)
        label.setPixmap(resize_pixmap)
