from scrapy.spiders import Spider
import scrapy
import re
import json
from datetime import datetime

class PhonescrawlerSpider(Spider):
    name = "phonesCrawler"
    allowed_domains = ["www.daraz.com.np"]
    start_urls = ["https://www.daraz.com.np/smartphones/?page="]


    custom_settings = {
        'FEEDS':{
            f'data/{name}.csv': {
                'format':'csv',
                'overwrite': True
            }

        }
    }

    def start_requests(self):        
        for i in range(1, 22):
            yield scrapy.Request(url=self.start_urls[0]+str(i), callback=self.parse)


    def parse(self, response):
        script_tag = response.xpath('//script[@type="application/ld+json"]/text()').extract()[-1]

        json_data = json.loads(script_tag)["itemListElement"]

        urls = []
        for item in json_data:            
            urls.append(item['url'])
        

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_product)


    def parse_product(self, response):
        data = dict()
        text = response.xpath("//script[contains(text(), 'window.LZD_RETCODE_PAGENAME = ')]").get()
        details_pattern = r'app\.run\((.*?)\);'
        text = re.search(details_pattern, text)
        text = text.group(1)
        # text = text.replace('\'', '"')
        jsn_content = json.loads(text)
        jsn_content = jsn_content['data']['root']['fields']
        data['title'] = jsn_content['product']['title']
        data['time'] = datetime.now().strftime("%d/%m/%y")
        data['specifications'] = jsn_content['specifications']
        data['price'] = jsn_content['skuInfos']['0']['price']
        data['review'] = jsn_content['review']
        data['url'] = response.url
        yield data
