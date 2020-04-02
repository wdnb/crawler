# -*- coding: utf-8 -*-
import scrapy
from crawler.items import CrawlerItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['www.douban.com']
    start_urls = ['https://www.douban.com/group/HZhome/']

    def parse(self, response):
        title_list = (response.xpath('//table[contains(@class,"olt")]//tr/td[contains(@class,"title")]//a/text()').extract())
        nickname = (response.xpath('//table[contains(@class,"olt")]//tr/td[contains(@nowrap,"nowrap")]//a/text()').extract())
        url_list = (response.xpath('//table[contains(@class,"olt")]//tr/td[contains(@class,"title")]//a/@href').extract())
        ci = CrawlerItem()
        for title,nickname,url in zip(title_list,nickname,url_list):
            ci['title'] = title.replace("\n", "").replace(" ","")
            ci['nickname'] = nickname
            ci['url'] = url
        yield scrapy.Request(url, callback=self.post_content_parse, meta={'item': ci, 'url': url})

    def post_content_parse(self, response):
        ci = response.meta['item']
        content_text_1 = (response.xpath('//div[contains(@class,"topic-richtext")]/p/text()').extract())
        content_img_1 = (response.xpath('//div[contains(@class,"image-wrapper")]/img/@src').extract())
        #title从这里获取吧 外部title不完整
        for content_text_1,content_img_1 in zip(content_text_1,content_img_1):
            ci['content_text_1'] = content_text_1
            ci['content_img_1'] = content_img_1


        print(ci)    
