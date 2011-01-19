from random import randint
from sentiwordnet import SentiWordNet
class WordScore():
	
	def __init__(self, fileName):
		"""Reads the contents of SentiWordNet into memory"""
		f = open(fileName, "r")
		self.swn = {}
		for line in f:	
			if line[0] == '#':
				continue
			else:
				row = line.split('\t')
				self.swn[(row[0], row[1])] = row[2:]
	def getScore(self, word):
		"""Returns an integer representing the score associated to a word by SentiWordNet""" 
		# first, get the synset of the word from wordnet

		# use the synset to fetch the associated score for sentiwordnet
		return randint(-5,5)
