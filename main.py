#Import statements
from google.appengine.ext import ndb
import webapp2
import json
from google.appengine.api import urlfetch
import logging
import jinja2
from db import Song

#Creating variables for template loading
template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader= template_loader)

class MainPage(webapp2.RequestHandler):
    """ Handles the main page (Map page), and renders it
    """
    def get(self):
        #Find and render the template
        template=template_env.get_template('html/main.html')
        self.response.write(template.render())
class MainPage2(webapp2.RequestHandler):
    """ Handles the main page (Map page), and renders it
    """
    def get(self):
        #Find and render the template
        template=template_env.get_template('html/home.html')
        self.response.write(template.render())
		
class Playlist(webapp2.RequestHandler):
    """ Handles the main page (Map page), and renders it
    """
    def get(self):
        #Find and render the template
		
		song = self.request.get('song-name')
		if (song != ""):
			song_record = Song(song_name = song)
			song_record.put()
			
		list_of_entities = ndb.get_multi(list_of_keys)
		logging.info(list_of_entities)
		template=template_env.get_template('html/playlist.html')
		self.response.write(template.render())
        
#Send calls to the correct class, thereby rendering the correct template
app = webapp2.WSGIApplication([
    ('/music', MainPage2),    #Country details page
	('/playlist', Playlist),	#Playlist details page
    ('/.*', MainPage),                   #Main map page/handles every call not to another page
], debug = True)