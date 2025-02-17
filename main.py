import requests
from random import randint
import push ,os

# 定义请求的URL
url = "http://yanwan.store/run4/mi20241027.php"

# 定义请求头
headers = {
    "Host": "yanwan.store",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Content-Length": "52",
    "Origin": "http://bs.yanwan.store",
    "Connection": "keep-alive",
    "Referer": "http://bs.yanwan.store/"
}
##MY_API_KEY=os.environ.get("MY_API_KEY")
user=os.environ.get("MY_ACCOUNT")
password==os.environ.get("MY_PASSWORD")
#user="laoeluziyang@163.com"
#password="asd123456!"

# 定义请求体
step = str(14000+randint(0, 4000))
data = {
    "user": user,
    "password": password,
    "step": step
}

# 发送POST请求
response = requests.post(url, headers=headers, data=data)
print(data)
# 输出响应内容
print(response.status_code)
print(str(response.json()))
#push.send_to_wechat(str(response.json()))
