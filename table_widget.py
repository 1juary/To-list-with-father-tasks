from PyQt5.QtWidgets import *

from db_controller import *

class TableWidget(QTableWidget):

    def __init__(self):
        super().__init__()
        self.controller = DbController("to_do.db")

        self.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

    def show_items(self, item_list):
        if len(item_list) == 0:
            self.setRowCount(0)
        else:
            row = 0
            for entry in item_list:
                self.setRowCount(row+1)
                column = 0
                for item in entry:
                    if item == None:
                        item = ""
                    elif column == 3:
                        item = str(item[:-7])
                    table_item = QTableWidgetItem(str(item))
                    self.setItem(row, column, table_item)
                    column += 1
                row += 1
        
class TasksTable(TableWidget):

    def __init__(self):
        super().__init__()

        self.setColumnCount(6)
        self.setHorizontalHeaderLabels(["TaskID", "Decription", "Deadline", "Created", "Completed", "ProjectID"])

    def get_tasks(self, task_type):
        if task_type == 0:
            tasks = self.controller.get_active_tasks()
        elif task_type == 1:
            tasks = self.controller.get_completed_tasks()
        else:
            tasks = self.controller.get_all_tasks()
        return tasks





class ProjectsTable(TableWidget):

    def __init__(self):
        super().__init__()
        
        self.setColumnCount(5)
        self.setHorizontalHeaderLabels(["ProjectID", "Decription", "Deadline", "Created", "Completed"])

    def get_projects(self, project_type):
        if project_type == 0:
            projects = self.controller.get_active_projects()
        elif project_type == 1:
            projects = self.controller.get_completed_projects()
        else:
            projects = self.controller.get_all_projects()
        return projects