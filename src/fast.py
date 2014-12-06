from google.appengine.ext import ndb
from google.appengine.api import users
from user import User

class Fast(ndb.Model):
    user = ndb.ReferenceProperty(User, collection_name="user_fasts")
    date = ndb.DateProperty()
