from datetime import datetime
from app import login
from flask_login import UserMixin
from santa import users_db_functions as usersdb

class User():
    is_authenticated = False
    is_active = False
    is_anonymous = False
    
    santa = None
    
    #returns the ID of the current user
	def get_id():
        returnValue = None
        if santa != None:
            intID = usersdb.findUserByUsername(santa.iden.name)[0]
            returnValue = str(intID).decode("utf-8")

        return returnValue

    def is_authenticated():
        return is_authenticated

    def is_active():
        return is_active

    def is_anonymous():
        return is_anonymous

#helper function for flask-login
@login.user_loader
def load_user(id):
    return usersdb.findUserByID(id)