# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #标题
    title = scrapy.Field()
    #发布用户昵称
    nickname = scrapy.Field()
    #帖子链接
    url = scrapy.Field()
    #帖子文本一楼
    content_text_1 = scrapy.Field()
    #帖子图片一楼
    content_img_1 = scrapy.Field()
