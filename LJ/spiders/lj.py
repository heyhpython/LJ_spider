# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from copy import deepcopy
from scrapy_redis.spiders import RedisCrawlSpider
from LJ.items import LjItem
import re
import json
import logging
logger = logging.getLogger(__name__)

class LjSpider(RedisCrawlSpider):
    name = 'lj'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://m.lianjia.com/city/']
    redis_key = "lj"

    rules = (
        # 找到所有的城市链接
        # Rule(LinkExtractor(restrict_xpaths=("//div[@class='block city_block']/a",)), follow=False),

        # 找到二手房
        # Rule(LinkExtractor(restrict_xpaths=("//h2[@title='二手房']//a",)), follow=False),

        # 找到房源url
        Rule(LinkExtractor(restrict_xpaths=("///li[@class='pictext']/a",)), follow=True,
             callback="parse_detail"),

        # 翻页
        Rule(LinkExtractor(restrict_xpaths=("//li[@class='loading_box']/a",)), follow=True),

    )

    def parse_detail(self, response):

        item = {}
        #logger.error(response.url)
        item['name'] = response.xpath('//h3[@class="house_desc lazyload_ulog"]/text()').extract_first()
        item['house_code'] = json.loads(response.xpath('//div[@class="content_area"]/@data-info').extract_first()).get(
            'house_code', '')
        item['city'] = response.xpath('//em[@class="city"]/text()').extract_first()
        item['community_name'] = response.xpath('//a[@class="post_ulog"]/text()').extract_first()

        # 售价房型面积
        temp1 = response.xpath('//h3[@class="similar_data"]//p[@class="red big"]//text()').extract()
        item['type'] = temp1[2] if temp1[2] else ""
        item['acreage'] = temp1[3] if temp1[3] else ""
        item['total_price'] = temp1[0] if temp1[0] else ""

        temp2 = response.xpath('//ul[@class="house_description big lightblack"]/li/text()').extract()
        #print(temp2)
        item['unit_price'] = temp2[0] if temp2[0] else ""
        item['orientation'] = temp2[2] if temp2[2] else ""
        item['floor'] = temp2[3] if temp2[3] else ""
        item['elevator'] = 1 if "有" in temp2[5] else 0
        item['style'] = temp2[6] if temp2[6] else ""
        item['create_at'] = temp2[1] if temp2[1] else ""

        item['distinct'] = response.xpath('//p[@class="marker_title"]/text()').extract_first()

        temp3 = response.xpath('//div[@class="data flexbox"]/div/strong/text()').extract()
        item['visitor'] = temp3[1] if temp3[1] else 0
        item['follower'] = temp3[2] if temp3[2] else 0
        yield deepcopy(item)
