from PyQt5.QtWidgets import *
#表示一个自定义的小部件，专门用于管理一组单选按钮
class RadioButtonWidget(QWidget):
    def __init__(self, button_list):
        #构造函数 __init__ 接受一个参数 button_list，这是一个包含按钮标签的列表
        #调用父类的构造函数 super().__init__()，初始化 QWidget 的基本功能
        super().__init__()
        #创建一个 QButtonGroup 实例，用于管理一组单选按钮。
        # QButtonGroup 允许将多个按钮组合在一起，以便在其中只能选择一个按钮
        self.radio_button_group = QButtonGroup()

        self.radio_button_list = []
        #遍历 button_list 中的每个项目，为每个项目创建一个 QRadioButton 实例，
        # 并将其添加到 self.radio_button_list 中
        for item in button_list:
            self.radio_button_list.append(QRadioButton(item))

        #set first button checked as default
        self.radio_button_list[0].setChecked(True)

        self.radio_button_layout = QHBoxLayout()

        for counter, item in enumerate(self.radio_button_list):
            self.radio_button_layout.addWidget(item)
            self.radio_button_group.addButton(item)
            self.radio_button_group.setId(item, counter)

        self.setLayout(self.radio_button_layout)

    #用于获取当前选中的单选按钮的 ID
    #checkedId() 方法返回当前选中按钮的 ID，如果没有按钮被选中，则返回 -1
    def selected_button(self):
        return self.radio_button_group.checkedId()