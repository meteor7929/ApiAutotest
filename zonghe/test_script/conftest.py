'''
脚本层的一些公共方法
'''
#################################################


'''
python导入包的规则：
1.安装目录找包
2.如果使用IDE，会从工程的根路径开始，向下搜索
3.命令行执行时，以当前执行的py文件开始，向下搜索。
解决办法：把工程路径，放到sys.path中
'''
import sys,os
print(sys.path)
cp = os.path.realpath(__file__)
# print('cp:',cp)
# mm = os.getcwd()
# print('cwd:',mm)
cd = os.path.dirname(cp)
cm = os.path.dirname(cd)
co = os.path.dirname(cm)
print(co)
# sys.path.append(co)
print(sys.path)
#############################################
import pytest

from zonghe.caw import DataRead
from zonghe.caw.BaseRequests import BaseRequests

env_path = r'data_env/env.ini'


# 读取env.ini中的url，设置session级别的，整个执行过程读一次
@pytest.fixture(scope='session')
def url():
    return DataRead.read_ini(env_path, 'url')


@pytest.fixture(scope="session")
def db():
    return eval(DataRead.read_ini(env_path, 'db'))


# 创建一个BaseRequests的实例，设置session级别的，整个执行过程只有一个实例，自动管理cookie
@pytest.fixture(scope="session")
def baserequests():
    return BaseRequests()
