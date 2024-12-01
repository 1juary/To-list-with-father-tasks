import sys
import os

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from create_new_db import *
from tab_widget import *
import sqlite3
verbindung = sqlite3.connect("to_do.db")
zeiger = verbindung.cursor()

sql_anweisung = """
CREATE TABLE IF NOT EXISTS Tasks (
TaskID integer,
Description text,
Deadline date,
Created timestamp,
Completed timestamp,
ProjectID integer,
PRIMARY KEY(TaskID),
FOREIGN KEY(ProjectID) REFERENCES Projects(ProjectID)
);"""

zeiger.execute(sql_anweisung)

sql_anweisung = """
CREATE TABLE IF NOT EXISTS Projects (
ProjectID integer,
Description text,
Deadline date,
Created timestamp,
Completed timestamp,
PRIMARY KEY(ProjectID)
);"""

zeiger.execute(sql_anweisung)
verbindung.close()


class ToDoWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("To Do List")
        self.setMinimumHeight(300)

        self.central_widget = TaskProjectTabs()
        self.setCentralWidget(self.central_widget)

        self.central_widget.task_exit_button.clicked.connect(self.close)
        self.central_widget.project_exit_button.clicked.connect(self.close)

if __name__ == "__main__":
    to_do = QApplication(sys.argv)
    main_window = ToDoWindow()
    main_window.show()
    main_window.raise_()
    #creates new database when run for the first time
    if not os.path.exists("to_do.db"):
        create_new_db("to_do.db")
        new_db = QMessageBox()
        new_db.setWindowTitle("New Database")
        new_db.setText("New database created")
        new_db.exec_()
    to_do.exec_()
