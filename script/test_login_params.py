# 1.导包
import unittest
import logging

from parameterized import parameterized

import app
from api.login_api import LoginApi
# 创建类
from utils import assert_common, read_login_data


class TestIHRMLogin(unittest.TestCase):
    # 进行实例化
    def setUp(self):
        self.login_api=LoginApi()
    def tearDown(self):
        pass

    filepath = app.BASE_DIR + "/data/login_data.json"

    # 编写登陆的函数
    @parameterized.expand(read_login_data(filepath))
    def test01_login(self, case_name, request_body, success, code, message, hettp_code):
        response = self.login_api.login(request_body,
                                        {"Content-Type": "application/json"})
        # 打印响应数据
        logging.info("登录的结果：{}".format(response.json()))
        # 断言

        assert_common(self, hettp_code, success, code, message, response)