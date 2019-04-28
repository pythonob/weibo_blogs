# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis import spiders
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders.crawl import Rule
from ..items import WeiboUserItem
import json, re


class WbuserSpider(spiders.RedisCrawlSpider):
    name = 'wbuser'
    allowed_domains = ['weibo.cn']
    redis_key = 'weibo_user:start_url'

    def start_requests(self):
        base_url = 'https://m.weibo.cn/api/container/getIndex?containerid=1076031885454921_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page='
        for i in range(13000):
            url = base_url + str(i)
            yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):

        resp = json.loads(response.text)
        if resp.get('data'):
            data1 = resp['data']
            if data1.get('cards'):
                data2 = data1['cards']
                for data3 in data2:
                    item = WeiboUserItem()
                    blog = data3['mblog']
                    item['likes'] = blog['attitudes_count']
                    item['comments'] = blog['comments_count']
                    item["created_at"] = blog['created_at']
                    item["idstr"] = blog['idstr']
                    #item['raw_text'] = blog['raw_text']
                    text = blog['text']
                    item['raw_text'] = re.sub(r'<[^>]+>','', text)
                    if blog.get('retweeted_status'):
                        item['retweeted'] = 1
                        item['retweeted_id'] = blog['retweeted_status']['idstr']
                    else:
                        item['retweeted'] = 0
                        item['retweeted_id'] = ''
                    item['reposts_count'] = blog['reposts_count']
                    if blog['isLongText'] == 'True':
                        item['islong'] = 1
                    else:
                        item['islong'] = 0

                    if blog.get('edit_config'):
                        if blog['edit_config'].get('edited'):
                            item['edited'] = 1
                        else:
                            item['edited'] = 0

                    else:
                        item['edited'] = 0
                    yield item




