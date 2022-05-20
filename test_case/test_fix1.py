# coding:utf-8
import pytest

login_data=[{'username':'liu','passwd':'123456'}]

def test_s1():
    print("用例1：登录之后其它动作111")


def test_s2():  # 不传login
    print("用例2：不需要登录，操作222")


def aest_s3():
    print("用例3：登录之后其它动作333")

def test_s4(get_cmdopt,http,get_token_head):
    print(get_cmdopt)
    print(http)
    print(get_token_head)


@pytest.mark.parametrize("login",login_data,indirect=True)
def test_s5(login):
    a=login
    print(a)


if __name__ == "__main__":
    pytest.main(["-s", "test_fix1.py","--cmdopt=dev"])