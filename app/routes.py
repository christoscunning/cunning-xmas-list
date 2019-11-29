from flask import render_template
from app import app
from app.forms import LoginForm

from santa import test
from santa import users_db_functions as userdb
from santa import auth
from santa import xmaslist

#main landing page
@app.route("/")
def index():
    user = {'username': test.test()}

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
		d_remember_me = form.remember_me.data
		
		flash('Login requested for user {}, remember_me={}'.format(
		    d_username, d_remember_me))
        return redirect('/index')

    return render_template('login.html', title='Sign In', form=form)


#if run from cmd line, run flask with external host
if __name__ == "__main__":
    print("poop")
    app.run(debug=True, host='0.0.0.0')
