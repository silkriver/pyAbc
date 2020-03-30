# Project: solidot
from pyspider.libs.base_handler import *
from datetime import datetime
import re


class Handler(BaseHandler):
    crawl_config = {
    }
    po = re.compile(r"\d+年\d+月\d+日 \d+时\d+分")

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('https://www.solidot.org/', callback=self.index_page)

    @config(age=5)
    def index_page(self, response):
        for each in response.doc('div[class="block_m"]').items():
            date = each('div[class="talk_time"]').text()
            date = Handler.po.search(date).group()
            date = datetime.strptime(date, "%Y年%m月%d日 %H时%M分")
            item = {
                "url": each('div[class="bg_htit"]>h2>a[href]').attr.href,
                "title": each('div[class="bg_htit"]>h2>a[href]').text(),
                "theme": "科技",
                "desc": each('.p_mainnew').text()[:50] + "...",
                "date": str(date)
            }
            self.send_message(self.project_name, item, url=item["url"])

    def on_message(self, project, msg):
        return msg
