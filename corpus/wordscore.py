from random import randint
from nltk.corpus import wordnet
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
		synsets = wordnet.synsets(word)
		res = []
		for synset in synsets:
			# get a list of all scores that match in swn
			if self.swn.has_key((synsets[0].pos, synsets[0].offset)):
				res.append(self.swn[(synset.pos, synset.offset)][0:1])
		return res

