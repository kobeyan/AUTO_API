#！/usr/bin.env python
# encoding: utf-8
# @author: kobe
# @File : log_utils.py
# @time: 2020/7/11 19:22 
import logging
import os
import time

from common.localconfig_utils  import Local_cfg

current_path = os.path.dirname(__file__)
log_output_path = os.path.join( current_path,'..', Local_cfg.LOG_PATH  )

class Log_utils():

    def __init__(self,log_path = log_output_path):

        self.log_name = os.path.join(log_path,'ApiTest_%s.log'%time.strftime('%Y_%m_%d'))
        print(self.log_name)
        self.logger = logging.getLogger()
        self.logger.setLevel(Local_cfg.LOG_LEVEL)

        handler1 = logging.StreamHandler()
        # handler1.setLevel(logging.INFO)

        handler2 = logging.FileHandler(self.log_name,"a",encoding="utf-8")
        # handler2.setLevel(logging.INFO)

        formarter = logging.Formatter("%(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s:%(message)s")
        handler1.setFormatter(formarter)
        handler2.setFormatter(formarter)

        self.logger.addHandler(handler1)
        self.logger.addHandler(handler2)

        handler1.close()
        handler2.close()

    def get_logger(self):
        return self.logger


Logger = Log_utils().get_logger()

if __name__ == '__main__':
    Logger.info("hello,kobe")
