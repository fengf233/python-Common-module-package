#coding:utf-8
import logging
import time,os
'''
    使用方法：
    import MyLog
    log = MyLog.Log().getlog()
    log.debug("###")
'''
class Log():

    def __init__(self):

        self.logger = logging.getLogger("mylog")
        self.logger.setLevel(logging.DEBUG)
        self.log_time = "\\"+time.strftime("%Y-%m-%d", time.localtime())+".log"
        self.log_path = os.path.join(os.getcwd() + "\\test log")
        if os.path.exists(self.log_path) and os.path.isdir(self.log_path):
            pass
        else:
            os.mkdir(self.log_path)
        self.log_name = os.path.join(self.log_path + self.log_time)

        #logging.basicConfig(filename=self.log_name)
        fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        formatter = logging.Formatter('[%(levelname)s][%(asctime)s] [%(filename)s]->[%(funcName)s] line:%(lineno)d ---> %(message)s')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

if __name__ == "__main__":
    log = Log().getlog()
    log.debug("hello")