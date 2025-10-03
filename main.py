import requests
from random import randint
import os
import datetime

MY_API_KEY="SCT171556TUitezllQAZBQWUhyDWRIY9RK"
def send_to_wechat(message):
   # print(message)
    url = f"https://sctapi.ftqq.com/{MY_API_KEY}.send"
    data = {
        "title": "Github_微信运动步数："+message,  # 消息标题
        "desp": message          # 消息内容（支持 Markdown）
    }
   # print(data)
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("消息推送成功！")
    else:
        print("消息推送失败！")
        
def generate_token():
    """
    生成基于当前时间的 token，计算方式：
    token = (年份 * (月份 + 日期)) + (日期 * 小时 * 分钟)
    """
    now = datetime.datetime.now()
    year = now.year
    month = now.month  # Python 的月份是 1-12，不需要 +1
    day = now.day
    hour = now.hour+8
    minute = now.minute

    token = (year * (month + day)) + (day * hour * minute)
    return str(token)

# 定义请求的URL
url = "https://bs.yanwan.store/run4/mi20241029.php"

# 定义请求头
headers = {
    "Host": "bs.yanwan.store",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Content-Length": "52",
    "Origin": "https://bs.yanwan.store",
    "Connection": "keep-alive",
    "Referer": "https://bs.yanwan.store/run4/"
}
##MY_API_KEY=os.environ.get("MY_API_KEY")
#user=os.environ.get("MY_ACCOUNT")
#password=os.environ.get("MY_PASSWORD")
user="laoeluziyang@163.com"
password="asd123456!"

# 定义请求体
step = str(16000+randint(0, 3000))
data = {
    "user": user,
    "password": password,
    "step": step,
    "token":generate_token()
}


# 发送POST请求
response = requests.post(url, headers=headers, data=data)
print(data)
# 输出响应内容
print(response.status_code)
print(str(response.json()))
msg=str(response.json())
send_to_wechat(msg)
