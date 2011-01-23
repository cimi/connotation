import sys
import ConfigParser
# from corpus.wordscore import WordScore
from nltk.corpus import wordnet
# from logic.algorithm import Algorithm
class main: 
    def __init__(self):
	self.member = "token"        

    def main(self):
	config = ConfigParser.ConfigParser()
	config.read('settings.cfg')
	print config.get('Algorithm', 'name')
	print config.get('Data', 'name')
	print config.get('Corpus', 'name')
	print config.get('Corpus','file')
	
	sources = ["The quick brown fox jumps over the lazy dog", "This is ninja stuff right there",
               "This is micky changing connotation project from eclipse:)",
               "The girl has an apple"]
	
	
	# get the corpus interface
	# c = WordScore('corpus/data/swn.txt')
	# get the score of the first word given as a command line argument
	# print c.getScore(sys.argv[1])
	quit()	
	a = Algorithm();
	for text in sources:
		print "<<" + text + ">> has score " + str(a.getScore(text)) + "\n\n\n"


if __name__ == '__main__':
    m = main()
    m.main()
