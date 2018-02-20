from PyQt5.QtWidgets import QMainWindow, QLabel

class ViewStack(QMainWindow):

    def __init__(self, stackID=None):
        self.stackID = stackID
        super().__init__()

    def create(self):
        #left, top, width, height
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('View Stack')
        self.show()
