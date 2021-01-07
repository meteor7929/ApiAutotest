import pytest
import requests


# 登录功能的测试数据，列表中的测试数据可以是任意类型的
@pytest.fixture(params=[{'mobilephone': '18695716435', 'pwd': '123456', 'regname': '', 'code': '10001'},
                        {'mobilephone': '18675875485', 'pwd': '123456789012345678', 'regname': '', 'code': '10001'},
                        {'mobilephone': '13645815335', 'pwd': '123456',
                         'regname': '小北小那就好多少级女个我女会计计的内立会计的撒牛刀次无按此陈多少级女个我女会计计的内立会计的撒牛刀次无按此丽娜内立法来看你了安徽阿克江小北小',
                         'code': '20102'},
                        {'mobilephone': '13645714235', 'pwd': '12345', 'regname': '', 'code': '20108'},
                        {'mobilephone': '13645714235', 'pwd': '1234567890123456789', 'regname': '', 'code': '20108'},
                        {'mobilephone': '13645714235', 'pwd': '', 'regname': '', 'code': '20103'},
                        {'mobilephone': '', 'pwd': '123456', 'regname': '', 'code': '20103'},
                        {'mobilephone': '', 'pwd': '', 'regname': '', 'code': '20103'},
                        {'mobilephone': '123', 'pwd': '123456', 'regname': '', 'code': '20109'},
                        {'mobilephone': '113645714235', 'pwd': '123456', 'regname': '', 'code': '20109'},
                        {'mobilephone': '1145714235', 'pwd': '123456', 'regname': '', 'code': '20109'},
                        {'mobilephone': '18675715335', 'pwd': '123456', 'regname': '', 'code': '20110'}
                        ])
def register_data(request):  # request 是pytest 中的关键字，固定写法
    return request.param  # 通过request.param返回每一组数据，固定写法


# 注册功能的测试脚本

def test_register(register_data):
    url = 'http://jy001:8081/futureloan/mvc/api/member/register'
    # cs = {"mobilephone": f"{register_data['mobilephone']}", "pwd": f"{register_data['pwd']}","regname":f"{register_data['regname']}"}
    # r = requests.post(url, data=cs)
    r = requests.post(url, data=register_data)
    print(r.text)
    assert r.json()['code'] == f"{register_data['code']}"
