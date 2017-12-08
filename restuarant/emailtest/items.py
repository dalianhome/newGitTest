# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EmailtestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class ProtienItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    # des = scrapy.Field()
    pass
class RestaurantItem(scrapy.Item):
    name = scrapy.Field()
    number = scrapy.Field()
    address = scrapy.Field()
    rating = scrapy.Field()