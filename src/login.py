import os
import logging
from google.appengine.api import users

import jinja2
import webapp2

from user import User

import fastsunday_utils as utils

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Login(webapp2.RequestHandler):
  def get(self):
    continue_url = self.request.get('continue')
    if not continue_url:
      continue_url = '/'
    user = users.get_current_user()
    if user:
      existing_user = User.query(User.id == user.email()).fetch(1)
      if not existing_user:
        User(id=user.email(), user=user).put()
      self.redirect(continue_url)
    else:
      data = { 'login_url': users.create_login_url('/login') }
      html = utils.render_template('tl/login.html', data)
      self.response.write(html)

app = webapp2.WSGIApplication([
    ('/login', Login),
], debug=True)
