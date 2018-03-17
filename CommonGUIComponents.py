from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def openMainMenu(curWindow):
    if curWindow.mainMenu is not None:
        move(curWindow, curWindow.mainMenu)

def openEditWindow(curWindow):
    import EditStack
    curWindow.mainMenu.es = EditStack.EditStack(curWindow.mainMenu,
            curWindow.stackID, curWindow.pos(), curWindow.size())
    curWindow.mainMenu.es.create()

def openViewWindow(curWindow):
    import ViewStack
    curWindow.mainMenu.vs = ViewStack.ViewStack(curWindow.mainMenu,
            curWindow.stackID, curWindow.pos(), curWindow.size())
    curWindow.mainMenu.vs.create()

def move(curWindow, nextWindow):
    #copy size and position over to new window
    nextWindow.move(curWindow.pos())
    nextWindow.resize(curWindow.size())

    #show next window
    nextWindow.show()
