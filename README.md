# cunning-xmas-list

Web application to create a secret santa list for the 
cunning family christmas gift exchange.

Uses a python backend and flask for the frontend.

Author: Christos Cunning


# Testing the Flask Server
The flask server can run locally using the following command:

FLASK_APP="app.py" flask run --host=0.0.0.0


# Uses
Checkout branches simulate and deployment for the two current uses of the xmas-list program.
 - simulate branch is for the xmas-list program repeatedly to find the optimal secret-santa list.
 - deployment branch is for serving the website over the internet using uwsgi and nginx as a reverse proxy.
