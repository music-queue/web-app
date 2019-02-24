from google.appengine.ext import ndb

class Song(ndb.Model):
	song_name = ndb.StringProperty(required=True)
	club_num = ndb.StringProperty(required = True)
	artist_name = ndb.StringProperty(required = False)
	current_score = ndb.IntegerProperty(required = True)
	
	@classmethod
	def query_book(cls, ancestor_key):
		return cls.query(ancestor = ancestor_key)