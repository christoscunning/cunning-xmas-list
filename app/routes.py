from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

from santa import test
from santa import users_db_functions as userdb
from santa import auth
from santa import xmaslist

#main landing page
@app.route("/")
def index():
    username = None
    if 'user_id' in session:
        username = userdb.findUserByID(session['user_id'])[2]
    user = {'username': username}

    #slist.append("Name":"GivingTo")
    masterlist = xmaslist.xmasShuffle(0)
    slist = masterlist.toDictionary()

    return render_template('index.html', title='Home', user=user, slist = slist)

#login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #get data from form if valid
        d_username = form.username.data
        d_password = form.password.data
        d_remember_me = form.remember_me.data
        #check if user exists in database
        if userdb.findUserByUsername(d_username) == 1:
            flash('Login failed. invalid password or username')
            return redirect(url_for('login'))
        # get user hashed_password from database using username
        stored_hashed_password = userdb.findUserByUsername(d_username)[1]
    
        #verify user log-in using auth module
        if auth.verify_password(stored_hashed_password, d_password):
            #success, redirect to home page
            flash('Login succesful for user {}, remember_me={}'.format(d_username, d_remember_me))
            #set current user
            session['user_id'] = userdb.findUserByUsername(d_username)[0]
            return redirect(url_for('index'))
        else:
            flash('Login failed. invalid password or username')
            return redirect(url_for('login'))

    return render_template('login.html', title='Sign In', form=form)


#if run from cmd line, run flask with external host
if __name__ == "__main__":
    print("poop")
    app.run(debug=True, host='0.0.0.0')
