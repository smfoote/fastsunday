""" Create a new fast """
import logging
from google.appengine.api import users
from datetime import datetime

import webapp2

import fastsunday_utils as utils
from fast import Fast

class CreateFast(webapp2.RequestHandler):
    """ Class for creating a new fast """
    def get(self):
        """ Render the create fast form """
        if not users.is_current_user_admin():
            self.redirect('/')
        else:
            html = utils.render_template('tl/createFast.html', {})
            self.response.write(html)

    def post(self):
        """ Handle the create fast form submit """
        date_response = self.request.get('date')
        if not date_response:
            self.redirect('/createFast?error=date')
        date_val = datetime.strptime(date_response, '%Y-%m-%d')
        fast = Fast(date=date_val, title=self.request.get('title'), committed_user_count=0)
        fast.put()

        # Change this to '/fasts' or '/admin' when those pages are ready
        self.redirect('/')

app = webapp2.WSGIApplication([
    ('/createFast', CreateFast),
], debug=True)
