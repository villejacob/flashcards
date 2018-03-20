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

        #create the top row of the layout to have
        #a main menu button and a study button

        row = QHBoxLayout()

        #create button for main menu
        #button will be fixed against left and top
        back = QPushButton('Main Menu')
        back.clicked.connect(self.backToMainMenu)
        row.addWidget(back)

        row.addStretch(1)

        #create button for main menu
        #button will be fixed against right and top
        back = QPushButton('Study')
        back.clicked.connect(self.enterStudyMode)
        row.addWidget(back)

        self.fullLayout.addLayout(row)

        self.fullLayout.addStretch(1)

        #rest of GUI added here

        row = QHBoxLayout()

        #TODO: list of cards

        row.addStretch(2)

        editSplit = QVBoxLayout()

        editArea = QGroupBox('Edit Card')

        editForm = QFormLayout()

        editForm.addRow(QLabel('Front text'), QTextEdit())
        editForm.addRow(QLabel('Back text'), QTextEdit())

        editArea.setLayout(editForm)

        editSplit.addWidget(editArea)

        editSplit.addStretch(1)

        #TODO: add drag/drop components (maybe)
        #could be something else

        row.addLayout(editSplit)

        row.addStretch(1)

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
