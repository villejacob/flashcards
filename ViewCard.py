from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from CommonGUIComponents import *
from db.helpers import *

class ViewCard(QWidget):

    def __init__(self, cardID, viewQuestion=True):
        self.cardID = cardID
        self.viewQuestion = viewQuestion

        super().__init__()

        self.setGeometry(300, 300, 250, 150)

        self.setMaximumSize(300, 200)
        self.setMinimumSize(300, 200)
        self.setStyleSheet("background-color: rgb(255,255,255)")

        self.layout = QVBoxLayout(self)

        cardAssets = get_card_assets(self.cardID)
        assetDict = {row[1]: (row[0], row[2], row[3],) for row in cardAssets}

        question = assetDict.get('question', ('', '', ''))[1]
        answer = assetDict.get('answer', ('', '', ''))[1]

        text = question if self.viewQuestion else answer

        self.textLabel = QLabel(text)
        self.textLabel.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.textLabel)

        self.setLayout(self.layout)

