import sys
import ConfigParser
# from corpus.wordscore import WordScore
from nltk.corpus import wordnet
from logic.algorithm import DummyAlgorithm
from corpus.sentiwordnet import SentiWordNet
class main: 
    def __init__(self):
	pass 

    def main(self):
	config = ConfigParser.ConfigParser()
	config.read('settings.cfg')
	print config.get('Algorithm', 'name')
	print config.get('Data', 'name')
	print config.get('Corpus', 'name')
	print config.get('Corpus','file')
	
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
		pass
		# read a sentence from the console.
	elif config.get('Data', 'name') == 'IMDB reviews':
		pass
		# do stuff for IMDB reviews
	else:
		sources = ["The quick brown fox jumps over the lazy dog", "This is ninja stuff right there", "The girl has an apple"]
	
	# get the score associated with each text from the data source	
	for text in sources:
		print "<<" + text + ">> has score " + str(algorithm.getScore(text)) + "\n\n\n"


if __name__ == '__main__':
    m = main()
    m.main()
