from google.appengine.ext import ndb

class Song(ndb.Model):
	song_name = ndb.StringProperty(required=True)
	club_num = ndb.StringProperty(required = True)
	
	@classmethod
	def query_book(cls, ancestor_key):
		return cls.query(ancestor = ancestor_key)
		
	