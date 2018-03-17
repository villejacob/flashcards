from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class EditStack(QWidget):

    def __init__(self, mainMenu=None, stackID=None,
                    pos = QPoint(300, 300), size = QSize(250, 150)):
        self.stackID = stackID
        self.mainMenu = mainMenu
        self.unsavedChanges = False

        super().__init__()

        #set size and position
        #usually passed in by constructor from
        #the main menu
        self.move(pos)
        self.resize(size)

        self.setWindowTitle('Edit Stack')



    def create(self):
        self.show()

    #save changes to database
    def save(self):
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
            #copy size and position over to main menu
            self.mainMenu.move(self.pos())
            self.mainMenu.resize(self.size())

            #show main menu
            self.mainMenu.show()
        event.accept()
