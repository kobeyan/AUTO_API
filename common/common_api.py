#！/usr/bin.env python
# encoding: utf-8
# @author: kobe
# @File : common_api.py
# @time: 2020/7/19 20:00
import requests

from common.localconfig_utils import Local_cfg


def get_access_token_api(session,grant_type,appid,secret):

    params = {
        'grant_type': grant_type,
        'appid': appid,
        'secret': secret
    }
    response = session.get(
        url=Local_cfg.URL + '/cgi-bin/token',
        params=params
    )
    return response

def get_access_token_value(session):
    get_response = get_access_token_api(session,
                                        grant_type = Local_cfg.grant_type,
                                        appid = Local_cfg.appid,
                                        secret = Local_cfg.secret)
    access_token = get_response.json()["access_token"]
    return access_token

def creart_user_tag_api(session,tagname):

    access_token = get_access_token_value(session)
    get_params = {'access_token':access_token}

    data_params = { "tag" : { "name" : tagname } }
    headers = {'content_type' : 'application/json'}

    add_tag_response = session.post(
        url = Local_cfg.URL + '/cgi-bin/tags/create',
        params = get_params,
        json = data_params,
        headers = headers
    )
    return add_tag_response
