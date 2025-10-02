import requests,os
MY_API_KEY=os.environ.get("MY_API_KEY")
#MY_API_KEY="SCT171556TUitezllQAZBQWUhyDWRIY9RK"
def send_to_wechat(message):
    url = f"https://sctapi.ftqq.com/{MY_API_KEY}.send"
    data = {
        "title": "Github_微信运动步数："+str(message),  # 消息标题
        "desp": message          # 消息内容（支持 Markdown）
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("消息推送成功！")
    else:
        print("消息推送失败！")

# 示例：推送程序运行结果
#result = "程序运行成功！数据：12345"
##send_to_wechat(result)
