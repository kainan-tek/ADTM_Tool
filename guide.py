from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon

import globalvar as gl
from ui.guide_ui import Ui_UserGuide


class UserGuide(QWidget):
    def __init__(self):
        super(UserGuide, self).__init__()
        self.ui = Ui_UserGuide()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/icons/adtm"))
        self.ui.guideTextEdit.setReadOnly(False)
        self.ui.guideTextEdit.setText(gl.GuideTips)
        self.ui.guideTextEdit.setReadOnly(True)
