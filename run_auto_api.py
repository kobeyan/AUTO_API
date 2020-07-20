#！/usr/bin.env python
# encoding: utf-8
# @author: kobe
# @File : run_auto_api.py
# @time: 2020/7/18 21:49
import os
import unittest
from common import HTMLTestReportCN
from common.localconfig_utils import Local_cfg

def get_all_cases():

    discover = unittest.defaultTestLoader.discover(
        start_dir = './testcases',
        pattern = '*_new.py',
        top_level_dir = './testcases'
    )
    all_cases_suite = unittest.TestSuite()
    all_cases_suite.addTest(discover)
    return all_cases_suite



report_dir = HTMLTestReportCN.ReportDirectory( Local_cfg.REPORT_PATH + '/' )

report_dir.create_dir('API_TEST_')
report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
with open(report_path,'wb') as fp:
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                             tester="kobe",
                                             title="哈哈哈啊发",
                                             description="Study_Test")
    runner.run(get_all_cases())
fp.close()

