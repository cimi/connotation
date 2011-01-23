from corpus.wordscore import WordScore
class Algorithm():
	def getScore(self, text):
		"""Returns an integer representing the score associated to the text"""
		score = [0,0]
		# print "algorithm.score: " + str(score)
		c = WordScore('corpus/data/swn.txt')
		
		words = text.split(' ')
		# print words
		w=0
		for word in words:
			# print c.getScore(word)
			res = c.getScore(word)
			i=0
			tmpScore = [0,0]
			for resi in res:
				# print resi
				# score[-1] += float(resi[-1])
				tmpScore[0] += float(resi[0])
				tmpScore[1] += float(resi[1])
				i += 1
			if i>0:
				tmpScore[0] /= i
				tmpScore[1] /= i
				score[0] += tmpScore[0]
				score[1] += tmpScore[1]
				w += 1	
		score[0] /= w
		score[1] /= w
				 
		return score
