# coding:utf-8
import pytest
from config.url_config import URLConfig
from common.http_request import HTTPRequests
from common.logger import logger

logger = logger()

def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt",action="store",default="test", choices=['dev', 'test'],help="my env option:dev or test"
    )

@pytest.fixture(scope='session')
def get_cmdopt(request):
    return request.config.getoption("--cmdopt")

@pytest.fixture(autouse=True)
def http(request):

    env = request.getfixturevalue("get_cmdopt")#同级的fixture，获取对应方法名的方法return的返回值
    url_mapping = URLConfig.url_mapping.value#取到枚举url_mapping的值，存数据方式为字典
    url = url_mapping.get(f'{env}') #这里相当于url_mapping.value['test']
    http = HTTPRequests(url) #将获取的环境url结果，传给封装好的requests
    return http

@pytest.fixture()
def login(request):
    get_userName=request.param
    return get_userName


@pytest.fixture(scope='session')#调用登录，且满足所有被测case，用的是一个token
def get_token_head(request):
    env = request.getfixturevalue("get_cmdopt")  # 同级的fixture，获取对应方法名的方法return的返回值
    url_mapping = URLConfig.url_mapping.value  # 取到枚举url_mapping的值，存数据方式为字典
    url = url_mapping.get(f'{env}')  # 这里相当于url_mapping.value['test']
    http = HTTPRequests(url)  # 将获取的环境url结果，传给封装好的requests

    user = URLConfig.user.value #这里拿到枚举user的值
    user_list = user.get(f'{env}').split("/")#根据命令行执行的结果，拿到登录的账号和密码，以split分割
    username = user_list[0]  #账号
    password = user_list[1]  #密码

    param = {'username': username,
             'password': password }

    logger.info("请求的url=={}".format(url)) #打印请求的地址

    response = http.post(uri=URLConfig.login_url.value, data=param)
    Authorization = response.headers["Authorization"]
    logger.info("获取的返回值是=={}".format(Authorization))
    token = None
    if response.status_code == 200:
        token = "Bearer" + " " + response.headers["Authorization"]
    else:
        token = 'get token fail'

    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Accept': 'image/gif, image/jpeg, image/pjpeg, application/x-ms-application, application/xaml+xml, '
                  'application/x-ms-xbap, application/vnd.ms-excel, application/vnd.ms-powerpoint, '
                  'application/msword, */*',
        'Accept-Language': 'zh-CN',
        'Cookie': "Hm_lvt_1b04138eba9c963fa12d5a2d7bc72fb8=1650956876; SESSION=MjU5MDY1ZTAtMjkxNC00Y2UwLThjMDYtY2E3NzE3NjlmN2Q4; JSESSIONID=09001767DB54AAD08FFF686FC3BE3E71",
                  'Authorization': token}
    yield head