class DummyAlgorithm():
	def __init__(self, corpus):
		self.corpus = corpus

	def getScore(self, text):
		"""Returns an integer representing the score associated to the text"""
		score = [0,0]
		
		words = text.split(' ')
		if len(words) == 0:
			return score

		for word in words:
			res = self.corpus.getScore(word)
			tmpScore = [0,0]
			for resi in res:
				tmpScore[0] += float(resi[0])
				tmpScore[1] += float(resi[1])

			if len(res) > 0:
				# calculate average scores for a word
				# from all the synsets, if found 
				tmpScore[0] /= len(res)
				tmpScore[1] /= len(res)
				score[0] += tmpScore[0]
				score[1] += tmpScore[1]

		# calculate average score for the entire text	
		score[0] /= len(words)
		score[1] /= len(words)
				 
		return score
