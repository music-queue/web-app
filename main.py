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

class Register(webapp2.RequestHandler):
    """ Handles the main page, and renders it
    """
    def get(self):
        #Find and render the template
        template=template_env.get_template('html/register.html')
        self.response.write(template.render())
class About(webapp2.RequestHandler):
    """ Handles the main page, and renders it
    """
    def get(self):
        #Find and render the template
        template=template_env.get_template('html/about.html')
        self.response.write(template.render()) 

class MainPage(webapp2.RequestHandler):
    """ Handles the main page, and renders it
    """
    def get(self):
        #Find and render the template
        template=template_env.get_template('html/home.html')
        self.response.write(template.render())
		
class Playlist(webapp2.RequestHandler):
    """ Handles the main page (Map page), and renders it
    """
    def getSongsData(self, test):
	    songs = Song.query().fetch()
	    d = []
	    for song in sorted(songs):
	    	d.append((song.song-name, song.current_score))
	    logging.info(d)
	
    def get(self):
		delete = self.request.get('delete-all')
		if (delete != ""):
			entities = Song.query().fetch()
			for entity in entities:
				entity.key.delete()
		song = self.request.get('song-name')
		club = self.request.get('club-name')
		
		
		songs = Song.query().fetch()
		
		
		songs_d = {"songsss":[]}
		found = False
		if (song != ""):
			for song2 in songs:
				if song == song2.song_name:
					logging.info(song2.key)
					update_song = song2.key.get()
					logging.info(update_song)
					update_song.current_score += 1
					logging.info(song2.key)
					update_song.put()
					found = True
					break
			if (not found):
				song_record = Song(song_name = song, club_num = club, current_score = 1)
				song_record.put()
				songs_d["songsss"].append(song)
		
		for song2 in songs:
			if (song2.club_num == club):
				songs_d["songsss"].append(song2.song_name)
		if (len(songs_d) == 0):
			songs_d["songsss"].append("Please add a song to see your playlist!")
		
		template=template_env.get_template('html/playlist.html')
		self.response.write(template.render(songs_d))
    def post(self):
		delete = self.request.get('delete-all')
		if (delete != ""):
			entities = Song.query().fetch()
			for entity in entities:
				entity.key.delete()
		song = self.request.get('song-name')
		club = self.request.get('club-name')
		
		
		ancestor_key = ndb.Key('club', club) 
		songs = Song.query().fetch()
		songs_d = {"songsss":[]}
		found = False
		if (song != ""):
			for song2 in songs:
				if song == song2.song_name:
					logging.info(song)
					logging.info(song2.key)
					update_song = song2.key.get()
					logging.info(update_song)
					update_song.current_score += 1
					logging.info(song2.key)
					update_song.put()
					found = True
					break
			if (not found):
				song_record = Song(song_name = song, club_num = club, current_score = 1)
				song_record.put()
				songs_d["songsss"].append(song)
		
		for song2 in songs:
			if (song2.club_num == club):
				songs_d["songsss"].append(song2.song_name)
		if (len(songs_d) == 0):
			songs_d["songsss"].append("Please add a song to see your playlist!")
		
		template=template_env.get_template('html/playlist.html')
		self.response.write(template.render(songs_d))
		


#Send calls to the correct class, thereby rendering the correct template
app = webapp2.WSGIApplication([
    ('/music', MainPage),    #Country details page
	('/playlist', Playlist),	#Playlist details page
	('/register', Register),
	('/about', About),
    ('/.*', MainPage),                   #Main map page/handles every call not to another page
], debug = True)