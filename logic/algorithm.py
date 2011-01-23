from corpus.wordscore import WordScore
class Algorithm():
	def getScore(self, text):
		"""Returns an integer representing the score associated to the text"""
		score = [0,0]
		c = WordScore('corpus/data/swn.txt')
		
		words = text.split(' ')
		w=0
		for word in words:
			res = c.getScore(word)
			i=0
			tmpScore = [0,0]
			for resi in res:
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
