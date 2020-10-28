"""
    2020.9.27
    show_strong
"""
import json

path_init = '/home/pxq/libdrv_so.so'


class Cso(object):
    """
        c 类 函数库的封装调用SO库
    """

    def __str__(self):
        introduce_str = "这是一个调用C类函数的封装so库的操作方法"
        return introduce_str

    def __init__(self, path=path_init):
        # 连接so库的方法
        self.path = path
        # return so

    @staticmethod
    def CSoCursor(path):
        """
        :param path:
        :return: 静态方法
        #>>> so = Cso.CSoCursor(path)
        #>>> print(so.get_board_count('void'))
        """
        import ctypes  # 这是调用C类函数的python内置方法
        so = ctypes.cdll.LoadLibrary(path)
        return so

    def FCSoCursor(self):
        """
        :return:
        c = Cso(path)
        print(c.FCSoCursor().get_board_count('void'))
        """
        import ctypes  # 这是调用C类函数的python内置方法
        so = ctypes.cdll.LoadLibrary(self.path)
        return so


response_code = [
    {"code": 1, "msg": "请求资源成功"},
    {"code": 0, "msg": "请求资源失败"},
    {"code": 2, "msg": "后台资源请求失败"},
    {"code": 101, "msg": "请求方式错误"},
    {"code": 201, "msg": "请求后台服务繁忙"},
    {"code": 404, "msg": "验证码查询失败，请求错误"},
    {"code": 110, "msg": "打开板卡成功"},
]


class InquireCode(object):
    def __str__(self):
        response_str = "这是查询code码及其返回对应数据资源的response生成对象集合"
        return response_str

    def __init__(self):
        self.retu_json = {"code": 404, "msg": "验证码查询失败，请求错误"}

    def inquire_code(self, code, data=None):
        for rc in response_code:
            if rc['code'] == code:
                self.retu_json = rc
        self.retu_json["data"] = data
        return self.retu_json

    @staticmethod
    def Sinquire_code(code, data=None):
        retu_json = {"code": 404, "msg": "验证码查询失败，请求错误"}
        for rc in response_code:
            if rc['code'] == code:
                retu_json = rc
        retu_json["data"] = data
        return retu_json

    def inquire_code_list(self, code, data=None):
        for rc in response_code:
            if rc['code'] == code:
                self.retu_json = rc
        self.retu_json["data"] = data
        return self.retu_json


if __name__ == '__main__':
    path = '/home/pxq/libdrv_so.so'
    so = Cso.CSoCursor(path)
    print(so.get_board_count('void'))
    c = Cso(path)
    print(c.FCSoCursor().get_board_count('void'))
