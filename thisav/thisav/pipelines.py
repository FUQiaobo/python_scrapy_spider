# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import os.path
from scrapy.pipelines.images import ImagesPipeline
# class Test1Pipeline(ImagesPipeline):
#     def get_media_requests(self, item, info):
#         return [Request(x) for x in item.get(self.images_urls_field, [])]
#
#     def item_completed(self, results, item, info):
#         if isinstance(item, dict) or self.images_result_field in item.fields:
#             item[self.images_result_field] = [x for ok, x in results if ok]
#         return item

class ThisavPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d',time.localtime())
        Filename = today+'.json'
        with open(Filename,'a',encoding='utf-8') as f:
            f.write('标题：'+item['title']+'\t')
            f.write('时长：'+item['time']+'\t')
            f.write('链接：'+item['link']+'\t')
            f.write('封面图片：'+item['src'] + '\n\n')
            time.sleep(2)

        return item
