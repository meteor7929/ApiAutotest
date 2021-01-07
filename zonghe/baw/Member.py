'''
用户接口模块，按模块管理（都是member模块中的）
'''


def register(url, baserequests, data):
    '''
    注册接口
    :param url: 环境数据，比如http://jy001:8081/
    :param baserequests: BaseRequests的实例
    :param data: 注册的数据
    :return: 响应
    '''
    url = url + "/futureloan/mvc/api/member/register"
    return baserequests.post(url, data=data)


# 登录接口
def login(url,baserequests,data):
    '''
    登录接口
    :param url: 环境数据，比如http://jy001:8081/
    :param baserequests: BaseRequests的实例
    :return: 响应
    '''
    url = url + "/futureloan/mvc/api/member/login"
    return baserequests.post(url,data=data)


# 查询接口
def query(url, baserequests):
    '''
    查询接口
    :param url: 环境数据，比如http://jy001:8081/
    :param baserequests: BaseRequests的实例
    :return: 响应
    '''
    url = url + "/futureloan/mvc/api/member/list"
    return baserequests.post(url)
