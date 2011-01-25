import MySQLdb

class ImdbMysql():
	def __init__(self):
		self.db = MySQLdb.connect("localhost", "root" , "", "sandbox") 	
	
	def getAllReviews(self):
		c = self.db.cursor()
		c.execute("""SELECT * FROM reviews""")
		results = c.fetchall()
		texts = []
		ratings = []
		for result in results:
			# unpack tuple
			iden, added, review, rating, url = result
			texts.append(review)
			ratings.append(rating)
		return [texts,ratings]
