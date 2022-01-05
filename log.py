import os
import time
import logging
import global_var as gl


class Log:
    def __init__(self):
        if not os.path.exists(gl.Gui_Info["dbg_dir"]):
            os.makedirs(gl.Gui_Info["dbg_dir"], exist_ok=True)
        self.now = time.strftime("%Y-%m-%d--%H-%M-%S")
        self.logname = os.path.join(gl.Gui_Info["dbg_dir"], f'{self.now}.log')

    def __printconsole(self, level, message):
        # 创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')
        # fh = logging.handlers.TimedRotatingFileHandler(
        #     filename=self.logname, when='D', interval=1, backupCount=10, encoding='utf-8')
        # fh.suffix = "%Y%m%d-%H%M.log"
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('[%(asctime)s] - %(filename)s [Line:%(lineno)d] - [%(levelname)s] - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)

        # 记录一条日志
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)

        # 记录完日志移除句柄Handler
        logger.removeHandler(ch)
        logger.removeHandler(fh)

        # 关闭打开的文件
        fh.close()

    def debug(self, message):
        self.__printconsole('debug', message)

    def info(self, message):
        self.__printconsole('info', message)

    def warning(self, message):
        self.__printconsole('warning', message)

    def error(self, message):
        self.__printconsole('error', message)


if __name__ == "__main__":
    log = Log()
    log.info("test")
