# -*- coding: utf-8 -*-
import scrapy
from items import QunarItem
import time
import os
# 设置相应的代理用户名密码，主机和端口号
# os.environ["http_proxy"] = "http://user:password@proxy.internal.server.com:8080"
os.environ["http_proxy"] = "http://127.0.0.1:8087"
class Q1Spider(scrapy.Spider):
    name = 'q1'
    address='桂林'
    # allowed_domains = ['qunar.com']
    start_urls = ['http://piao.qunar.com/ticket/list.htm?keyword=%s&region=&from=mpl_search_suggest'%address]
    n=1
    def parse(self, response):
       for div in response.xpath('//*[@id="search-list"]/div'):
           items=QunarItem()
           items['name']=div.xpath('./div/div[2]/h3/a/text()')[0].extract()
           items['addr']=div.xpath('./div/div[2]/div/p/span/@title')[0].extract()
           items['geo']=div.xpath('./@data-point')[0].extract()
           try:
               items['sales']=div.xpath('.//*[@class="hot_num"]/text()')[0].extract()
           except:
               items['sales'] =0
           yield items
       next_url=response.xpath('//*[@class="next"]/@href').extract()
       self.n+=1
       if self.n%1000==0:
            time.sleep(30)
       if self.n%5000==0:
            time.sleep(60)
       if next_url:
            yield response.follow(next_url[0],callback=self.parse)