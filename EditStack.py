from PyQt5.QtWidgets import QMainWindow, QMessageBox

class EditStack(QMainWindow):

    def __init__(self, mainMenu=None, stackID=None):
        self.stackID = stackID
        self.mainMenu = mainMenu
        self.unsavedChanges = False
        super().__init__()

    def create(self):
        #left, top, width, height
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Edit Stack')
        self.show()

    #save changes to database
    def save():
        self.unsavedChanges = False

    #the MainMenu needs to be opened on close
    #edits need to be checked to unsure nothing is unsaved
    def closeEvent(self, event):
        close = True

        if self.unsavedChanges:
            reply = QMessageBox.question(self, 'Unsaved changes',
                'Would you like to save your changes?',
                 QMessageBox.Save | QMessageBox.No | QMessageBox.Cancel,
                 QMessageBox.Save)
            if reply == QMessageBox.Save:
                self.save()
            elif reply == QMessageBox.Cancel:
                event.ignore()
                return

        if self.mainMenu is not None:
            self.mainMenu.show()
        event.accept()
