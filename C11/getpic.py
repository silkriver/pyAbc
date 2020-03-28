"""随机图片API测试程序
从“岁月小筑”获取一张随机图片的网址并用浏览器打开
"""
from urllib.request import urlopen
import webbrowser
url = "http://img.xjh.me/random_img.php?return=url"


def main():
    try:
        # 请求图片API网址，得到图片网址
        pic = urlopen(url).read().decode()
        # 使用浏览器打开图片网址
        webbrowser.open("http:" + pic)
    except Exception as ex:
        print(repr(ex))


if __name__ == "__main__":
    main()
