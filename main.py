import sys
from corpus.wordscore import WordScore
from nltk.corpus import wordnet
class main: 
    def __init__(self):
	self.member = "token"        

    def main(self):
	sources = ["The quick brown fox jumps over the lazy dog", "This is ninja stuff right there",
               "This is micky changing connotation project from eclipse:)"]
	# get the corpus interface
	sys.path.append('corpus')
	c = WordScore('corpus/data/swn.txt')
	# get the score of the first word given as a command line argument
	print c.getScore(sys.argv[1])


if __name__ == '__main__':
    m = main()
    m.main()
