import hashlib

def hash(text):
	instance = hashlib.md5()
	instance.update(bytearray(text, "utf-8"))
	return instance.hexdigest()
