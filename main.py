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
	word = 'coconut'
	print wordnet.synsets(word)
	print wordnet.synsets(word)[0]
	print c.getScore(word)


if __name__ == '__main__':
    m = main()
    m.main()
