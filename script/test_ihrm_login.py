# 1.导包
import unittest
import logging

from parameterized import parameterized

import app
from api.login_api import LoginApi
# 创建类
from utils import assert_common, read_login_data


class TestIHRMLoginParams(unittest.TestCase):
    # 进行实例化
    def setUp(self):
        self.login_api=LoginApi()
    def tearDown(self):
        pass

    def test01_login(self):
        response =self.login_api.login({
                                  "mobile": "13800000002",
                                  "password": "123456"
                                },
                             {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("登录的结果：{}".format(response.json()))
        # 断言

        assert_common(self, 200,True,10000, "操作成功", response)
    # 手机号码为空
    def test02_mobile_is_error(self):
        response = self.login_api.login({"mobile": "", "password": "error"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("手机号码为空：{}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)
    # 手机号码不存在
    def test03_mobile_is_empty(self):
        response = self.login_api.login({"mobile": "13800001111", "password": "123456"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("手机号码不存在的结果：{}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)
    # 密码为空
    def test04_password_is_empty(self):
        response = self.login_api.login({"mobile": "13800000002", "password": ""},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("密码为空的结果：{}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 密码错误
    def test05_password_is_error(self):
        response = self.login_api.login({"mobile": "13800000002", "password": "1234567"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info(" 密码错误的结果：{}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)
    # 无参
    def test06_params_is_none(self):
        response = self.login_api.login({},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("无参的结果：{}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)
    # 传入NULL
    def test07_params_is_null(self):
        response = self.login_api.login(None,
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("传入NULL的结果：{}".format(response.json()))
        # 断言
        assert_common(self, 200, False, 99999, "抱歉，系统繁忙，请稍后重试！", response)

    # 多参
    def test08_more_params(self):
        # 使用封装的接口调用登录接口，并接收返回的响应数据
        response = self.login_api.login({"mobile": "13800000002", "password": "123456", "more_params": "1"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("多参的结果为：{}".format(response.json()))
        assert_common(self, 200, True, 10000, "操作成功", response)

    # 少参-缺少mobile
    def test09_less_params_mobile(self):
        # 使用封装的接口调用登录接口，并接收返回的响应数据
        response = self.login_api.login({"password": "123456", "more_params": "1"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("少参-缺少mobile的结果为：{}".format(response.json()))
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 少参-缺少Passowrd
    def test10_less_password(self):
        # 使用封装的接口调用登录接口，并接收返回的响应数据
        response = self.login_api.login({"mobile": "13800000002", "more_params": "1"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("少参-缺少Passowrd的结果为：{}".format(response.json()))
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)

    # 错误参数
    def test11_params_is_error(self):
        # 使用封装的接口调用登录接口，并接收返回的响应数据
        response = self.login_api.login({"mboile": "13800000002", "password": "123456", "more_params": "1"},
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("错误参数的结果为：{}".format(response.json()))
        assert_common(self, 200, False, 20001, "用户名或密码错误", response)



