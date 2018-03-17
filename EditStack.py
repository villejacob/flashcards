from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from CommonGUIComponents import *

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

    @pyqtSlot()
    def backToMainMenu(self):
        self.hide()
        openMainMenu(self)

    @pyqtSlot()
    def enterStudyMode(self):
        self.hide()
        openViewWindow(self)

    def create(self):

        self.fullLayout = QVBoxLayout()

        row = QHBoxLayout()

        back = QPushButton('Main Menu')
        back.clicked.connect(self.backToMainMenu)
        row.addWidget(back)

        row.addStretch(1)

        back = QPushButton('Study')
        back.clicked.connect(self.enterStudyMode)
        row.addWidget(back)

        self.fullLayout.addLayout(row)

        self.fullLayout.addStretch(1)

        self.setLayout(self.fullLayout)


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

        openMainMenu(self)
        event.accept()
