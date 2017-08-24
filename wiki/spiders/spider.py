# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import Rule
from scrapy.link import Link
from wiki.items import Article

class SpiderSpider(scrapy.Spider):
		name = "spider"
		allowed_domains = ["es.wikipedia.org"]
		start_urls = (
			'https://es.wikipedia.org/wiki/Parque_de_la_Ciudadela',
		)

		def parse(self, response):
			title = response.css('#firstHeading::text').extract_first()
			url = response.url
			referer = response.request.headers.get('Referer', None)

			for nextUrl in response.css('#mw-content-text a::attr(href)').extract():
				yield scrapy.Request(response.urljoin(nextUrl), callback=self.parse)

			yield Article(title=title, url=response.url, referer=response.request.headers.get('Referer', None))
