# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import os.path

class BookPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d',time.localtime())
        Filename = today+'.json'
        with open (Filename,'a',encoding='utf-8') as f:
            f.write('书名：'+item['title']+'\t\n\n')
            # f.write(item['jianjie']+ '\t\n')
            # f.write('内容简介：'+item['neirong']+'\t\n')
            # f.write('作者简介：'+item['zuozhe']+'\t\n')
            # f.write('评分：'+item['pingfen']+'\t\n')
            # f.write('评价人数：'+item['pingjia'] + '\n\n\n')
            time.sleep(2)
        return item
