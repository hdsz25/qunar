# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import datetime
from spiders.q1 import Q1Spider
today=str(datetime.date.today()).replace('-','')

class QunarPipeline(object):
    def __init__(self):
        self.f=open(u'%s旅游景点售票信息%s.csv'%(Q1Spider.address,today),'w',newline="",encoding='utf-8')
        self.writer=csv.writer(self.f)
        self.writer.writerow([u'景点名字',u'经纬度',u'地址',u'已售票数'])
    def process_item(self, item, spider):
        self.writer.writerow((item['name'],item['geo'],item['addr'],item['sales']))
        return item
    def close_spider(self,spider):
        self.f.close()
