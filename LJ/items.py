# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LjItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    city = scrapy.Field()
    community_name = scrapy.Field()
    type = scrapy.Field()
    acreage = scrapy.Field()
    orientation = scrapy.Field()
    style = scrapy.Field()
    elevator = scrapy.Field()
    distinct = scrapy.Field()
    floor = scrapy.Field()
    follower = scrapy.Field()
    visitor = scrapy.Field()
    create_at = scrapy.Field()
    tag = scrapy.Field()
    total_price = scrapy.Field()
    unit_price = scrapy.Field()
    house_code = scrapy.Field()

