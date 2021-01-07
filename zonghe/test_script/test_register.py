'''
注册的测试脚本
'''

# 注册失败的测试脚本
import pytest

from zonghe.baw import Member, Db
from zonghe.caw import DataRead, Asserts


# pytest 数据驱动的方式
# 从yaml中读取测试数据
@pytest.fixture(params=DataRead.read_yaml(r'data_case/register_fail.yaml'))
def fail_data(request):
    return request.param


def test_register_fail(url, baserequests, fail_data):
    # 下发注册的请求
    r = Member.register(url, baserequests, fail_data['data'])
    # 断言响应的结果
    print(r.text)
    # assert r.json()['code'] == fail_data['expect']['code']
    # assert r.json()['msg'] == fail_data['expect']['msg']
    # assert r.json()['status'] == fail_data['expect']['status']
    Asserts.check(r.json(), fail_data['expect'], 'code,msg,status')


# 把注册成功的数据写到register_pass.yaml
# 注册成功的脚本，下发请求，断言响应的结果
@pytest.fixture(params=DataRead.read_yaml(r'data_case/register_pass.yaml'))
def pass_data(request):
    return request.param


def test_register_pass(url, baserequests, pass_data, db):
    mobilephone = pass_data['data']['mobilephone']
    # mobilephone = str(repeat_data['data']['mobilephone']) # 若原数据电话号码为整型,需要强转(因为断言是in text  其他的不需要)

    # 初始化环境：删除注册用户（数据库中可能有其他人测试注册的数据，与本用例冲突）
    Db.delete_user(db, mobilephone)
    # 下发注册的请求
    r = Member.register(url, baserequests, pass_data['data'])
    # 断言响应的结果
    print(r.text)
    # assert r.json()['code'] == pass_data['expect']['code']
    # assert r.json()['msg'] == pass_data['expect']['msg']
    # assert r.json()['status'] == pass_data['expect']['status']
    Asserts.check(r.json(), pass_data['expect'], 'code,msg,status')

    # 调用查询接口，在查询的结果中能够找到本次注册的手机号
    m = Member.query(url, baserequests)
    # print("打印出来的信息为", m.text)
    # print(type(m.text))    # 字符串类型
    # n = eval(m.text)
    # print(type(n))         # 字典类型
    assert mobilephone in m.text
    # 清理环境：删除注册用户（在数据库中添加的数据，测试完成后清理掉）
    Db.delete_user(db, mobilephone)


# 重复注册的写完
# 注册失败、注册成功的测试数据补充完
@pytest.fixture(params=DataRead.read_yaml(r'data_case/register_repeat.yaml'))
def repeat_data(request):
    return request.param


def test_register_repeat(url, baserequests, repeat_data, db):
    mobilephone = repeat_data['data']['mobilephone']

    # 初始化环境：删除注册用户（数据库中可能有其他人测试注册的数据，与本用例冲突）
    Db.delete_user(db, mobilephone)
    # 下发注册的请求
    Member.register(url, baserequests, repeat_data['data'])
    # 重复注册
    r = Member.register(url, baserequests, repeat_data['data'])
    # 断言响应的结果
    print(r.text)
    # assert r.json()['code'] == repeat_data['expect']['code']
    # assert r.json()['msg'] == repeat_data['expect']['msg']
    # assert r.json()['status'] == repeat_data['expect']['status']
    Asserts.check(r.json(), repeat_data['expect'], 'code,msg,status')

    # 清理环境：删除注册用户（在数据库中添加的数据，测试完成后清理掉）
    Db.delete_user(db, mobilephone)
