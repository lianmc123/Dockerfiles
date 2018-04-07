# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
import asyncio
from aiomysql.sa import create_engine
import json
from sqlalchemy.orm import sessionmaker


# from biscrapy.models import news, news_extend


class BiscrapyPipeline(object):
    def process_item(self, item, spider):
        a = item['a_id']
        return item


class MySQLTwisterPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings['DB_HOST'],
            port=settings['DB_PORT'],
            user=settings['DB_USERNAME'],
            passwd=settings['DB_PASSWORD'],
            db=settings['DATABASE'],
            charset=settings['DB_CHARSET'],
            # use_unicode=True
        )
        dbpool = adbapi.ConnectionPool("pymysql", **dbparms)
        return cls(dbpool)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.do_insert, item)
        # query.addErrback(self.handle_error, item, spider)
        return item

    def handle_error(self, failure, item, spider):
        print(failure)

    def do_insert(self, cursor, item):
        insert_sql = '''
            insert into news(a_id, title, cover_img, content, channel, pubtime, url, crawl_time, update_time)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(insert_sql, (
            item['a_id'], item['title'], item['cover_img'], json.dumps(item['content']), item['channel'],
            item['pubtime'],
            item['url'], item['crawl_time'], item['update_time']))


class SQLAlchemyPipeline(object):
    def __init__(self, dbparms):
        self.dbparms = dbparms

    @classmethod
    def from_crawler(cls, crawler):
        dbparms = dict(
            host=crawler.settings['DB_HOST'],
            port=crawler.settings['DB_PORT'],
            user=crawler.settings['DB_USERNAME'],
            password=crawler.settings['DB_PASSWORD'],
            db=crawler.settings['DATABASE'],
            charset=crawler.settings['DB_CHARSET'],
            use_unicode=True
        )
        return cls(dbparms=dbparms)

    # def open_spider(self, spider):
    #     import aiomysql
    #     aiomysql.connect()
    #     import pymysql
    #     pymysql.connect()

    @asyncio.coroutine
    def go(self, item):
        # engine = yield from create_engine(**self.dbparms)
        engine = yield from create_engine(user='root', db='website', host='127.0.0.1', password='124578',
                                          charset='utf8', use_unicode=True)
        # with (yield from engine) as conn:
        #     yield from conn.execute(news.insert().values(a_id=item['a_id'], title=item['title']))
        #     yield from conn.execute(news_extend.insert().values(cover_img=item['cover_img'], content=item['content'],
        #                                                         pubtime=item['pubtime'], url=item['url'],
        #                                                         channel=item['channel'], a_id=item['a_id']))

    def process_item(self, item, spider):
        asyncio.get_event_loop().run_until_complete(self.go(item))
        return item
