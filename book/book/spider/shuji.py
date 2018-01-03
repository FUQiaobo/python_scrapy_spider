# -*- coding: utf-8 -*-
import scrapy
from book.items import BookItem
from scrapy import Request
import logging

class ShujiSpider(scrapy.Spider):
    name = 'shuji'
    allowed_domains = ['book.douban.com']

    def start_requests(self):
        url = 'https://book.douban.com/tag/'
        tag = ['小说','外国文学','文学','随笔']
        for i in tag:
            urls = url+i
            yield Request(url = urls,callback=self.parse)

    def parse(self, response):
        if response.xpath('//*[@id="subject_list"]/ul/li'):   #将得到的页面地址传送给单个页面处理函数进行处理 -> parse_content()
            for pro1 in response.xpath('//*[@id="subject_list"]/ul/li'):
                link = pro1.xpath('normalize-space(./div[2]/h2/a/@href)').extract()[0]

                yield Request(url=link,callback=self.parse_content,meta={'dont_redirect': True,"handle_httpstatus_list": [302]})
        next_page = response.xpath('//*[@id="subject_list"]/div[2]/span[4]/a/@href').extract()[0]
        if next_page:  #如果存在下一页，则将下一页链接返回自身
            realy_next_page = 'https://book.douban.com'+next_page
            yield Request(url=realy_next_page,callback=self.parse,meta={'dont_redirect': True,"handle_httpstatus_list": [302]})
    def parse_content(self,response):
        item = BookItem()
        title = response.xpath('//*[@id="wrapper"]/h1/span/text()').extract()[0]
        jianjie = response.xpath('normalize-space(//*[@id="info"])').extract()[0]
        neirong = response.xpath('//*[@id="link-report"]/div[1]/div/p/text()|//*[@id="link-report"]/span[1]/div/p/text()').extract()[0]
        zuozhe = response.xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div/div/p/text()|//*[@id="content"]/div/div[1]/div[3]/div[2]/span[1]/div/p/text()').extract()[0]
        pingfen = response.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()').extract()[0]
        pingjia = response.xpath('//*[@id="interest_sectl"]/div/div[2]/div/div[2]/span/a/span/text()').extract()[0]
        item['title'] =title
        item['jianjie'] =jianjie
        item['neirong'] = neirong
        item['zuozhe'] =zuozhe
        item['pingfen'] =pingfen
        item['pingjia'] =pingjia
        yield item
