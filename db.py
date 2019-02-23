from google.appengine.ext import ndb

class Song(ndb.Model):
  song_name = ndb.StringProperty(required=True)