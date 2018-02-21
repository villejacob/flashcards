from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot

class MainMenu(QWidget):

    def __init__(self):

        super().__init__()

    @pyqtSlot()
    def onStudyClick(self, stackID):
        print('Studying Stack ' + str(stackID))

    @pyqtSlot()
    def onEditClick(self, stackID):
        print('Editing Stack ' + str(stackID))

    @pyqtSlot()
    def onDeleteClick(self, stackID):
        print('Deleting Stack ' + str(stackID))

    @pyqtSlot()
    def onAddStackClick(self):
        print('Adding Stack')

    def create(self):

        #create main window
        #left, top, width, height
        self.setGeometry(300, 300, 750, 450)
        self.setWindowTitle('Main Menu')

        stacks = [0, 1, 2] #replace with method getting list of stackIDs

        fullList = QVBoxLayout()

        #layout the list of stacks
        for stack in stacks:
            row = QHBoxLayout()

            row.addStretch(1)
            #image would go here
            row.addStretch(5)

            study = QPushButton('Study')
            study.clicked.connect(lambda : self.onStudyClick(stack))
            row.addWidget(study)

            edit = QPushButton('Edit')
            edit.clicked.connect(lambda : self.onEditClick(stack))
            row.addWidget(edit)

            delete = QPushButton('Delete')
            delete.clicked.connect(lambda : self.onDeleteClick(stack))
            row.addWidget(delete)

            row.addStretch(1)

            fullList.addStretch(1)
            fullList.addLayout(row)

        #add button for new stack
        fullList.addStretch(1)
        row = QHBoxLayout()
        addNew = QPushButton('Add new stack')
        addNew.clicked.connect(self.onAddStackClick)
        row.addWidget(addNew)
        fullList.addLayout(row)

        #set the layout for the window to the vbox layout
        self.setLayout(fullList)

        self.show()
