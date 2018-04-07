# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose, Join


class BiscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class NewsItem(scrapy.Item):
    a_id = scrapy.Field()
    title = scrapy.Field()
    cover_img = scrapy.Field()
    content = scrapy.Field()
    pubtime = scrapy.Field()
    url = scrapy.Field()
    crawl_time = scrapy.Field()
    update_time = scrapy.Field()
    channel = scrapy.Field()


# def add_title(value):
#     return value + 'def'

# class NewsItem(scrapy.Item):
#     a_id = scrapy.Field()
#     title = scrapy.Field(
#         # input_processor=MapCompose(add_title),
#         input_processor=MapCompose(lambda x: x + 'abc', add_title),
#     )
#     cover_img = scrapy.Field()
#     content = scrapy.Field()
#     pubtime = scrapy.Field()
#     url = scrapy.Field()
#     crawl_time = scrapy.Field()
#     update_time = scrapy.Field()
