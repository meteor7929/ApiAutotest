'''
fixture作用域：类级别的

每个类，首次调用login的地方执行前置，类中用例执行完执行后置
'''
import pytest


@pytest.fixture(scope='class')
def login():
    print("前置：登录系统")
    yield
    print("后置：退出登录")

class TestQuery:
    def test_01(self):
        print("用例1")

    def test_02(self,login):      # 执行前置
        print("用例2")

    def test_03(self,login):
        print("用例3")

    def test_04(self,login):      # 执行后置
        print("用例4")

class TestAdd:
    def test_001(self):
        print("用例001")

    def test_002(self):
        print("用例002")

    def test_003(self, login):      # 执行前置
        print("用例003")

    def test_004(self, login):      # 执行后置
        print("用例004")