# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import os.path


class Movie1905Pipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%y',time.localtime())
        fileName = today+'.txt'
        with open(fileName,'a') as f:
            f.write(item['name']+'\t')
            f.write(item['miaoshu'] + '\t')
            f.write(item['Actor'] + '\t')
            f.write(item['time'] + '\t')
            f.write(item['descr'] + '\t')
            f.write(item['url'] + '\n\n')
            time.sleep(2)
        return item
