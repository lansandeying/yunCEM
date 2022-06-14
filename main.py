#coding:utf-8

uri = '/api/ironfist/contact/tag/v2/list'
        header = get_token_head
        try:
            response = http.post(uri=uri,  headers=header)

            json_req = response.json()
            logger.info("请求结果是:{}".format(json_req))


            assert json_req.get('code') == 20000
            assert json_req.get('result')[0]['name'] == "曾昭测试"
        except Exception as e:
            logger.error("报错结果%s" %e)
            raise
        finally:
            logger.info("测试customer完成")
