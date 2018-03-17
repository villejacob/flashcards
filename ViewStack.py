from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

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


    def create(self):
        self.show()

    #the MainMenu needs to be opened on close
    def closeEvent(self, event):
        if self.mainMenu is not None:
            #copy size and position over to main menu
            self.mainMenu.move(self.pos())
            self.mainMenu.resize(self.size())

            #show main menu
            self.mainMenu.show()
        event.accept()
