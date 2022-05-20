# encoding: utf-8

import requests
import urllib3
# from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings()
# 加这句不会报错(requests证书警告)
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class HTTPRequests(object):
    def __init__(self, url):
        self.url = url
        self.req = requests.session()
        # 依据自己公司的请求头默认值配置
        self.head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Accept': 'image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, '
                      'application/x-ms-xbap, application/vnd.ms-excel, application/vnd.ms-powerpoint, '
                      'application/msword, */*',
            'Accept-Language': 'zh-CN'}

    # 封装自己的get请求，获取资源
    def get(self, uri='', params='', data='', headers=None, cookies=None, verify=False):
        if headers is None:
            headers = self.head
        # print("请求头是:{}".format(headers))
        url = self.url + uri
        response = self.req.get(url, params=params, data=data, headers=headers, cookies=cookies, verify=verify)
        return response

    # 封装自己的post请求，获取资源
    def post(self, uri='', params='', data='', headers=None, cookies=None, verify=False):
        if headers is None:
            headers = self.head
        url = self.url + uri
        response = self.req.post(url, params=params, data=data, headers=headers, cookies=cookies, verify=verify)
        return response