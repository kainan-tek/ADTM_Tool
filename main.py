import os
import sys
import re
import threading
import subprocess
from log import Log
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon, QPixmap
from ui.ui_mainwindow import Ui_MainWindow
from plotly.offline import plot
import plotly.graph_objects as go
import global_var as gl
import resrc.resource as res


class MainWindow(QMainWindow):
    def __init__(self, log):
        super(MainWindow, self).__init__()
        self.log = log
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.gui_setup()
        self.init_var()

    def gui_setup(self):
        self.setWindowTitle(f'{gl.Gui_Info["proj"]} {gl.Gui_Info["version"]}')
        adtm_icon = QIcon(QPixmap(":/icon/adtm_icon"))
        self.setWindowIcon(adtm_icon)
        self.dialog = QFileDialog()
        self.msgbox = QMessageBox()
        self.ui.periodEdit.setText("8")
        self.ui.bufferEdit.setText("24")
        self.ui.selectButton.clicked.connect(self.call_select_bt)
        self.ui.drawButton.clicked.connect(self.call_draw_bt)
        self.ui.actionExit.triggered.connect(self.action_exit)
        self.ui.actionOpen_Log.triggered.connect(self.action_open_log)
        self.ui.actionAbout.triggered.connect(self.action_about)
        # self.ui.comboBox.setStyleSheet("border-width:1;border-style:outset")

    def init_var(self):
        self.draw_dict = {}
        self.gl_bg = "#e7eaed"
        self.key_words = ["inverval_max", "interval_min", "inverval_mean"]
        # self.min_pattern = re.compile(r"interval_min:(\d+) ms")      # interval_min:0 ms
        # self.mean_pattern = re.compile(r"inverval_mean:(\d+) ms")    # inverval_mean:8 ms
        self.max_pattern = re.compile(r"inverval_max:(\d+) ms")        # inverval_max:11 ms
        self.alsanode_pattern = re.compile(r"alsa node\((.*)\) adtm")  # alsa node(pcmMicRefIn_c) adtm

    @Slot()
    def call_select_bt(self):
        all_log_list = []
        alsanode_list = []

        self.dialog.setFileMode(QFileDialog.AnyFile)
        self.dialog.setViewMode(QFileDialog.Detail)
        if not self.dialog.exec():
            return False
        file_name = self.dialog.selectedFiles()[0]
        self.log.info(f"Log file: {file_name}")
        self.ui.logEdit.setText(file_name)
        self.ui.comboBox.clear()

        try:
            with open(file_name, mode='r', encoding="utf-8", errors="ignore") as fp:
                all_log_list = fp.readlines()
        except Exception as e:
            msgtext = "'Error of opening log file"
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
        log_file = self.ui.logEdit.text().strip()
        period_time = self.ui.periodEdit.text().strip()
        buffer_time = self.ui.bufferEdit.text().strip()
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
        data_dict["x"] = [i for i in range(len(actual_time_list))]
        data_dict["y1"] = [self.draw_dict["period_time"] for item in actual_time_list]
        data_dict["y2"] = [self.draw_dict["buffer_time"] for item in actual_time_list]
        data_dict["y3"] = actual_time_list

        trace_period = go.Scatter(x=data_dict["x"], y=data_dict["y1"], name="period_time",
                                  mode="markers+lines", line=dict(color="green"))
        trace_buffer = go.Scatter(x=data_dict["x"], y=data_dict["y2"], name="buffer_time",
                                  mode="markers+lines", line=dict(color="red"))
        trace_actual = go.Scatter(x=data_dict["x"], y=data_dict["y3"], name="actual_time",
                                  mode="markers+lines", line=dict(color="blue"))
        _data = [trace_period, trace_actual, trace_buffer]
        _layout = go.Layout(title=self.draw_dict["alsa_node"], xaxis=dict(
            title='unit: second'), yaxis=dict(title='unit: ms'), legend=dict(font_size=16))

        fig = go.Figure(data=_data, layout=_layout)
        plot(fig, filename=f'adtm_test_{self.draw_dict["alsa_node"]}.html')

    def action_exit(self):
        sys.exit()

    def action_open_log(self):
        os.makedirs(gl.Gui_Info["dbg_dir"], mode=0o777, exist_ok=True)
        subprocess.Popen(f'start {gl.Gui_Info["dbg_dir"]}', shell=True)
        # os.system("start %s" % gl.Gui_Info["debug_dir"])

    def action_about(self):
        self.msgbox.information(self, "About", gl.About_Info)


if __name__ == "__main__":
    log = Log()
    app = QApplication(sys.argv)
    window = MainWindow(log)
    window.show()
    sys.exit(app.exec())
