# encoding: utf-8
"""
customer profile模块
"""
import os
import allure
import pytest

import logging

logger = logging.getLogger(__name__)
logger.info("customer profile模块日志")


@allure.feature("customer profile模块")
@pytest.mark.webtest
class TestCustomerProfile(object):
    """
        /api/ironfist/contact/tag/v2/list
    """

    @allure.story("customer(查询用户成就信息)")
    def test_001_customer(self, get_token_head, http):
        logger.info("--------")
        uri = '/api/ironfist/contact/tag/v2/list'
        header = get_token_head

        try:
            response = http.post(uri=uri,  headers=header)

            json_req = response.json()
            logger.info("请求结果是:{}".format(json_req))


            # assert json_req.get('code') == 20000
            # assert json_req.get('result')[0]['name'] == "曾昭测试"
        except Exception as e:
            logger.error("报错结果%s" %e)
            raise
        finally:
            logger.info("测试customer完成")
        # else:
        #     response = http.get(uri=uri, params=params)
        #     json_req = response.json()
        #     logger.info("Query_Related_Achievements没有token的返回值是:{}".format(json_req))
        #
        #     assert json_req.get('retCode') == 401
        #     assert json_req.get('message') == result　
if __name__ == "__main__":
    pytest.main(["-s", "test_customer_profile.py","--cmdopt=test"])
