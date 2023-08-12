import logging
import os
from logging.handlers import RotatingFileHandler

LogInfo = {"reldir": "log/adtm",
           "basename": "adtm.log",
           "filesize": 48*1024*1024,
           "fbkcount": 6
           }


class Log:
    def __init__(self):
        log_dirname = os.path.join(os.path.expanduser('~'), LogInfo["reldir"])
        if not os.path.exists(log_dirname):
            os.makedirs(log_dirname, exist_ok=True)

        # time_now = time.strftime("%Y-%m-%d--%H-%M-%S")
        logname = os.path.normpath(os.path.join(log_dirname, LogInfo["basename"]))
        formatter = logging.Formatter('%(asctime)s - %(filename)s:%(lineno)d - [%(levelname)s] - %(message)s')

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        # fh = logging.FileHandler(logname, 'a', encoding='utf-8')
        rfh = RotatingFileHandler(filename=logname, mode='a',
                                  maxBytes=LogInfo["filesize"], backupCount=LogInfo["fbkcount"], encoding='utf-8')
        # fh = logging.handlers.TimedRotatingFileHandler(
        #     filename=logname, when='D', interval=1, backupCount=10, encoding='utf-8')
        # fh.suffix = "%Y%m%d-%H%M.log"
        ch.setLevel(logging.INFO)
        rfh.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        rfh.setFormatter(formatter)

        self.logger.addHandler(ch)
        self.logger.addHandler(rfh)


log_inst = Log()

if __name__ == "__main__":
    log_inst.logger.info("test")
