# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request,Spider
from qiushi.items import QiushiItem


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    #start_urls = ['https://www.qiushibaike.com/text/page/1/']
    def start_requests(self):
        urls = []
        for i in range(1,14):
            page_url = 'https://www.qiushibaike.com/text/page/{}/'.format(i)
            urls.append(page_url)
        for url in urls:
            yield Request(url=url,callback=self.parse)

    def parse(self, response):
        if response.xpath('//*[@id="content-left"]'):
            for res in response.xpath('//*[@id="content-left"]/div'):
                try:
                    item = QiushiItem()
                    text = res.xpath('normalize-space(./a/div/span/text())').extract()[0]
                    #id = res.xpath('./div/div/a[2]/h2/text()').extract()[0]
                    #good = res.xpath('./div/div/span[@class="stats-vote"]/text()').extract()[0]
                    #item['id'] = id
                    item['text'] = text
                    #item['good'] = good
                    yield item
                except:
                    print('格式错误，爬虫结束')
                    

