# -*- coding: utf-8 -*-
import scrapy
from Movie1905.items import Movie1905Item



class TodaymovieSpider(scrapy.Spider):
    name = 'todayMovie'
    allowed_domains = ['www.1905.com']
    start_urls = ['http://vip.1905.com/?fr=homepc_rbdp_more']

    def parse(self, response):
        subSelector = response.xpath(
                                     '//section[2]/div/div/div[2]/div[1]/ul/li|\
                                     //section[3]/div/div/div[2]/div/div/ul/li|\
                                     //section[4]/div/div/div[2]/div/div/ul/li|\
                                    //section[5]/div/div/div[2]/div/div/ul[1]/li|\
                                    //section[5]/div/div/div[2]/div/div/ul[2]/li|\
                                    //section[6]/div/div/div[2]/div/ul/li'
                                     )
        try:
            for x in subSelector:
                item = Movie1905Item()
                item['name'] = x.xpath('./h3/a/span[1]/text()').extract()[0]
                item['miaoshu'] = x.xpath('./h3/a/span[2]/text()').extract()[0]
                item['time'] = x.xpath('./h3/a/span[3]/text()').extract()[0]
                item['Actor'] = x.xpath('./h3/a/span[5]/text()').extract()[0]
                item['descr'] = x.xpath('./h3/a/span[6]/text()').extract()[0]
                item['url'] = x.xpath('./h3/a/span[7]/text()').extract()[0]
                yield item

        except:
            print('该影片错误，继续抓取下一个')
            continue











