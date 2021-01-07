'''
测试前置和后置：fixture的方式（用的比较多的方式）
1.命名比较灵活，不用setup、teardown这种固定命名
2.使用方便，跨文件使用，不用import

使用方法：
    方法一：在需要使用前置的地方，作为参数使用
    方法二：在需要使用前置的地方，使用usefixtures注解
'''
import pytest


# 在普通的函数上增加fixture的注解，表示是测试前置
@pytest.fixture()
def login():
    print("登录系统")
    yield  # yield 关键字，表示 yield 之前的代码是前置，之后的内容是后置
    print("退出登录")  # 即每个测试用例之前执行前置内容，测试用例后执行后置内容（前提是函数中加入参数）

# autouse=True时，测试用例自动使用
@pytest.fixture(autouse=True)   # 每个测试用例之前都会执行（在fixture测试前置之前执行）
def data():
    print("准备测试数据")

def test_query():
    print("测试查询功能，不需要用户登录")


def test_add(login):  # 在需要使用前置的地方，作为参数使用
    print("测试添加的功能，需要登录")


def test_delete(login):
    print("测试删除的功能，需要登录")


# 在需要使用前置的地方，方法二：使用usefixtures注解
@pytest.mark.usefixtures('login')
def test_modify():
    print("测试修改的功能，需要登录")
