# -*- coding: utf-8 -*-
import scrapy
import re
from urllib import parse
from scrapy.http import Request
from emailtest.items import RestaurantItem

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['koipy.com']# the page would not turn to next page without this
    start_urls = [
        # 'https://www.koipy.com/shop?parent_id=1&language=zh_cn&Store_page=2'
        'https://www.koipy.com/shop?parent_id=1&language=zh_cn'
        # 'http://www.gnc.com/protein-fitness/protein/whey-protein/?sz=72'
    ]

    def parse(self, response):
        # it = ProtienItem()
        # items = response.xpath('.//ul[@id="search-result-items"]//li')
        # for item in items:
        #  it['name'] = item.xpath('.//div[@class="product-name"]//a//text()').extract()[0].strip()
        #  raw_url = item.xpath('.//div[@class="product-name"]//a//@href').extract()[0].strip()
        #  it['url']= parse.urljoin(response.url,raw_url)
        #  it['price'] = item.xpath('.//div[@class="product-pricing"]//span//text()').extract()[0]
        #  size = item.xpath('.//div[@class="serving-size"]//span[1]//text()').extract()[0]
        #  # print ( name+ " -->"+price +" " + url )
        #  # print('----------------------------')
        #  # yield it
        #
        item = RestaurantItem()
        divs = response.xpath('.//div[@id="yw0"]//div[@class="items"]//ul[@class="thumbnails"]//li[@class="span3"]//div[@class="thumbnail"]')
        for div in divs:
            item['name'] = div.xpath('.//div//div[@class="text-center spa"]//text()').extract()[0]
            item['number'] = div.xpath('.//div//p//text()').extract()[0]
            item['address'] = div.xpath('.//div//p//text()').extract()[1]
            item['rating']= div.xpath('.//div//div[@class="overallRating"]//p//span//text()').extract()[0]
            # print(name + ' : '+ number +"  Addrss:"+address +" Rating"+recommd)
            yield item

        ntpage = response.xpath('.//div[@class="pagination"]//ul[@id="yw1"]//li[@class="next"]//a//@href').extract()[0]
        if ntpage:
            # ntpage = response.urljoin(ntpage)
            yield scrapy.Request(url=parse.urljoin(response.url,ntpage), callback=self.parse)
            # print(nextpage)

    def newparse(self,response):
        print(response.url)