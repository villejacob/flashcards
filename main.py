#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication
from mainMenu import *
from viewStack import *
from editStack import *

def main():
    #create the application
    application = QApplication(sys.argv)

    #testing code to open up specific window from the start
    if len(sys.argv) > 1:
        if sys.argv[1] == 'edit':
            estack = editStack()
            estack.create()
        elif sys.argv[1] == 'view':
            vstack = viewStack()
            vstack.create()
    else:
        menu = mainMenu()
        menu.create()

    #wait for application to exit
    sys.exit(application.exec_())




if __name__ == "__main__":
    main()
