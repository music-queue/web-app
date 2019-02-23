#Import statements
from __future__ import absolute_import
from google.appengine.ext import ndb
import webapp2
import json
from google.appengine.api import urlfetch
import logging
import jinja2
from db import Song

template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader= template_loader)

class MainPage(webapp2.RequestHandler):
    """ Handles the main page, and renders it
    """
    def get(self):
        #Find and render the template
        template=template_env.get_template('html/main.html')
        self.response.write(template.render())
 

class MainPage2(webapp2.RequestHandler):
    """ Handles the main page, and renders it
    """
    def get(self):
        #Find and render the template
        template=template_env.get_template('html/home.html')
        self.response.write(template.render())
		
class Playlist(webapp2.RequestHandler):
    """ Handles the main page (Map page), and renders it
    """
    def get(self):
        #Find and render the templatehope
		
		delete = self.request.get('delete-all')
		logging.info("TEST: "+delete)
		if (delete != ""):
			entities = Song.query().fetch()
			for entity in entities:
				entity.key.delete()
		
		song = self.request.get('song-name')
		club = self.request.get('club-name')
		
		songs_d = {"songsss":[]}
		if (song != ""):
			song_record = Song(song_name = song, club_num = club)
			song_record.put()
			songs_d["songsss"].append(song)
		
		ancestor_key = ndb.Key('club', club) 
		songs = Song.query().fetch()
		
		for song in songs:
			logging.info("Next song tried: "+song.song_name)
			logging.info(song.club_num)
			if (song.club_num == club):
				logging.info("Made it: "+song.song_name+ "    "+ song.club_num)
				songs_d["songsss"].append(song.song_name)
		
		template=template_env.get_template('html/playlist.html')
		self.response.write(template.render(songs_d))
		
    def post(self):
		delete = self.request.get('delete-all')
		logging.info("TEST: "+delete)
		if (delete != ""):
			entities = Song.query().fetch()
			for entity in entities:
				entity.key.delete()
		song = self.request.get('song-name')
		club = self.request.get('club-name')
		
		songs_d = {"songsss":[]}
		if (song != ""):
			song_record = Song(song_name = song, club_num = club)
			song_record.put()
			songs_d["songsss"].append(song)
		else:
			songs_d["songsss"].append("Please add a song to see your playlist!")
		
		ancestor_key = ndb.Key('club', club) 
		songs = Song.query().fetch()
		
		for song in songs:
			logging.info("Next song tried: "+song.song_name)
			logging.info(song.club_num)
			if (song.club_num == club):
				logging.info("Made it: "+song.song_name+ "    "+ song.club_num)
				songs_d["songsss"].append(song.song_name)
		
		template=template_env.get_template('html/playlist.html')
		self.response.write(template.render(songs_d))
		


#Send calls to the correct class, thereby rendering the correct template
app = webapp2.WSGIApplication([
    ('/music', MainPage2),    #Country details page
	('/playlist', Playlist),	#Playlist details page
    ('/.*', MainPage),                   #Main map page/handles every call not to another page
], debug = True)