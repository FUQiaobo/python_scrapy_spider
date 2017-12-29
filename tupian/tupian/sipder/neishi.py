# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from tupian.items import TupianItem
from scrapy.spider import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class NeishiSpider(scrapy.Spider):
    name = 'neishi'
    start_urls = ['http://www.quanjing.com/imgbuy/tid185t000015.html']
    # def start_requests(self):
    #     urls = []
    #     url = 'http://www.quanjing.com/search.aspx?q=%E7%94%9C%E7%82%B9||1|100|2|2||||#%E7%94%9C%E7%82%B9||1|100|{}|2||||'
    #     for i in range (10):
    #         page_url = url.format(i)
    #         urls.append(page_url)
    #     for only_url in urls:
    #         yield Request(url=only_url,callback=self.parse)

    def parse(self, response):
        item = TupianItem()
        src = response.xpath('//*[@id="picurl"]/@src').extract()
        item['image_url'] = src
        yield item