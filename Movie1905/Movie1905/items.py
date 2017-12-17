# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Movie1905Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    Actor = scrapy.Field()
    miaoshu = scrapy.Field()
    descr = scrapy.Field()
    time = scrapy.Field()
    url = scrapy.Field()

