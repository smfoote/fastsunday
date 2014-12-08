from google.appengine.ext import ndb
from google.appengine.api import users
from user import User

class Fast(ndb.Model):
    date = ndb.DateProperty()
    title = ndb.StringProperty()
    committed_user_count = ndb.IntegerProperty()
