# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboUserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    likes = scrapy.Field()  # 点赞数
    comments = scrapy.Field()
    idstr = scrapy.Field()
    islong = scrapy.Field()
    raw_text = scrapy.Field()  # 文本
    reposts_count = scrapy.Field()  # 被转发次数
    retweeted = scrapy.Field()  # 是否转发
    retweeted_id = scrapy.Field()  # 原微博喜欢次数
    edited = scrapy.Field()
    created_at = scrapy.Field()

