# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import urllib


class OurfirstbotSpider(scrapy.Spider):
    name = 'ourfirstbot'
    start_urls = [
        'https://tr.wikipedia.org/wiki/T%C3%BCrk_Hava_Kuvvetleri',
    ]

    def parse(self, response):
        #yield response
        headings = response.css('.mw-headline').extract()       
        datas = response.css('ul').extract()       
        texts = response.css('p').extract()
        link= response.xpath('///tbody/tr/td/a/@href').extract()
        
        for item in zip(headings, datas,texts,link):
            getlink= BeautifulSoup(item[3]).text
            a = "www.wikipedia.com/{}".format(getlink)
            all_items = {
                'headings' : BeautifulSoup(item[0]).text,
                'datas' : BeautifulSoup(item[1]).text,
                'texts' : BeautifulSoup(item[2]).text,
                'link' : a

            }


            yield all_items