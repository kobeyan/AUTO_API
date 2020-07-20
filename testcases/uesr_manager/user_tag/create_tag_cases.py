#！/usr/bin.env python
# encoding: utf-8
# @author: kobe
# @File : create_tag_cases.py
# @time: 2020/7/18 21:13
import unittest
import requests
from common.localconfig_utils import Local_cfg
from common.log_utils import Logger


class CreateTag(unittest.TestCase):

    def setUp(self) -> None:
        self.hosts = Local_cfg.URL
        self.session = requests.session()

    def tearDown(self) -> None:
        pass

    def test_add_tag(self):
        self._testMethodDoc = "开始测试正常创建用户标签接口"
        Logger.info("开始测试创建用户标签")

        params = {
            'grant_type':'client_credential',
            'appid':'wxef0b51edf48d2c6d',
            'secret':'cec590dcce71ca2edffe3a54130b988b'
        }
        get_access_token = self.session.get(
            url = self.hosts + '/cgi-bin/token',
            params = params
        )

        access_token = get_access_token.json()['access_token']
        get_params = {'access_token':access_token}
        data_params = '{ "tag" : { "name" : "kobe789" } }'
        headers = {'content_type' : 'application/json'}
        add_tag_response = self.session.post(
            url = self.hosts + '/cgi-bin/tags/create',
            params = get_params,
            data = data_params,
            headers = headers
        )

        print(add_tag_response.text)
        add_tag_result = add_tag_response.json()["tag"]["name"]
        self.assertEqual(add_tag_result,'kobe789')

if __name__ == '__main__':
    unittest.main()