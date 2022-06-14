#encoding:utf-8
import enum

class URLConfig(enum.Enum):
    '''环境配置信息'''
    url_mapping={
        'dev': 'https://phone.yuntingai.com',
        'test': 'http://192.168.21.21:6003',
        'beat': 'https://ironfist.yuntingai.com'
    }

    '''不同环境的登录信息'''
    user={
        'dev': 'liudongqin2@skieer.com/Aa123456',
        'test': 'mazda_test02@skieer.com/Aa123456',
        'beat': 'liudongqin1@skieer.com/Aa123456'
    }

    '''不同环境的项目信息'''
    project = {
        'dashboard': 'cd5679176c5e4df7a1a6b208e3722454',
    }

    login_url=r'/api/login'

if __name__=="__main__":
    print(URLConfig.login_url.value)
    print(URLConfig.url_mapping.name)
    print(URLConfig.url_mapping.value)
    print(URLConfig.url_mapping.value['dev'])
    print(URLConfig.user.value)
    print(URLConfig.project.value['dashboard'])