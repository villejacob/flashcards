from PyQt5.QtWidgets import *
from ImagePreview import *
from PyQt5.QtCore import pyqtSlot
from ViewStack import *
from EditStack import *


class MainMenu(QWidget):

    def __init__(self):

        super().__init__()

    @pyqtSlot()
    def onStudyClick(self, stackID):
        self.hide()
        self.vs = ViewStack(self, stackID)
        self.vs.create()
        print('Studying Stack ' + str(stackID))

    @pyqtSlot()
    def onEditClick(self, stackID):
        self.hide()
        self.es = EditStack(self, stackID)
        self.es.create()
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

        #keep track of buttons
        self.studyButttons = []
        self.editButtons = []
        self.deleteButtons = []

        stacks = [0, 1, 2] #replace with method getting list of stackIDs

        self.fullList = QVBoxLayout()

        #layout the list of stacks
        #essentially this creates a bunch of horizontal boxes (QHBoxLayout) and
        #adds the elements for each stack to them, each of these hboxes is then
        #added to vertical box (QVBoxLayout) created above to create the overall
        #layout
        for stack in stacks:
            row = QHBoxLayout()

            row.addStretch(1)
            #image would go here
            image = ImagePreview()
            row.addWidget(image)

            row.addStretch(5)

            #note: the "check" parameter is needed in the lambda as it
            #is passed by the clicked event (it is a boolean signifying if
            # the button has been checked, if checkable)

            #create study button
            study = QPushButton('Study')
            study.clicked.connect(lambda check,x=stack: self.onStudyClick(x))
            self.studyButttons.append(study)
            row.addWidget(study)

            #create edit button
            edit = QPushButton('Edit')
            edit.clicked.connect(lambda check,x=stack: self.onEditClick(x))
            self.editButtons.append(edit)
            row.addWidget(edit)

            #create delete button
            delete = QPushButton('Delete')
            delete.clicked.connect(lambda check,x=stack: self.onDeleteClick(x))
            self.deleteButtons.append(delete)
            row.addWidget(delete)

            row.addStretch(1)

            self.fullList.addStretch(1)
            self.fullList.addLayout(row)

        #add button for new stack
        self.fullList.addStretch(1)
        row = QHBoxLayout()
        addNew = QPushButton('Add new stack')
        addNew.clicked.connect(self.onAddStackClick)
        row.addWidget(addNew)
        self.fullList.addLayout(row)

        #set the layout for the window to the vbox layout
        self.setLayout(self.fullList)

        self.show()
