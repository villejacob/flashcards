from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from CommonGUIComponents import *
from db.helpers import *
from PlaySound import *
from ViewVideo import*

class ViewStack(QWidget):

    def __init__(self, mainMenu=None, stackID=None,
                    pos = QPoint(300, 300), size = QSize(250, 150)):
        self.stackID = stackID
        self.mainMenu = mainMenu
        self.cardID = None
        #variable for determing which side of the card is being viewed
        self.viewFront = True

        super().__init__()

        #set size and position
        #usually passed in by constructor from
        #the main menu
        self.move(pos)
        self.resize(size)

        self.setWindowTitle('View Stack')


    @pyqtSlot()
    def backToMainMenu(self):
        #switch to main menu with current size and position
        openMainMenu(self)
        self.hide()

    @pyqtSlot()
    def enterEditMode(self):
        #switch to main menu with current size and position
        openEditWindow(self)
        self.hide()

    def onViewVideoClick(self):
        if (self.videoLocation != ''):
            self.vv = ViewVideo(self.videoLocation)
            self.vv.create()
            print('Opening Video')
        else:
            msg = QMessageBox()
            msg.setText("No video found")
            msg.setWindowTitle("Attention!")
            retval = msg.exec_()

    @pyqtSlot()
    def onFlipClick(self):
        #changes the side of the card being viewed
        if (self.viewFront == True):
            self.viewFront = False
            print('success')
        else:
            self.viewFront = True
        #refresh page
        QWidget().setLayout(self.layout())
        self.create()

    def switchToCard(self, cardID):
    	#gets information from a card, same as EditStack
        self.cardID = cardID
        dbData = get_card_assets(self.cardID)
        print(dbData)

        #key is asset type
        #value is (id, content, filename)
        self.assetDict = {row[1]: (row[0], row[2], row[3],) for row in dbData}

        self.frontText = self.assetDict.get('question', ('', '', ''))[1]
        self.backText = self.assetDict.get('answer', ('', '', ''))[1]
        self.imageLocation = self.assetDict.get('image', ('', '', ''))[2]
        self.videoLocation = self.assetDict.get('video', ('', '', ''))[2]
        self.audioLocation = self.assetDict.get('audio', ('', '', ''))[2]


    def create(self):

        self.fullLayout = QVBoxLayout()

        #create the top row of the layout to have
        #a main menu button and a edit button

        row = QHBoxLayout()

        #create button for main menu
        #button will be fixed against left and top
        back = QPushButton('Main Menu')
        back.clicked.connect(self.backToMainMenu)
        row.addWidget(back)

        row.addStretch(1)

        #create button for flipping card
        flip = QPushButton('Flip')
        flip.clicked.connect(self.onFlipClick)
        row.addWidget(flip)

        row.addStretch(1)

        #create button for main menu
        #button will be fixed against right and top
        back = QPushButton('Edit')
        back.clicked.connect(self.enterEditMode)
        row.addWidget(back)

        #retrieve cards from DB
        self.cardIDs = get_stack_cards(self.stackID)

        self.switchToCard(self.cardIDs[0][0])

        #add row for navigation
        self.fullLayout.addLayout(row)

        self.fullLayout.addStretch(1)

        if len(self.cardIDs) > 0:

            row = QHBoxLayout()

            #displays labels
            if (self.viewFront == True):
                frontLabel = QLabel(self.frontText)
                frontLabel.setAlignment(Qt.AlignCenter)
                row.addWidget(frontLabel)

            else:
                backLabel = QLabel(self.backText)
                backLabel.setAlignment(Qt.AlignCenter)
                row.addWidget(backLabel)

            self.fullLayout.addLayout(row)

            self.fullLayout.addStretch(1)

            row = QHBoxLayout()

            row.addStretch(5)

            #GUI for showing cards goes here
            #needs to be added to self.fullLayout

            #TODO: add view stack code

            row.addStretch(1)
           #image
            viewImage = QPushButton('View Image')
            row.addWidget(viewImage)

            #audio
            hearAudio = PlaySound(self.audioLocation)
            row.addWidget(hearAudio)

	        #video
            viewVideo = QPushButton('View Video')
            viewVideo.clicked.connect(self.onViewVideoClick)
            row.addWidget(viewVideo)
        else:
            row = QHBoxLayout()

            noCardLabel = QLabel('There are no cards in this stack')
            row.addWidget(noCardLabel)


        self.fullLayout.addLayout(row)

        self.setLayout(self.fullLayout)

        self.show()

    #the MainMenu needs to be opened on close
    def closeEvent(self, event):
        openMainMenu(self)
        event.accept()
