# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import os.path

class DoubanPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d',time.localtime())
        Filename = today+'.json'
        with open (Filename,'a',encoding='utf-8') as f:
            f.write(item['title']+'\t')
            f.write(item['pingfen']+'\t')
            f.write(item['pingjia']+'\t')
            f.write(item['pingyu']+'\n\n')
            time.sleep(2)
        return item
