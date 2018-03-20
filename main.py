#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication
from db.helpers import *
from MainMenu import *
from ViewStack import *
from EditStack import *

def main():
    # connect to the db
    conn = create_connection("db/flashcards.db")

    initialize_tables(conn)

    #debuging output to see the current set of stacks
    select_all_stacks(conn)

    #create the application
    application = QApplication(sys.argv)

    #testing code to open up specific window from the start
    if len(sys.argv) > 1:
        if sys.argv[1] == 'edit':
            estack = EditStack()
            estack.create()
        elif sys.argv[1] == 'view':
            vstack = ViewStack()
            vstack.create()
    else:
        menu = MainMenu(conn)
        menu.create()

    #wait for application to exit
    sys.exit(application.exec_())


if __name__ == "__main__":
    main()
