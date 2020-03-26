# -*- coding: utf-8 -*-
import scrapy
from crawler.items import CrawlerItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['www.douban.com']
    start_urls = ['https://www.douban.com/group/HZhome/']

    def parse(self, response):
        # title = (response.xpath('//table[contains(@class,"olt")]//tr//a/text()').extract())
        title = (response.xpath('//table[contains(@class,"olt")]//tr/td[contains(@class,"title")]//a/text()').extract())
        nickname = (response.xpath('//table[contains(@class,"olt")]//tr/td[contains(@nowrap,"nowrap")]//a/text()').extract())
        print(title)
        print(nickname)
        # 返回一个request对象和一个item对象，request对象放的是标题的url，后面scrapy会继续读取这个url然后交给parse继续解析
        # return [scrapy.Request(content_url, self.post_content_parse, dont_filter=True),{"title":title}]
