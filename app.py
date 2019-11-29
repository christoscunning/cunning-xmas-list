from flask import Flask
from flask import render_template

app = Flask(__name__)

#main landing page
@app.route("/")
def index():
	user = {'username': 'Christos'}
	
	slist = {
		"Christos": "Dimitri",
		"Dimitri": "Yiannis",
		"Yiannis": "Christos"
	}
	
	return render_template('index.html', title='Home', user=user, slist = slist)


#login page
@app.route("/login")
def login():
	return "login page"


# if run from command line, run flask with external host
if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')

