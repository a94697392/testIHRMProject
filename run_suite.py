# 生成测试报告时，要先执行测试用例
# 我们可以把测试用例添加到测试套件中，然后执行测试套件生成测试报告
# 1.导包
import os
import time
import  unittest
# 2.创建测试套件
import HTMLTestRunner_PY3

from script.test_ihrm_employee_params import TestIHRMEmployee
from script.test_login_params import TestIHRMLogin

BASE_DIR =os.path.dirname(os.path.abspath(__file__))

suite =unittest.TestSuite()
# 3.将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestIHRMEmployee))
suite.addTest(unittest.makeSuite(TestIHRMLogin))
# 4.定义报告的目录和报告的名称
# report_path = BASE_DIR + "/report/ihrm{}.html".format(time.strftime("%Y%m%d%H%M%S"))
report_path = BASE_DIR + "/report/ihrm.html"
# 5.使用HTMLTestRunner_PY3生成测试报告
with open(report_path,"wb")as f:
    runner =HTMLTestRunner_PY3.HTMLTestRunner(f,verbosity=1,title="ihrm登陆接口功能测试",description="这是一个更加美观的报告")
    # 使用实例化的runner运行测试套件，生成测试报告
    runner.run(suite)
print("测试会不会触发轮形")