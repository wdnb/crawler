# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['https://www.douban.com/']
    start_urls = ['https://www.douban.com/group/HZhome/']

    def parse(self, response):
          filename = response.url.split("/")[-2] # 获取url，用”/”分段，获去倒数第二个字段
          with open(filename, 'a') as f:
                f.write(response.body) # 把访问的得到的网页源码写入文件
        # filename
        # pass
