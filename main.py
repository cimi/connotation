import sys

class main: 
    def __init__(self):
	self.member = "token"        

    def main(self):
	sources = ["The quick brown fox jumps over the lazy dog", "This is ninja stuff right there"]
	print sources
	print self.member


if __name__ == '__main__':
    m = main()
    m.main()
