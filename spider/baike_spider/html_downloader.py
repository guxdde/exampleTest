# -*- coding: utf-8 -*-

import urllib2


class HtmlDownloader(object):
    """docstring for HtmlDownloader"""

    def __init__(self):
        pass

    # 下载网页内容
    def download(self, new_url):
        if new_url is None:
            return
        response = urllib2.urlopen(new_url)
        if response.getcode() != 200:
            return None
        return response.read()
