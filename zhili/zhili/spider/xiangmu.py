# -*- coding: utf-8 -*-
from scrapy import Request, Spider


class XiangmuSpider(Spider):
    name = 'environmental'

    def start_requests(self):
        '''第一页单独处理  添加20页 '''
        urls=['http://www.nmgepb.gov.cn/ywgl/hjpj/xmslqk/index.html']

        for i in range(1,21):
            next_page = 'http://www.nmgepb.gov.cn/ywgl/hjpj/xmslqk/index_{}.html'.format(i)
            urls.append(next_page)

        for url in urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):

        first_time = response.xpath('//ul/li[1]/span[3]/text()').extract_first().replace('-', '')
        while int(first_time) <= 20150101: #  整数形式界定时间范围 
            break

        for pro in response.xpath('/html/body/div[3]/div/div[3]/div[2]/ul/li'): #取出每个li
            page_url = pro.xpath('./span[2]/a/@href').extract_first().replace('.', '', 1)#  取出url字符串并替换.
            times = pro.xpath('./span[3]/text()').extract_first().replace('-', '') #  取出时间字符串并替换.
            if int(times) >= 20150101:
                url = 'http://www.nmgepb.gov.cn/ywgl/hjpj/xmslqk' + str(page_url)
                yield Request(url=url, callback=self.parse_page)   #  将拼接的url callback到self.parse_page


    def parse_page(self, response):  #  坑好多系列（分3种情况）

        if response.xpath('//table/tbody/tr[3]'):
            for pro in response.xpath('//table/tbody/tr[3]'):
                pro_name = pro.xpath('./td[2]/text()').extract_first()
                pro_location = pro.xpath('./td[3]/text()').extract_first()
                pro_campy = pro.xpath('./td[4]/text()').extract_first()
                pro_evaluate = pro.xpath('./td[5]/text()').extract_first()
                pro_time = pro.xpath('./td[6]/text()').extract()
                item = {          #
                    'name': pro_name,
                    'location': pro_location,
                    'campy': pro_campy,
                    'evaluate': pro_evaluate,
                    'time': ''.join(pro_time).replace('\xa0', '').replace(' ',''),
                    'url': str(response.url),
                }
                return item

        elif response.xpath('//table/tbody/tr[2]'):
            for pro in response.xpath('//table/tbody/tr[2]'):
                pro_name = pro.xpath('./td[2]//text()').extract()
                pro_location = pro.xpath('./td[3]//p/span//text()').extract_first()
                pro_campy = pro.xpath('./td[4]//p/span//text()').extract_first()
                pro_evaluate = pro.xpath('./td[5]//p/span//text()').extract_first()
                pro_time = pro.xpath('./td[6]//text()').extract()
                item = {
                    'name': ''.join(pro_name).replace('\xa0', '').replace(' ', '').replace('\n', ''),
                    'location': pro_location,
                    'campy': pro_campy,
                    'evaluate': pro_evaluate,
                    'time': ''.join(pro_time).replace('\xa0', '').replace(' ', '').replace('\n', ''),
                    'url': str(response.url),
                }
                return item


        elif response.xpath('//strong[contains(text(),"受理日期：")]/following-sibling::text()[1]'):
            item={
                'name': response.xpath('//strong[contains(text(),"项目名称：")]/following-sibling::text()[1]').extract_first(),
                'location': response.xpath('//strong[contains(text(),"建设地点：")]/following-sibling::text()[1]').extract_first(),
                'campy': response.xpath('//strong[contains(text(),"建设单位：")]/following-sibling::text()[1]').extract_first(),
                'evaluate': response.xpath('//strong[contains(text(),"环境影响评价机构：")]/following-sibling::text()[1]').extract_first(),
                'time': response.xpath('//strong[contains(text(),"受理日期：")]/following-sibling::text()[1]').extract_first(),
                'url': str(response.url),
            }
            return item

        else:
            print(response.url)






