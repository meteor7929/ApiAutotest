'''
上传文件：
    本地文件上传到服务器，比如上传头像，附件等
'''
import requests

# 上传文件的接口
url = 'http://www.httpbin.org/post'
# 要上传的文件（本地磁盘上的文件）
filePath = 'd:/monkey.log'
filePath2 = 'd:/w3.png'
# 'name':file-tuple
# ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``
# 3-tuple ``('filename', fileobj, 'content_type')``
# a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``

# with open(filePath, 'rb') as f:
#     file = {
#         'file1': (filePath, f)  # 二元组
#     }
#     r = requests.post(url, files=file)
#     print(r.text)

with open(filePath, 'rb') as f:
    with open(filePath2, 'rb') as f2:
        file = {
            'file1': (filePath, f),  # 二元组
            # content-type  MIME 类型，大类型/子类型  text/plain  image/jpg  application/json....
            'file2': (filePath2, f2, "image/png")  # 三元组    # image/png  图片类型
        }
        r = requests.post(url, files=file)
        print(r.text)
