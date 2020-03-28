"""批量下载图片
说明：
创建类实例调用getlinks方法获取图片链接列表，调用savefile方法将链接保存为文件
示例：
>>> from webcrawler import Crawler
>>> c = Crawler()
>>> links = c.getlinks("高清动漫")
搜索词条 高清动漫
>>> len(links) > 0
True
"""
from urllib.request import build_opener, install_opener, urlopen, urlretrieve
from urllib.parse import quote, urlparse
import os
import re
bdimg = "https://image.baidu.com/search/flip?tn=baiduimage&word="


class Crawler:
    """百度图片爬虫"""

    def __init__(self):
        """初始化爬虫实例，设置图片保存目录"""
        pydir = os.path.dirname(os.path.abspath(__file__))
        self.imgdir = os.path.join(pydir, "img")
        if not os.path.exists(self.imgdir):
            os.mkdir(self.imgdir)
        self.cnt = 0

    def getlinks(self, word):
        """获取链接列表"""
        links = []
        print("搜索词条", word)
        try:
            # 向百度图片搜索提交指定关键字获取结果网页
            html = urlopen(bdimg + quote(word)).read().decode()
            # 使用正则表达式从搜索结果网页源码中提取原始图片链接
            links = re.findall(r'"objURL":"(.+?)"', html)
        except Exception as ex:
            print("发生错误", repr(ex))
        return links

    def savefile(self, url):
        """将链接保存为文件"""
        imgfile = os.path.join(self.imgdir, quote(url, ""))
        if not os.path.exists(imgfile):
            print("保存文件", url)
            try:
                res = urlparse(url)
                # 为HTTP请求构建特定的报头
                # 部分网站会检查客户端是否提供必要信息
                domain = res.hostname.split(".", 1)[1]
                opener = build_opener()
                opener.addheaders = [
                        ("User-Agent", "Mozilla/5.0"),
                        ("Referer", f"{res.scheme}://www.{domain}/")]
                install_opener(opener)
                urlretrieve(url, imgfile)   # 将链接目标保存为文件
                self.cnt += 1
            except Exception as ex:
                print("发生错误", repr(ex))


if __name__ == "__main__":
    c = Crawler()
    links = c.getlinks("国画")
    for i in links:
        c.savefile(i)
    print(f"运行结束，共下载{c.cnt}个文件")
