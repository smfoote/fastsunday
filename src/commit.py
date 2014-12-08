""" Commit to a fast """
import logging
from google.appengine.api import users
from datetime import datetime

import webapp2

import fastsunday_utils as utils
from fast import Fast
from user import User

class Challenge(webapp2.RequestHandler):
    def get(self, fast_id):
        """ Will you commit to a fast? """
        fast = Fast.get_by_id(fast_id)
        logging.info('HEY THERE')
        logging.info(fast_id)
        if fast:
            data = {'fast_date': fast.date, 'fast_id': fast_id}
            html = utils.render_template('tl/challenge.html', data)
            self.response.write(html)


class Commit(webapp2.RequestHandler):
    """ Class for committing to a fast """
    def get(self, fast_id):
        """ Congratulations, you've committed to a fast """
        logging.info('HEY THERE')
        logging.info(fast_id)
        fast = Fast.get_by_id(fast_id)
        if fast:
            data = {'fast_date': fast.date, 'fast_id': fast_id}
            html = utils.render_template('tl/committed.html', data)
            self.response.write(html)

app = webapp2.WSGIApplication([
    ('/fast/(\d+)/challenge', Challenge),
    ('/fast/(\d+)/commit', Commit),
], debug=True)
