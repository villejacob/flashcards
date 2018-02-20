from PyQt5.QtWidgets import QMainWindow

class EditStack(QMainWindow):

    def __init__(self, stackID=None):
        self.stackID = stackID
        super().__init__()

    def create(self):
        #left, top, width, height
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Edit Stack')
        self.show()
