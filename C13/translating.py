"""Python文档翻译项目进度通知
"""
import json
import os
import smtplib      # 用于发送电子邮件的SMTP协议库
import time
from datetime import datetime, timedelta
from email.mime.text import MIMEText    # 用于处理电子邮件信息的email包
from email.header import Header
from email.utils import formataddr
from urllib.request import urlopen, Request
mail_to = os.environ.get("mail_to")     # 从环境变量获取电子邮件服务信息
mail_from = os.environ.get("mail_from")
smtp_host = os.environ.get("smtp_host")
smtp_user = os.environ.get("smtp_user")
smtp_pass = os.environ.get("smtp_pass")
url = "http://gce.zhsj.me/python/newest"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) \
    Gecko/20100101 Firefox/61.0"}


def automail(title, content, encoding="utf-8"):
    """自动发送邮件"""
    msg = MIMEText(content, "plain", encoding)
    msg["To"] = mail_to
    msg["From"] = formataddr(["自动邮件", mail_from])
    msg["Subject"] = Header(title, encoding)
    try:
        smtp = smtplib.SMTP(smtp_host)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(smtp_user, smtp_pass)
        smtp.sendmail(mail_from, mail_to, msg.as_string())
    except Exception as ex:
        print(repr(ex))


def main(t):    # 发送通知邮件
    try:
        req = Request(url=url, headers=headers)
        data = urlopen(req).read().decode()
        data_dict = json.loads(data)
        message = "时间：" + t + "\n进度：" + data_dict.get("zh_CN")
        automail("Python文档翻译进度报告", message)
    except Exception as ex:
        automail("程序错误报告", repr(ex))


if __name__ == "__main__":  # 每天定时执行任务
    while True:
        main(datetime.now().strftime("%Y-%m-%d %H:%M"))
        dt = datetime.now() + timedelta(days=1)
        dt = dt.replace(hour=6, minute=0, second=0, microsecond=0)
        while datetime.now() < dt:
            time.sleep(1)
