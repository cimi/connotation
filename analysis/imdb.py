class AnalyzeImdbData:
	def __init__(self, datafile):
		f = open(datafile, "r")
		ratings = {}
		for line in f:
			row = line.split('\t')
			rating = int(row[2].strip())
			if rating not in ratings:
				ratings[rating] = []
			ratings[rating].append([float(row[0]), float(row[1])])
		self.ratings = ratings 
	
	def avgScores(self):
		ratings = self.ratings	
		print "Rating <-> avg pos score <-> avg neg score <-> no. of inputs"
		for k,v in ratings.iteritems():
			# do this more nicely, with a reducer?
			avg = [0, 0]
			for pair in v:
				avg[0] += pair[0]
				avg[1] += pair[1]
			avg[0] /= len(v)
			avg[1] /= len(v)
			print k, avg, len(v)

	def simpleConfirmation(self):
		ratings = self.ratings
		correctness = {}
		print "Rating <-> % of correct evaluations"
		for k,v in ratings.iteritems():
			correctness[k] = 0
			for pair in v:
				if (pair[0] - pair[1]) > 0 and k >= 5 or k < 5 and (pair[0] - pair[1] < 0) or pair[0]-pair[1] == 0:
					correctness[k] += 1
			# calculate it as a percentage
			correctness[k] = correctness[k] * 100 / len(v)
			print "{0} -> {1}%".format(k, correctness[k])
		print "Average success rate:"
		success = 0
		for k,x in correctness.iteritems():
			success += x
		print "{0}%".format(success // 10)
	

test = AnalyzeImdbData('imdb.out')
test.avgScores()
test.simpleConfirmation()
