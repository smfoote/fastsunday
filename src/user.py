from google.appengine.ext import ndb
from google.appengine.api import users

class User(ndb.Model):
    id = ndb.StringProperty()
    user = ndb.UserProperty()
    fasts = ndb.JsonProperty()
