# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from thisav.items import ThisavItem


class AdultavSpider(scrapy.Spider):
    name = 'adultav'
    allowed_domains = ['www.thisav.com']
    #start_urls = ['http://www.thisav.com/videos']

    def start_requests(self):
        urls = []
        url = 'http://www.thisav.com/videos?o=mr&type=&c=0&t=a&page={}'
        for i in range(1,11):
            page_url =url.format(i)
            urls.append(page_url)

        for one_url in urls:
            yield Request(url=one_url,callback=self.parse)

    def parse(self, response):
        item = ThisavItem()
        if response.xpath('//*[@id="content"]/div[1]/div[1]/div[@class="video_box"]'):
            for res in response.xpath('//*[@id="content"]/div[1]/div[1]/div[@class="video_box"]'):
                title = res.xpath('./a/span/text()').extract()[0]
                time = res.xpath('normalize-space(./div[1]/text())').extract()[0]
                link = res.xpath('./a/@href').extract()[0]
                src = res.xpath('./a/img/@src').extract()[0]
                item['title'] = title
                item['time'] = time
                item['link'] = link
                item['src'] = src
                yield item

        else:
            print('格式不对，不要捉急')
            


