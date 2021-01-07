'''
pytest脚本：
1.文件以test_开头
2.测试类以Test开头
3.测试函数或者方法以test_开头
'''

import requests

url = "http://jy001:8081/futureloan/mvc/api/member/register"


def test_register_001():
    cs = {"mobilephone": "18017965357", "pwd": "1234356"}
    r = requests.post(url, data=cs)
    # print(r.text)
    assert r.json()['code'] == '20110'
    assert r.json()['msg'] == "手机号码已被注册"


def test_register_002():
    cs = {"mobilephone": "18017866357", "pwd": "12345"}
    r = requests.post(url, data=cs)
    assert r.json()['code'] == '20108'
    assert r.json()['msg'] == '密码长度必须为6~18'


def test_register_003():
    cs = {"mobilephone": "18017865357"}
    r = requests.post(url, data=cs)
    # print(r.text)
    assert r.json()['code'] == '20103'
    assert r.json()['msg'] == '密码不能为空'
