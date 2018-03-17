from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from CommonGUIComponents import *

class ViewStack(QWidget):

    def __init__(self, mainMenu=None, stackID=None,
                    pos = QPoint(300, 300), size = QSize(250, 150)):
        self.stackID = stackID
        self.mainMenu = mainMenu

        super().__init__()

        #set size and position
        #usually passed in by constructor from
        #the main menu
        self.move(pos)
        self.resize(size)

        self.setWindowTitle('View Stack')


    @pyqtSlot()
    def backToMainMenu(self):
        openMainMenu(self)
        self.hide()

    @pyqtSlot()
    def enterEditMode(self):
        openEditWindow(self)
        self.hide()

    def create(self):

        self.fullLayout = QVBoxLayout()

        row = QHBoxLayout()

        back = QPushButton('Main Menu')
        back.clicked.connect(self.backToMainMenu)
        row.addWidget(back)

        row.addStretch(1)

        back = QPushButton('Edit')
        back.clicked.connect(self.enterEditMode)
        row.addWidget(back)

        self.fullLayout.addLayout(row)

        self.fullLayout.addStretch(1)

        self.setLayout(self.fullLayout)

        self.show()

    #the MainMenu needs to be opened on close
    def closeEvent(self, event):
        openMainMenu(self)
        event.accept()
