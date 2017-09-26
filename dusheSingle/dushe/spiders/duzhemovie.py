# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy import Spider,Request
from time import sleep
import logging
import random
class DuzhemovieSpider(Spider):
    name = "duzhemovie"
    allowed_domains = ["dushemovie.com"]
    start_urls = ['http://dushemovie.com/']
    url="https://dswxapp.dushemovie.com/dsmovieapi/ssl/daily_recmd/list_daily_recmd_dynamic/3"
    postBody={"count":"20","startIndex":"0","userId":"0"}
    def start_requests(self):   	
    	yield Request(url=self.url,method="POST",body=str(self.postBody),callback=self.parse)
    def parse(self, response):
    	jsonData=json.loads(response.body.decode('UTF-8'))
    	yield jsonData
    	while True:
    		sleep(1)
	    	self.postBody["startIndex"]=str(int(self.postBody['startIndex'])+20)
	    	yield Request(url=self.url,method="POST",body=str(self.postBody),callback=self.parse)