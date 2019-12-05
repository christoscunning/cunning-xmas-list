# cunning-xmas-list

Web application to create a secret santa list for the 
cunning family christmas gift exchange.

Uses a python backend and flask for the frontend.

Author: Christos Cunning


# Testing the Flask Server
The flask server can run locally using the following command:

FLASK_APP="app.py" flask run --host=0.0.0.0

# Deployment
run the following commands in ~/cunning-xmas-site/
 - activate venv
 source flask/bin/activate
 - start uwsgi server on tcp port 3033
 - specify main py file for site and main module name
uwsgi --socket 0.0.0.0:3033 -w santasite:app
	
	
nginx should run by default or just run
	sudo service nginx restart
to ensure changes take effect

TO start in a screen session:
ssh into your remote box. type screen Then start the process you want.
Press Ctrl-A then Ctrl-D. This will detach your screen session but leave your processes running. You can now log out of the remote box.
If you want to come back later, log on again and type screen -r This will resume your screen session, and you can see the output of your process.
