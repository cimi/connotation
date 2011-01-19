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
				# get set of keys associated with a score & offset
				synsets = row[-1].strip().replace("#",".").split(' ')
				for synset in synsets:
					synset = synset[:-1] + '0' + synset[-1]
					self.swn[synset] = row[2:-1]

	def getScore(self, word):
		"""Returns an integer representing the score associated to a word by SentiWordNet""" 
		# first, get the synset of the word from wordnet
		synsets = wordnet.synsets(word)
		print "The word " + word + " is associated with the following synsets:"			
		res = []
		for synset in synsets:
			# print out synsets for debugging
			# print synset.name + " with offset " + str(synset.offset) + " and pos " + synset.pos 
			# get a list of all scores that match in swn
			# print self.swn['comment.v.2']
			if self.swn.has_key(synset.name):
				res.append(self.swn[(synset.name)])
		return res

