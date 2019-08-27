# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CycleCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    model = scrapy.Field()
    amount = scrapy.Field()
    link = scrapy.Field()

    pass
