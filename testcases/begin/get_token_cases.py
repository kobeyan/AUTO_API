#！/usr/bin.env python
# encoding: utf-8
# @author: kobe
# @File : get_token_cases.py
# @time: 2020/7/18 20:31 

import requests
import unittest

from common.localconfig_utils import Local_cfg
from common.log_utils import Logger


class GetToken(unittest.TestCase):

    def setUp(self) -> None:
        self.hosts = Local_cfg.URL
        self.session = requests.session()

    # def tearDown(self) -> None:
    #     pass

    def test_get_access_token(self):
        self._testMethodDoc = '测试正常获取access_token时'
        #Logger.info("开始测试正常获取access_token")
        params = {
            'grant_type':'client_credential',
            'appid':'wxef0b51edf48d2c6d',
            'secret':'cec590dcce71ca2edffe3a54130b988b'
        }
        response = self.session.get(
            url = self.hosts + '/cgi-bin/token',
            params = params
        )
        self.assertEqual(response.json()['expires_in'],7200)

    def test_secret_errp(self):
        self._testMethodDoc = '测试获取access_token时secret错误'
        #Logger.info("开始测试获取access_token时secret错误")
        params = {
            'grant_type': 'client_credential',
            'appid': '123',
            'secret': 'cec590dcce71ca2edffe3a54130b988b'
        }
        response = self.session.get(
            url=self.hosts + '/cgi-bin/token',
            params = params
        )
        self.assertEqual(response.json()['errcode'], 40013)

if __name__ == '__main__':
    unittest.main()