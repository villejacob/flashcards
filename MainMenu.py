from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton

class MainMenu(QMainWindow):

    def __init__(self):

        super().__init__()

    def create(self):

        #create main window
        #left, top, width, height
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Main Menu')

        stacks = [] #replace with method getting list of stackIDs

        fullList = QVBoxLayout()

        #layout the list of stacks
        for stack in stacks:
            row = QHBoxLayout()

            row.addStretch(1)
            #image would go here
            row.addStretch(2)

            study = QPushButton('Study')
            row.addWidget(study)

            edit = QPushButton('Edit')
            row.addWidget(edit)

            delete = QPushButton('Delete')
            row.addWidget(delete)

            fullList.addStretch(1)
            fullList.addLayout(row)

        #add button for new stack
        row = QHBoxLayout()
        addNew = QPushButton('Add new stack')
        row.addWidget(addNew)
        fullList.addLayout(row)

        #set the layout for the window to the vbox layout
        self.setLayout(fullList)

        self.show()
