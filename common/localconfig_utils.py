#！/usr/bin.env python
# encoding: utf-8
# @author: kobe
# @File : localconfig_utils.py
# @time: 2020/7/11 18:46
import configparser
import os

pro_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(pro_path,"config/config.ini")

class Localconfig_Utils():

    def __init__(self,cfg_path = config_path):
        self.cfg_path = cfg_path
        self.cfg = configparser.ConfigParser()
        self.cfg.read(self.cfg_path)

    @property
    def URL(self):
        url_value = self.cfg.get("default","URL")
        return url_value

    # @property
    # def CASE_DATA_PATH(self):
    #     CASE_DATA_PATH_value = self.cfg.get("path","CASE_DATA_PATH")
    #     return CASE_DATA_PATH_value


    @property
    def REPORT_PATH(self):
        REPORT_PATH = self.cfg.get("path","REPORT_PATH")
        return REPORT_PATH

    @property
    def LOG_PATH(self):
        LOG_PATH = self.cfg.get("path","LOG_PATH")
        return LOG_PATH

    @property
    def grant_type(self):
        grant_type = self.cfg.get("default","grant_type")
        return grant_type

    @property
    def appid(self):
        appid = self.cfg.get("default","appid")
        return appid

    @property
    def secret(self):
        secret = self.cfg.get("default","secret")
        return secret

    @property
    def LOG_LEVEL(self):
        LOG_LEVEL = self.cfg.get("log", "LOG_LEVEL")
        return LOG_LEVEL


Local_cfg = Localconfig_Utils()

if __name__ == '__main__':
    print(Local_cfg.REPORT_PATH)