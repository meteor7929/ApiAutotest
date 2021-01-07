'''
使用 request 做接口测试
'''

# 导入包
import requests

# 发送一个请求
# response = requests.get("http://www.baidu.com")
# print(response.text)  # 文本格式的返回值
# print(response.status_code)  # 响应状态码
# print(response.raw)  # 无格式的相应

# 接口测试：构造不同的参数，发送请求，对响应的结果做断言
# 获取用户列表
# http://jy001:8081 测试环境
# http://192.168.150.222:8081
# futureLoan/mvc/api/member/list  接口地址

url = "http://jy001:8081/futureloan/mvc/api/member/list"
r = requests.get(url)
print(r.text)
assert r.status_code == 200  # 响应码
# 响应体是json格式，去里面的code，检查是不是10001
assert r.json()['code'] == '10001'

# 发送的请求带参数
# 方式一：拼接到url后面
# 注册用户
url = "http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=18112345678&pwd=123456"
r = requests.get(url)
print(r.text)
assert r.status_code == 200  # 响应码
# 响应体是json格式，去里面的code，检查是不是10001
assert r.json()['code'] == '20110'
assert r.json()['msg'] == '手机号码已被注册'
assert r.json()['status'] == 0

# 方式二：使用params传参
url = "http://jy001:8081/futureloan/mvc/api/member/register"
data = {"mobilephone":'181##2345678',"pwd":"12345","regname":"requests"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['msg'] == '密码长度必须为6~18'
# assert r.json()['msg'] == '手机号码格式不正确'

print("***********************************************")
# 练习：淘宝查询手机号码归属地的接口
url = 'https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=18571457257'
# 参数tel:手机号码
r = requests.get(url)
print(r.text)

url = 'https://tcc.taobao.com/cc/json/mobile_tel_segment.htm'
data = {'tel':13636161964}
r = requests.get(url,params=data)
print(r.text)
# assert "湖北移动" in r.text

# 发送请求，设置请求头
# 测试的网站，不管发送什么请求，服务器会将请求的内容封装成json格式返回
# /get  get方法    /post   post方法
head = {
    "User-Agent":'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}
url = 'http://www.httpbin.org/get'
r = requests.get(url,headers=head)
print(r.text)