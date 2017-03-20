# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import config

from neo4j.v1 import GraphDatabase, basic_auth

from wiki.utils import hash

class WikiPipeline():
	def process_item(self, item, spider):
		print("%s\t%s"%(item['title'], item['url']))
		return item

class SerializePipeline():
	def open_spider(self, spider):
		self.file = open('items.json', 'wb')

	def close_spider(self, spider):
		self.file.close()

	def process_item(self, item, spider):
		dictItem = dict(item)
		dictItem['url'] = hash(dictItem['url'])
		dictItem['referer'] = hash(dictItem['referer'])
		line = json.dumps(dictItem) + "\n"
		self.file.write(line)
		return item

class Neo4jPipeline():
	def open_spider(self, spider):
		self.driver = GraphDatabase.driver("bolt://%s:%d"%(config.n4j['url'], config.n4j['port']), auth=basic_auth(config.n4j['user'], config.n4j['password']))
		self.session = self.driver.session()

	def close_spider(self, spider):
		self.session.close()

	def process_item(self, item, spider):
		title = item['title']
		url = hash(item['url'])
		referer = hash(item['referer'])
		self.session.run("CREATE (a:Article {title: {title}, referer: {referer}, url: {url}})",
								{"title": title, "referer": referer, "url": url})

# Si no hay un return y este pipeline se configura antes, es el 
# unico que accede a los Items
#	class TestPipeline():
#		def process_item(self, item, spider):
#			print("Yo tambien proceso %s"%(item['title']))
