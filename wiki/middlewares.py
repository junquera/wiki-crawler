import md5
from scrapy.exceptions import IgnoreRequest

def hash(text):
	instance = md5.md5(text)
	return instance.hexdigest()

class AvoidDupicatesDownloaderMiddleware():
	visited = []
	def process_request(self, request, spider):
		digest = hash(request.url)
		if digest in self.visited:
			raise IgnoreRequest("Duplicated url %s"%(request.url))
		else:
			self.visited.append(digest)
			return None
