import sys
import ConfigParser
# from corpus.wordscore import WordScore
from nltk.corpus import wordnet
from logic.algorithm import DummyAlgorithm
from corpus.sentiwordnet import SentiWordNet
from datasource.imdb import ImdbMysql
class main: 
    def __init__(self):
	pass 

    def main(self):
    	# read configuration file to determine functionality
	config = ConfigParser.ConfigParser()
	config.read('settings.cfg')
	
	# select corpus according to config options
	if config.get('Corpus', 'name') == 'SentiWordNet':
		corpus = SentiWordNet(config.get('Corpus','file'))
	else:
		print 'No other corpuses are interfaced besides SWN.'
		quit()
	
	# select algorithm according to config options
	if config.get('Algorithm', 'name') == 'dummy':
		algorithm = DummyAlgorithm(corpus)
	elif config.get('Algorithm', 'name') == 'neural net':
		print 'I wish a neural net was implemented. Unfortunately it isn\'t :).'
		quit()
	else:
		print 'No other algorithm is implemented besides the dummy algorithm.'
		quit()

	# select input according to config options
	if config.get('Data', 'name') == 'console':
		# read a sentence from the console.
		# not implemented yet
		pass
	elif config.get('Data', 'name') == 'IMDB':
		# do stuff for IMDB reviews
		res = ImdbMysql().getAllReviews()
		sources = res[0]
		ratings = res[1]
	else:
		# some hardcoded values, just to see if it works
		sources = [
			"The quick brown fox jumps over the lazy dog", 
			"This is ninja stuff right there", 
			"The girl has an apple"
		]
	
	# get the score associated with each text from the data source	
	for idx, text in enumerate(sources):
		#print "<<" + text + ">> has score " + str(algorithm.getScore(text))
		#if ratings[idx] > 0:
		#	print " and the associated (initial) rating was " + str(ratings[idx])
		#print "\n\n"
		# this is Spartaa! Only works if ratings for textts exist
		score = algorithm.getScore(text)
		print str(score[0]) + "\t" + str(score[1]) + "\t" + str(ratings[idx])


if __name__ == '__main__':
    m = main()
    m.main()
