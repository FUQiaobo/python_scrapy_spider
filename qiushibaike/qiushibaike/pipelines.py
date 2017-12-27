# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import time
import os.path

class QiushiPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d',time.localtime())
        Filename = today+'.txt'
        with open(Filename,'a') as f:
            #f.write(item['id']+'\t')
            f.write(item['text']+'\t\n')
            #f.write(item['good']+'\n')
            time.sleep(2)
        return item
