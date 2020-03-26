# -*- coding: utf-8 -*-
import scrapy
from crawler.items import CrawlerItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['www.douban.com']
    start_urls = ['https://www.douban.com/group/HZhome/']

    def parse(self, response):
        dl = response.css('.mod table')
        # filename = response.url.split("/")[-2]  # 获取url，用”/”分段，获去倒数第二个字段
        # with open(filename, 'ab') as f:
            # f.write(response.body)  # 把访问的得到的网页源码写入文件
        for dd in dl:
            item = CrawlerItem()
            item['title'] = dd.css('.title a::text').extract_first()
            # item['nowrap'] = dd.css('.nowrap a::text').extract_first()
            yield item

        #   filename = response.url.split("/")[-2] # 获取url，用”/”分段，获去倒数第二个字段
        #   with open(filename, 'ab') as f:
            #   f.write(response.body)  # 把访问的得到的网页源码写入文件
