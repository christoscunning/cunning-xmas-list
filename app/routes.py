from flask import render_template
from app import app

from santa import test

#main landing page
@app.route("/")
def index():
    user = {'username': test.test()}

    slist = {
	"Chris": "Dim",
        "Dim": "Yan",
        "Yan": "Chris"
    }
    return render_template('index.html', title='Home', user=user, slist = slist)

#login page
@app.route("/login")
def login():
    return "login page"


#if run from cmd line, run flask with external host
if __name__ == "__main__":
    print("poop")
    app.run(debug=True, host='0.0.0.0')
