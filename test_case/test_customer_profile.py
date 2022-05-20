# encoding: utf-8
"""
customer profile模块
"""
from common.logger import logger
import os
import allure
import pytest


logger().info("customer profile模块日志")


@allure.feature("customer profile模块")
@pytest.mark.webtest
class TestCustomerProfile(object):
    """
        /api/ironfist/contact/tag/v2/list
    """

    @allure.story("Query Related Achievements(查询用户成就信息)")
    def test_001_customer(self, get_token_head, http):
        uri = '/api/ironfist/contact/tag/v2/list'
        # data={"id":"4dc11c917a994d12aacd1a3230d4dfe8"}

        # if istoken == 'yes':
        header = get_token_head
        logger().info(header)
        response = http.post(uri=uri,  headers=header)
        # logger.info(response.headers)
        logger().info(response.url)
        json_req = response.text
        logger().info("请求结果是:{}".format(json_req))
        # logger.info()

        #     assert json_req.get('retCode') == 200
        #     assert json_req.get('result')[0]['smallImg'] == result
        # else:
        #     response = http.get(uri=uri, params=params)
        #     json_req = response.json()
        #     logger.info("Query_Related_Achievements没有token的返回值是:{}".format(json_req))
        #
        #     assert json_req.get('retCode') == 401
        #     assert json_req.get('message') == result　
if __name__ == "__main__":
    pytest.main(["-s", "test_customer_profile.py","--cmdopt=dev"])