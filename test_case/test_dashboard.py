# encoding: utf-8
"""
customer profile模块
"""
import os
import allure
import pytest

import logging

logger = logging.getLogger(__name__)
logger.info("dashboard模块日志")


@allure.feature("dashboard模块")
@pytest.mark.webtest
# 只想运行某些测试用例，可以在使用mark功能进行标记
# 在pytest.main(["-s", "test_XX.py", "-m=webtest"])#这里运行没有效果，运行结果仍然是两个，
# 在命令行使用pytest -s test_XX.py -m=webtest可以成功，仅一个用例执行，但是会有警告
# 解决警告的方式
# 新建pytest.ini文件，添加如下代码
# [pytest]
# marks=webtest
class TestDashboard(object):
    """
        /api/dashboard/filter/find/dataset/project_ID
    """

    @pytest.mark.run(order=1)
    @allure.story("dashboard(查看项目下数据集)")
    def test_001_dashboard(self, get_token_head, http):
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
