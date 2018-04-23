from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from CommonGUIComponents import *
from db.helpers import *

class EditStack(QWidget):

    def __init__(self, mainMenu=None, stackID=None,
                    pos = QPoint(300, 300), size = QSize(250, 150)):
        self.stackID = stackID
        self.mainMenu = mainMenu
        self.unsavedChanges = False
        self.cardID = None
        self.index = 0
        self.cardNum = 0

        super().__init__()

        #set size and position
        #usually passed in by constructor from
        #the main menu
        self.move(pos)
        self.resize(size)

        self.setWindowTitle('Edit Stack')

    @pyqtSlot()
    def backToMainMenu(self):
        if not self.checkSaved():
            return
        self.hide()
        openMainMenu(self)

    @pyqtSlot()
    def enterStudyMode(self):
        if not self.checkSaved():
            return
        self.hide()
        openViewWindow(self)

    @pyqtSlot()
    def selectImageFile(self):
        #TODO: update with accepted image files
        fileName = self.selectFile("Select Image",
            "Image Files (*.png *.bmp *.jpg *.jpeg)",
            self.imageLocation)

        if fileName and fileName != self.imageLocation:
            self.makeChanges()
            self.imageLocation = fileName

    @pyqtSlot()
    def selectVideoFile(self):
        #TODO: update with accepted video files
        fileName = self.selectFile("Select Video",
            "Video Files (*.avi *.mp4 *.flv)",
            self.videoLocation)

        if fileName and fileName != self.videoLocation:
            self.makeChanges()
            self.videoLocation = fileName

    @pyqtSlot()
    def selectAudioFile(self):
        #TODO: update with accepted audio files
        fileName = self.selectFile("Select Audio",
            "Audio Files (*.mp3)",
            self.audioLocation)

        if fileName and fileName != self.audioLocation:
            self.makeChanges()
            self.audioLocation = fileName

    @pyqtSlot()
    def addCard(self):
        cid = create_card(self.stackID)
        qid = get_card_question(cid)
        aid = get_card_answer(cid)

        #create question and answer text assets
        create_asset((qid, None, 'question', '', None, 0, 0, 0, 0,))
        create_asset((None, aid, 'answer', '', None, 0, 0, 0, 0,))

        #reload list of cards
        self.cardIDs = get_stack_cards(self.stackID)

        #start editing new card
        self.switchToCard(cid)
        item = QListWidgetItem("Card " + str(self.cardNum))
        self.listWidget.addItem(item)
        self.cardNum += 1

    def selectFile(self, title, fileOptions, defaultFile=''):
        fileName, _ = QFileDialog.getOpenFileName(self, title, defaultFile, fileOptions)
        return fileName

    def reloadCard(self):
        self.switchToCard(self.cardID)

    #switches window to editing a specific card
    def switchToCard(self, cardID):
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

        self.unsavedChanges = False

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

        #create button for new card
        newCard = QPushButton('Add Card')
        newCard.clicked.connect(self.addCard)
        row.addWidget(newCard)

        row.addStretch(1)

        #create button for main menu
        #button will be fixed against right and top
        back = QPushButton('Study')
        back.clicked.connect(self.enterStudyMode)
        row.addWidget(back)

        self.fullLayout.addLayout(row)

        self.fullLayout.addStretch(1)

        self.cardIDs = get_stack_cards(self.stackID)

        #rest of GUI added here

        #check if there is at least on card and create
        #it if there isn't
        if len(self.cardIDs) > 0:
            self.switchToCard(self.cardIDs[0][0])
            row = QHBoxLayout()

            #TODO: list of cards
            viewCards = QVBoxLayout()
            self.listWidget = QListWidget()
            cardNum = 1
            for self.cardID in self.cardIDs:
                item = QListWidgetItem("Card " + str(cardNum))
        
                self.listWidget.addItem(item)
                cardNum += 1

            self.cardNum = cardNum
            #self.listWidget.itemClicked.connect(self.switchToCard(self.cardIDs[self.listWidget.currentRow()-1][0]))
            viewCards.addWidget(self.listWidget)
     
            row.addLayout(viewCards)

            row.addStretch(2)

            editSplit = QVBoxLayout()

            editArea = QGroupBox('Edit Card')

            #this could potentially be dynamically generated
            #it would be challenging to handle the updates

            editForm = QFormLayout()

            self.front = QTextEdit()
            self.front.setPlainText(self.frontText)
            self.front.textChanged.connect(self.makeChanges)
            editForm.addRow(QLabel('Front text'), self.front)

            self.back = QTextEdit()
            self.back.setPlainText(self.backText)
            self.back.textChanged.connect(self.makeChanges)
            editForm.addRow(QLabel('Back text'), self.back)

            #image file browser
            selectImage = QPushButton('Browse')
            selectImage.clicked.connect(self.selectImageFile)
            editForm.addRow(QLabel('Select Image'), selectImage)

            #video file browser
            selectVideo = QPushButton('Browse')
            selectVideo.clicked.connect(self.selectVideoFile)
            editForm.addRow(QLabel('Select Video'), selectVideo)

            #audio file browser
            selectAudio = QPushButton('Browse')
            selectAudio.clicked.connect(self.selectAudioFile)
            editForm.addRow(QLabel('Select Audio'), selectAudio)

            editArea.setLayout(editForm)

            editSplit.addWidget(editArea)

            saveChangesDialog = QDialogButtonBox(QDialogButtonBox.Save)
            saveChangesDialog.accepted.connect(self.save)

            editSplit.addWidget(saveChangesDialog)

            editSplit.addStretch(1)

            #TODO: add drag/drop components (maybe)
            #could be something else

            row.addLayout(editSplit)

            row.addStretch(1)

            self.fullLayout.addLayout(row)
        else:
            self.addCard()


        self.fullLayout.addStretch(1)

        self.setLayout(self.fullLayout)

        self.show()

    #save changes to database
    def save(self):
        #don't save if a card is not loaded
        if self.cardID is None:
            return

        answerID = get_card_answer(self.cardID)

        #check each field to make sure it has an entry in the db
        if 'question' in self.assetDict:
            aid = self.assetDict['question'][0]
            update_asset(aid, self.front.toPlainText(), None)

        if 'answer' in self.assetDict:
            aid = self.assetDict['answer'][0]
            update_asset(aid, self.back.toPlainText(), None)

        if 'image' in self.assetDict:
            aid = self.assetDict['image'][0]
            update_asset(aid, None, self.imageLocation)
        elif self.imageLocation != '' and not self.imageLocation.isspace():
            create_asset((None, answerID, 'image', None, self.imageLocation, 0, 0, 0, 0,))

        if 'video' in self.assetDict:
            aid = self.assetDict['video'][0]
            update_asset(aid, None, self.videoLocation)
        elif self.videoLocation != '' and not self.videoLocation.isspace():
            create_asset((None, answerID, 'video', None, self.videoLocation, 0, 0, 0, 0,))

        if 'audio' in self.assetDict:
            aid = self.assetDict['audio'][0]
            update_asset(aid, None, self.audioLocation)
        elif self.audioLocation != '' and not self.audioLocation.isspace():
            create_asset((None, answerID, 'audio', None, self.audioLocation, 0, 0, 0, 0,))

        self.unsavedChanges = False

    def reject(self):
        self.reloadCard()
        self.unsavedChanges = False

    #sets the unsavedChanges flag
    #a method is needed because assignment isn't allowed inside of lambda
    #this method is called whenever the textboxes are modified
    @pyqtSlot()
    def makeChanges(self):
        self.unsavedChanges = True

    #check if the content has been saved
    #and save it if the user choses to
    #returns whether it is OK to exit
    def checkSaved(self):
        if self.unsavedChanges:
            reply = QMessageBox.question(self, 'Unsaved changes',
                'Would you like to save your changes?',
                 QMessageBox.Save | QMessageBox.No | QMessageBox.Cancel,
                 QMessageBox.Save)
            if reply == QMessageBox.Save:
                self.save()
            elif reply == QMessageBox.Cancel:
                return False

        return True


    #the MainMenu needs to be opened on close
    #edits need to be checked to unsure nothing is unsaved
    def closeEvent(self, event):
        close = True

        if not self.checkSaved():
            event.ignore()
            return

        openMainMenu(self)
        event.accept()
