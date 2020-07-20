#！/usr/bin.env python
# encoding: utf-8
# @author: kobe
# @File : get_token_cases_new.py
# @time: 2020/7/19 19:58 
#！/usr/bin.env python
# encoding: utf-8
# @author: kobe
# @File : get_token_cases.py
# @time: 2020/7/18 20:31

import requests
import unittest

from common.localconfig_utils import Local_cfg
from common.log_utils import Logger
from common import common_api


class GetToken(unittest.TestCase):

    def setUp(self) -> None:
        self.session = requests.session()

    def tearDown(self) -> None:
        pass

    def test_get_access_token(self):
        self._testMethodDoc = '测试正常获取access_token时'
        Logger.info("开始测试正常获取access_token")
        response = common_api.get_access_token_api(self.session,
                                       grant_type=Local_cfg.grant_type,
                                       appid=Local_cfg.appid,
                                       secret=Local_cfg.secret)
        self.assertEqual(response.json()['expires_in'],7200)

    def test_secret_errp(self):
        self._testMethodDoc = '测试获取access_token时secret错误'
        Logger.info("开始测试获取access_token时secret错误")

        response = common_api.get_access_token_api(self.session,
                                        grant_type = Local_cfg.grant_type,
                                        appid = Local_cfg.appid,
                                        secret = Local_cfg.secret+"000")
        self.assertEqual(response.json()['errcode'], 40125)

if __name__ == '__main__':
    unittest.main()