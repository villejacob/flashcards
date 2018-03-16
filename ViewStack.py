from PyQt5.QtWidgets import QMainWindow, QLabel

class ViewStack(QMainWindow):

    def __init__(self, mainMenu=None, stackID=None):
        self.stackID = stackID
        self.mainMenu = mainMenu
        super().__init__()

    def create(self):
        #left, top, width, height
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('View Stack')
        self.show()

    #the MainMenu needs to be opened on close
    def closeEvent(self, event):
        if self.mainMenu is not None:
            self.mainMenu.show()
        event.accept()
