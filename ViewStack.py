from PyQt5.QtWidgets import QMainWindow

class ViewStack(QMainWindow):

    def __init__(self):

        super().__init__()

    def create(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('View Stack')
        self.show()
