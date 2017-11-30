# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class ZhiliPipeline(object):
    header = ['项目名称', '建设地点', '建设单位', '环境影响评价机构', '受理日期', 'url']
    with open('data.csv', 'a', newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(header)

    def process_item(self, item, spider):
        line = [item['name'], item['location'], item['campy'], item['evaluate'], item['time'], item['url']]
        with open('data.csv', 'a', newline='') as f:
            f_csv = csv.writer(f)
                #f_csv.writerow(headers)
            f_csv.writerow(line)

        return item
