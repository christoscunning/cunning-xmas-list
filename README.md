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

#This is the simulation branch
simply run simulate_xmas.py or whatever it is from the commandline
and it will randomize lists until in finds one with the least errors
