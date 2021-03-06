# -*- coding: utf-8 -*-

import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    """docstring for SpiderMain"""

    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        count = 1

        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                print "craw %d : %s" % (count, new_url)
                if count == 10:
                    break
                count = count + 1
            except Exception, e:
                print e, "craw failed"

        self.outputer.output_html()

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
