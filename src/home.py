import os
import logging
import jinja2
import webapp2

from google.appengine.api import users

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Home(webapp2.RequestHandler):
    def get(self):
      template = JINJA_ENVIRONMENT.get_template('tl/index.html')
      self.response.write(template.render({'logout_url': users.create_logout_url('/')}))

app = webapp2.WSGIApplication([
    ('/', Home),
], debug=True)
