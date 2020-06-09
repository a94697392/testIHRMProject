# 需求
# 导包
import requests
# 发送IHRM登陆的接口请求
response = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                         json={"mobile": "13800000002", "password": "123456"},
                         headers={"Content-Type": "application/json"})
# 查看登陆的结果
print("登陆的结果是:",response.json())