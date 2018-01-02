# -*- coding: utf-8 -*-
import scrapy
from scrapy import  Request
from douban.items import DoubanItem

class DianyingSpider(scrapy.Spider):
    name = 'dianying'
    allowed_domains = ['https://movie.douban.com/top250']
    def start_requests(self):
        urls = []
        url = 'https://movie.douban.com/top250?start={}'
        for i in range(0,10):
            page_url = url.format(i*25)
            urls.append(page_url)
            for new_url in urls:
                yield Request(url=new_url,callback=self.parse)

    def parse(self, response):
        if response.xpath('//*[@id="content"]/div/div[1]/ol/li'):
            try:
                for pro in response.xpath('//*[@id="content"]/div/div[1]/ol/li'):
                    item = DoubanItem()
                    title = pro.xpath('./div/div[2]/div[1]/a/span[1]/text()').extract()[0]
                    pingfen = pro.xpath('./div/div[2]/div[2]/div/span[2]/text()').extract()[0]
                    pingjia = pro.xpath('./div/div[2]/div[2]/div/span[4]/text()').extract()[0]
                    pingyu = pro.xpath('./div/div[2]/div[2]/p[2]/span/text()').extract()[0]
                    item['title'] = title
                    item['pingfen'] = pingfen
                    item['pingjia'] = pingjia
                    item['pingyu'] = pingyu
                    yield item

            except:
                print('格式不对，sorry')
                



