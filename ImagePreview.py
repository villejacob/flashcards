from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from db.helpers import *
import sys

class ImagePreview(QWidget):

    def __init__(self, CardID):
        super().__init__()
        self.CardID = CardID
        self.initUI()

    def initUI(self):
        self.setMinimumSize(32,32)
        label = QLabel(self)

        #TODO: dynamic pathing
        imagePath = get_card_asset(self.CardID, "image")
        pixmap = QPixmap(imagePath[3])
        resize_pixmap = pixmap.scaled(32, 32)
        label.setPixmap(resize_pixmap)
