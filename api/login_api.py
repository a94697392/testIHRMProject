# 1.导包
import requests
# 创建封装接口类
class LoginApi:
    def __init__(self):
        self.login_url="http://ihrm-test.itheima.net"+"/api/sys/login"
    def login(self,jsonData,headers):
        """
        :rtype:Response
        :param jsonData:
        :param headers:
        :return:
        """
        # 发送登陆的请求,并返回reponse对象
        return requests.post(url=self.login_url,json=jsonData,headers=headers)