# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class JianshutestPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient('localhost',27017)
        test = client['test']
        jianshutest = test['jianshutest']
        self.post = jianshutest

    def process_item(self, item, spider):
        info = dict(item)
        self.post.insert(info)
        return item
