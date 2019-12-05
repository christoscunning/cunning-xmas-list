# cunning-xmas-list

Web application to create a secret santa list for the 
cunning family christmas gift exchange.

Uses a python backend and flask for the frontend.
Hosted on my raspberry pi using nginx as a reverse proxy to a uwsgi web server.
url: home.christoscunning.com
(may be down if my pi is off)

Author: Christos Cunning

Criteria for Cunning Gift Exchange:
 - Person cannot buy for someone in the same family as themselves
 - Person cannot buy for the same person as last year

Todo:
 - better UI to view the santa assignments
 - Implement a wishlist for each user that can be viewed somewhere 
 - registration system


# Testing the Flask Server
The flask server can run locally using the following command:

FLASK_APP="app.py" flask run --host=0.0.0.0

make sure to enable to virtual enviroment first using

# Uses
Checkout branches simulate and deployment for the two current uses of the xmas-list program.
 - simulate branch is for the xmas-list program repeatedly to find the optimal secret-santa list.
 - deployment branch is for serving the website over the internet using uwsgi and nginx as a reverse proxy.
