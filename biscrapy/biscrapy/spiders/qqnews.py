# -*- coding: utf-8 -*-
import scrapy
import json
import datetime
from scrapy.loader import ItemLoader
from biscrapy.items import NewsItem


class QqnewsSpider(scrapy.Spider):
    name = 'qqnews'
    allowed_domains = ['qq.com']
    start_urls = ['http://news.qq.com/']

    base_url = "http://openapi.inews.qq.com/getQQNewsNormalContent?id={id}&refer=mobilewwwqqcom"

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.index_parse)

    def index_parse(self, response):
        finance_url = response.xpath("//ul[@id='siteNavPart1']/li[3]/a/@href").extract_first()
        sports_url = response.xpath("//ul[@id='siteNavPart1']/li[4]/a/@href").extract_first()
        ent_url = response.xpath("//ul[@id='siteNavPart1']/li[5]/a/@href").extract_first()
        tech_url = response.xpath("//ul[@id='siteNavPart1']/li[6]/a/@href").extract_first()
        auto_url = response.xpath("//ul[@id='siteNavPart2']/li[2]/a/@href").extract_first()
        fashion_url = response.xpath("//ul[@id='siteNavPart2']/li[4]/a/@href").extract_first()
        cul_url = response.xpath("//ul[@id='siteNavPart2']/li[5]/a/@href").extract_first()
        yield scrapy.Request(finance_url, callback=self.finance_page_parse, meta={"channel": "财经"})
        yield scrapy.Request(sports_url, callback=self.sports_page_parse, meta={"channel": "运动"})
        yield scrapy.Request(ent_url, callback=self.ent_page_parse, meta={"channel": "娱乐"})
        yield scrapy.Request(tech_url, callback=self.tech_page_parse, meta={"channel": "科技"})
        yield scrapy.Request(auto_url, callback=self.auto_page_parse, meta={"channel": "汽车"})
        yield scrapy.Request(fashion_url, callback=self.fashion_page_parse, meta={"channel": "时尚"})
        yield scrapy.Request(cul_url, callback=self.cul_page_parse, meta={"channel": "文化"})

    def finance_page_parse(self, response):
        '''财经'''
        articles = response.xpath("//div[@class='Q-tpList']/div")
        channel = response.meta.get('channel')
        for article in articles:
            article_url = article.xpath("./a/@href").extract_first()
            tag = article_url.split('/')[-1].split('.')[0]
            if len(tag) > 6:
                a_id = tag + '00'
            else:
                a_id = "".join(article_url.split('/')[-2:]).split('.')[0] + '00'
            yield scrapy.Request(self.base_url.format(id=a_id), callback=self.news_detail_parse,
                                 meta={"channel": channel})

    def sports_page_parse(self, response):
        '''运动'''
        channel = response.meta.get('channel')
        links = response.xpath("//div[contains(@class,main-item)]/div[@class='fl']/ul/li/span/a/@href").extract()
        for link in links:
            tag = link.split('/')[-1].split('.')[0]
            if len(tag) > 6:
                a_id = tag + '00'
            else:
                a_id = "".join(link.split('/')[-2:]).split('.')[0] + '00'
            yield scrapy.Request(self.base_url.format(id=a_id), callback=self.news_detail_parse,
                                 meta={"channel": channel})

    def ent_page_parse(self, response):
        '''娱乐'''
        articles = response.xpath("//div[@class='Q-tpList']/div")
        channel = response.meta.get('channel')
        for article in articles:
            article_url = article.xpath("./a/@href").extract_first()
            a_id = article_url.split('/')[-1].split('.')[0] + '00'
            yield scrapy.Request(self.base_url.format(id=a_id), callback=self.news_detail_parse,
                                 meta={"channel": channel})

    def tech_page_parse(self, response):
        '''科技'''
        channel = response.meta.get('channel')
        links = response.xpath("//div[@class='Q-tpList']/div[@class='Q-tpListInner']/a/@href").extract()
        for link in links:
            tag = link.split('/')[-1].split('.')[0]
            if len(tag) > 6:
                a_id = tag + '00'
            else:
                a_id = "".join(link.split('/')[-2:]).split('.')[0] + '00'
            yield scrapy.Request(self.base_url.format(id=a_id), callback=self.news_detail_parse,
                                 meta={"channel": channel})

    def auto_page_parse(self, response):
        '''汽车'''
        channel = response.meta.get('channel')
        links = response.xpath("//div[@class='list']")[0:6].xpath("./ul/li/a/@href").extract()
        for link in links:
            tag = link.split('/')[-1].split('.')[0]
            if len(tag) > 6:
                a_id = tag + '00'
            else:
                a_id = "".join(link.split('/')[-2:]).split('.')[0] + '00'
            yield scrapy.Request(self.base_url.format(id=a_id), callback=self.news_detail_parse,
                                 meta={"channel": channel})

    def fashion_page_parse(self, response):
        '''时尚'''
        channel = response.meta.get('channel')
        links = response.xpath("//div[@class='Q-tpList']/div[@class='Q-tpWrap']/a/@href").extract()
        for link in links:
            a_id = link.split('/')[-1]
            yield scrapy.Request(self.base_url.format(id=a_id), callback=self.news_detail_parse,
                                 meta={"channel": channel})

    def cul_page_parse(self, response):
        '''文化'''
        channel = response.meta.get('channel')
        links = response.xpath("//div[@class='Q-pList']/div[@class='content']/em/a/@href").extract()
        links2 = response.xpath("//div[@class='Q-tpList']/div[@class='Q-tpWrap']/a/@href").extract()
        links.extend(links2)
        for link in links:
            tag = link.split('/')[-1].split('.')[0]
            if len(tag) > 6:
                a_id = tag + '00'
            else:
                a_id = "".join(link.split('/')[-2:]).split('.')[0] + '00'
            yield scrapy.Request(self.base_url.format(id=a_id), callback=self.news_detail_parse,
                                 meta={"channel": channel})

    def news_detail_parse(self, response):
        result = json.loads(response.text, encoding='utf-8')
        if result and result['ret'] == 0:
            title = result['title']
            a_id = result['id']
            cover_img = result['img']['imgurl']
            content = result['content']
            url = result['url']
            pubtime = result['pubtime']
            news_item = NewsItem()
            news_item['a_id'] = a_id
            news_item['title'] = title
            news_item['cover_img'] = cover_img
            news_item['content'] = content
            news_item['url'] = url
            news_item['pubtime'] = datetime.datetime.strptime(pubtime, '%Y-%m-%d %H:%M:%S')
            news_item['crawl_time'] = datetime.datetime.now()
            news_item['update_time'] = datetime.datetime.now()
            news_item['channel'] = response.meta.get('channel')
            yield news_item
