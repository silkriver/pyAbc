# Project: sciencenet
from pyspider.libs.base_handler import *
from datetime import datetime
import re


class Handler(BaseHandler):
    crawl_config = {
    }
    po = re.compile(r"\d+/\d/\d+ \d+:\d+:\d+")

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl(
            'http://news.sciencenet.cn/todaynews.aspx',
            callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        rule = '#DataGrid1>tr>td>font>table>tr>td>a[href]'
        for each in response.doc(rule).items():
            self.crawl(each.attr.href, callback=self.detail_page)

    @config(priority=2)
    def detail_page(self, response):
        desc = response.doc('#content1').text().split('\n',  maxsplit=1)[1]
        desc = desc.replace('\n', '')[:50] + '...'
        date = response.doc('#content>tr>td[align="left"]>div').text()
        date = Handler.po.search(date).group()
        date = datetime.strptime(date, "%Y/%m/%d %H:%M:%S")
        return {
            "url": response.url,
            "title": response.doc('title').text(),
            "theme": "科学",
            "desc": desc,
            "date": str(date)
        }
