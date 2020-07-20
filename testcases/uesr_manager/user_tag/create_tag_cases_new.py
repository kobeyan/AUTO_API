#！/usr/bin.env python
# encoding: utf-8
# @author: kobe
# @File : create_tag_cases_new.py
# @time: 2020/7/19 19:59 
import unittest
import requests
from common.localconfig_utils import Local_cfg
from common.log_utils import Logger
from common import common_api

class CreateTag(unittest.TestCase):

    def setUp(self) -> None:
        self.session = requests.session()

    def tearDown(self) -> None:
        pass

    def test_add_tag(self):
        self._testMethodDoc = "开始测试正常创建用户标签接口"
        Logger.info("开始测试创建用户标签")

        add_tag_response = common_api.creart_user_tag_api(self.session,tagname="kobe006")
        add_tag_result = add_tag_response.json()["tag"]["name"]
        self.assertEqual(add_tag_result,'kobe006')

    def test_add_repeat_tag(self):
        self._testMethodDoc = "开始测试重复名创建用户标签接口"
        Logger.info("开始测试创建用户标签")

        add_tag_response = common_api.creart_user_tag_api(self.session,tagname="kobe001")
        add_tag_result = add_tag_response.json()["errcode"]
        self.assertEqual(add_tag_result,45157)


if __name__ == '__main__':
    unittest.main()