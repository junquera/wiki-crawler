from scrapy.exceptions import IgnoreRequest

from wiki.utils import hash

# https://doc.scrapy.org/en/1.3/topics/settings.html#std:setting-DUPEFILTER_CLASS
class AvoidDupicatesDownloaderMiddleware():
	visited = []
	def process_request(self, request, spider):
		digest = hash(request.url)
		if digest in self.visited:
			raise IgnoreRequest("Duplicated url %s"%(request.url))
		else:
			self.visited.append(digest)
			return None
