from PySide6.QtWidgets import QWidget
from ui.ui_guide import Ui_UserGuide


class UserGuide(QWidget):
    def __init__(self):
        super(UserGuide, self).__init__()
        self.ui = Ui_UserGuide()
        self.ui.setupUi(self)
