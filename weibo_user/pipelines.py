# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from pymysql.cursors import DictCursor


class WeiboUserPipeline(object):
    def __init__(self):
        self.PORT = 3306
        self.HOST = '192.168.100.110'
        self.USER = 'mysql'
        self.PASSWD = 'P@ssw0rd'
        self.conn = pymysql.connect(port=self.PORT, host=self.HOST, user=self.USER, passwd=self.PASSWD,db='weibo', charset='utf8')
        self.cursor = self.conn.cursor(DictCursor)

    def process_item(self, item, spider):

        sql = "insert into wb_blogs (likes, comments, idstr, islong, raw_text,reposts_count, " \
                     "retweeted, retweeted_id, edited, created_at) values (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)"
        print(self.cursor.mogrify(sql,args=(item['likes'], item['comments'], item['idstr'], item['islong'], item['raw_text'].strip(),
                                            item['reposts_count'], item['retweeted'], item['retweeted_id'],item['edited'],
                                            str(item['created_at']))))
        ret = self.cursor.execute(
            query=sql,
            args=(item['likes'], item['comments'], item['idstr'], item['islong'], item['raw_text'].strip(),
                                            item['reposts_count'], item['retweeted'], item['retweeted_id'],item['edited'],
                                            str(item['created_at'])))
        if ret == 1:
            self.conn.commit()


        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()