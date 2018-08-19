# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
import json


class LjPipeline(object):
    def open_spider(self, spider):
        self.client = MongoClient()
        self.collection = self.client['LJ']['LJ']

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        item = json.dumps(item, ensure_ascii=False)
        item = item.replace('\n', '')
        item = item.replace('\\', '')
        item = json.loads(item)
        self.collection.insert(item)
        return item
