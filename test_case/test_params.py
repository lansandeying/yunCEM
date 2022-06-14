# encoding: utf-8
"""
customer profile模块
"""
import os
import allure
import pytest

import logging

logger = logging.getLogger(__name__)
logger.info("params模块日志")

test_datas = [
    ({"username": "yoyo1", "password": "123456"}, "success!"),
    ({"username": "yoyo2", "password": "123456"}, "failed!"),
    ({"username": "yoyo3", "password": "123456"}, "success!"),
]

@allure.feature("params模块")
@pytest.mark.webtest
class TestParams(object):
    """
        /api/ironfist/contact/tag/v2/list
    """

    @allure.story("params(验证数据驱动)")
    @pytest.mark.parametrize("test_input,expected",
                             test_datas
                             )
    def test_001_params(self, test_input,expected):

        try:
            logger.info(test_input["username"])
            logger.info(test_input["password"])
            logger.info(expected)


            # assert json_req.get('code') == 20000
            # assert json_req.get('result')[0]['name'] == "曾昭测试"
        except Exception as e:
            logger.error("报错结果%s" %e)
            raise
        finally:
            logger.info("测试params完成")

if __name__ == "__main__":
    pytest.main(["-s", "test_params.py","--cmdopt=test"])
