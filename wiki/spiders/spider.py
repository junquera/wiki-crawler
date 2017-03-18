# -*- coding: utf-8 -*-
import scrapy

from wiki.items import Article

class SpiderSpider(scrapy.Spider):
		name = "spider"
		allowed_domains = ["es.wikipedia.org"]
		start_urls = (
			'https://es.wikipedia.org/wiki/Parque_de_la_Ciudadela',
		)
		
		def parse(self, response):	
			title = response.css('#firstHeading::text').extract_first()
			for url in response.css('a::attr(href)').extract():
					yield scrapy.Request(response.urljoin(url), callback=self.parse)
			pass
			yield Article(title=title, url=response.url, referer=response.request.headers.get('Referer', None))
