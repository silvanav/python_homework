import os

class FastaParser(object):
	def __init__(self, path):
		self.path = path
#		if len(os.listdir(path)) == 0:
#			raise IOError
		if not os.path.exists(path):
			raise IOError

	def count(self):
		file = open(self.path, 'r')
		splitting = file.split('>')
		num = 0
		for splitting in file:
			num += 1
		return num
