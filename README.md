# cunning-xmas-list

Web application to create a secret santa list for the 
cunning family christmas gift exchange.

Uses a python backend and flask for the frontend.

Author: Christos Cunning


# Testing the Flask Server
The flask server can run locally using the following command:

FLASK_APP="app.py" flask run --host=0.0.0.0

#Deployment
run the following commands in ~/cunning-xmas-site/
-activate venv
	source flask/bin/activate
-start uwsgi server on tcp port 3033
-specify main py file for site and main module name
	uwsgi --socket 0.0.0.0:3033 -w santasite:app
	
	
nginx should run by default or just run
	sudo service nginx restart
to ensure changes take effect