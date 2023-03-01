import os
import re
import sys
import threading

from plotly import graph_objects as go
from plotly.offline import plot
from PySide6.QtGui import QIcon, QIntValidator, QPixmap
from PySide6.QtWidgets import (QApplication, QFileDialog, QMainWindow,
                               QMessageBox)

import globalvar as gl
import logwrapper
import resrc.rc_resource as res
from guide import UserGuide
from ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.log = logwrapper.log_instance
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.uguide = UserGuide()
        self.init_var()
        self.init_gui()

    def init_var(self):
        self.draw_dict = {}
        self.dialog = QFileDialog()
        self.msgbox = QMessageBox()
        self.key_words = ["inverval_max", "interval_min", "inverval_mean"]
        # self.min_pattern = re.compile(r"interval_min:(\d+) ms")      # interval_min:0 ms
        # self.mean_pattern = re.compile(r"inverval_mean:(\d+) ms")    # inverval_mean:8 ms
        self.max_pattern = re.compile(r"inverval_max:(\d+) ms")        # inverval_max:11 ms
        self.alsanode_pattern = re.compile(r"alsa node\((.*)\) adtm")  # alsa node(pcmMicRefIn_c) adtm

    def init_gui(self):
        self.setWindowTitle(f'{gl.GuiInfo["proj"]} {gl.GuiInfo["version"]}')
        adtm_icon = QIcon(QPixmap(":/icon/adtm_icon"))
        self.setWindowIcon(adtm_icon)
        self.ui.periodLineEdit.setText("8")
        self.ui.bufferLineEdit.setText("24")
        self.ui.guideTextEdit.setStyleSheet(u"background-color: rgb(231, 234, 237);")
        self.ui.selectButton.clicked.connect(self.call_select_bt)
        self.ui.drawButton.clicked.connect(self.call_draw_bt)
        self.ui.actionExit.triggered.connect(self.action_exit)
        self.ui.actionOpenLog.triggered.connect(self.action_open_log)
        self.ui.actionUserGuide.triggered.connect(self.action_user_guide)
        self.ui.actionAbout.triggered.connect(self.action_about)

        self.ui.periodLineEdit.setValidator(QIntValidator())
        self.ui.bufferLineEdit.setValidator(QIntValidator())
        self.ui.guideTextEdit.setReadOnly(False)
        self.ui.guideTextEdit.setText(gl.GuideTips)
        self.ui.guideTextEdit.setReadOnly(True)

    def call_select_bt(self):
        all_log_list = []
        alsanode_list = []

        self.dialog.setFileMode(QFileDialog.AnyFile)
        self.dialog.setViewMode(QFileDialog.Detail)
        if not self.dialog.exec():
            return False
        file_name = self.dialog.selectedFiles()[0]
        self.log.info(f"Log file: {file_name}")
        self.ui.logLineEdit.setText(file_name)
        self.ui.comboBox.clear()

        try:
            with open(file_name, mode='r', encoding="utf-8", errors="ignore") as fp:
                all_log_list = fp.readlines()
        except Exception as e:
            msgtext = "Error of opening log file"
            self.log.error(f'{msgtext}: {e}')
            self.msgbox.critical(self, "Error", msgtext)  # warning, information, about, question
            return False

        for item in all_log_list:
            _alsanode = self.alsanode_pattern.findall(item)
            if _alsanode and _alsanode[0] not in alsanode_list:
                alsanode_list.append(_alsanode[0])
        if not alsanode_list:
            msgtext = "No alsa node be found in log file"
            self.log.info(msgtext)
            self.msgbox.information(self, "Info", msgtext)
            return False
        self.ui.comboBox.addItems(alsanode_list)
        self.ui.comboBox.setCurrentIndex(0)

    def call_draw_bt(self):
        msgtext = ""
        log_file = self.ui.logLineEdit.text().strip()
        period_time = self.ui.periodLineEdit.text().strip()
        buffer_time = self.ui.bufferLineEdit.text().strip()
        alsa_node = self.ui.comboBox.currentText().strip()

        if not os.path.exists(log_file):
            msgtext = "No log file be selected"
        elif not alsa_node:
            msgtext = "No alsa node be selected"
        elif not period_time:
            msgtext = "No period time be found"
        elif not buffer_time:
            msgtext = "No buffer time be found"
        if msgtext:
            self.log.warning(msgtext)
            self.msgbox.warning(self, "Warning", msgtext)
            return False

        self.draw_dict.clear()
        self.draw_dict["log_file"] = log_file
        self.draw_dict["alsa_node"] = alsa_node
        try:
            self.draw_dict["period_time"] = int(period_time)
            self.draw_dict["buffer_time"] = int(buffer_time)
        except Exception:
            msgtext = "Check the type of period_time or buffer_time"
            self.log.error(msgtext)
            self.msgbox.critical(self, "Error", msgtext)
            return False

        draw_thread = threading.Thread(target=self.drawing_thread, daemon=True, name="Draw Thread")
        draw_thread.start()

    def drawing_thread(self):
        all_log_list = []
        target_log_list = []
        data_dict = {}

        try:
            with open(self.draw_dict["log_file"], mode='r', encoding="utf-8", errors="ignore") as fp:
                all_log_list = fp.readlines()
        except Exception:
            msgtext = "Error of opening log file"
            self.log.error(msgtext)
            self.msgbox.critical(self, "Error", msgtext)
            return False

        target_log_list = [item for item in all_log_list if re.search(
            self.draw_dict["alsa_node"], item, re.I) and self.key_words[0] in item]
        # print(target_log_list)
        if not target_log_list:
            msgtext = "No data be found in log file"
            self.log.error(msgtext)
            self.msgbox.critical(self, "Error", msgtext)
            return False
        actual_time_list = [int(self.max_pattern.findall(item)[0]) for item in target_log_list]
        if len(actual_time_list) > 10:
            del actual_time_list[:5]
            del actual_time_list[-5:]
        # print(actual_time_list)
        data_dict["x"] = list(range(0, len(actual_time_list), 1))
        data_dict["y1"] = [self.draw_dict["period_time"]] * len(actual_time_list)
        data_dict["y2"] = [self.draw_dict["buffer_time"]] * len(actual_time_list)
        data_dict["y3"] = actual_time_list

        fig = go.Figure()
        trace_period = go.Scatter(x=data_dict["x"], y=data_dict["y1"], name="period_time",
                                  mode="markers+lines", line=dict(color="green"))
        trace_buffer = go.Scatter(x=data_dict["x"], y=data_dict["y2"], name="buffer_time",
                                  mode="markers+lines", line=dict(color="red"))
        trace_actual = go.Scatter(x=data_dict["x"], y=data_dict["y3"], name="actual_time",
                                  mode="markers+lines", line=dict(color="blue"))
        fig.add_trace(trace_period)
        fig.add_trace(trace_actual)
        fig.add_trace(trace_buffer)

        fig.update_layout(title=self.draw_dict["alsa_node"],
                          xaxis_title='unit: second', yaxis_title='unit: ms', legend_font_size=16)
        # _data = [trace_period, trace_actual, trace_buffer]
        # _layout = go.Layout(title=self.draw_dict["alsa_node"], xaxis=dict(
        #     title='unit: second'), yaxis=dict(title='unit: ms'), legend=dict(font_size=16))
        # fig = go.Figure(data=_data, layout=_layout)

        plot(fig, filename=f'adtm_test_{self.draw_dict["alsa_node"]}.html')

    def action_exit(self):
        sys.exit()

    def action_open_log(self):
        if "nt" in os.name:
            dbg_dirname = os.path.normpath(os.path.join(
                logwrapper.LogInfo["win_tmp"], logwrapper.LogInfo["dbg_reldir"]))
            # subprocess.Popen(f'explorer.exe {dbg_dirname}', close_fds=True)
            os.startfile(dbg_dirname)
        else:
            dbg_dirname = os.path.join(os.path.expanduser('~'), logwrapper.LogInfo["dbg_reldir"])
            # subprocess.Popen(f'xdg-open {dbg_dirname}', close_fds=True)
            os.system(f'xdg-open {dbg_dirname}')

    def action_about(self):
        self.msgbox.information(self, "About", gl.AboutInfo)

    def action_user_guide(self):
        self.uguide.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
