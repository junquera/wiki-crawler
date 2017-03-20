import md5

def hash(text):
	instance = md5.md5(text)
	return instance.hexdigest()

