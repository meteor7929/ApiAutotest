'''
post请求
'''
import requests

# 发送post请求，表单类型的参数，使用data传参
# 登录接口
url = 'http://jy001:8081/futureloan/mvc/api/member/login'
cs = {"mobilephone": "18012345678", "pwd": "123456"}
r = requests.post(url, data=cs)
print(r.text)
assert r.json()['msg'] == '登录成功'

# 发送post请求，json类型的参数，使用json传参
url = 'http://www.httpbin.org/post'
cs = {"username": "123456789", "pwd": "123456789", "email": '3245@qq.com'}
r = requests.post(url, json=cs)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(r.text)
assert r.json()['json']['username'] == '123456789'

head = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}
r = requests.post(url, json=cs, headers=head)
print(r.text)
