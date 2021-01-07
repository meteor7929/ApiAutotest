'''
断言
'''

import pytest_check as ck




def check(r_json, expect, keys):
    '''
    校验r_json与expect中，相应的key对应的value是否相同
    :param r_json: 实际的响应结果：r.json()
    :param expect: 预期结果
    :param keys: 校验的key列表，用逗号隔开：code,status,msg
    :return:
    # check(r.json(), login_data['expect'], 'code,msg,status')
    '''
    ks = keys.split(',')
    for k in ks:
        real = r_json[k]  # 根据key取r_json中的value
        exp = expect[k]  # 根据key取expect中的value
        try:
            # assert str(real) == str(exp)
            ck.equal(str(real), str(exp))
        except Exception as e:
            print(f'响应信息：{r_json},预期结果：{expect},校验{k}失败')
