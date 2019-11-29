# Creates the SQLite database and table for the website users.
#
# Author: Christos Cunning
#
# Version: 0.2
# Last Updated: 2019-11-28
#
# Notes:
#	- do not have to specifty user_id when adding a user to the database
#

import sqlite3

#function to create user database
# does nothing if it already exists

def createDatabase():
	#make connection
	conn = sqlite3.connect("users.db")

	#create cursor
	cursor = conn.cursor()

	print("Connected to database succesfully.")

	cursor.execute("""CREATE TABLE IF NOT EXISTS users (
					user_id      INTEGER     PRIMARY KEY AUTOINCREMENT NOT NULL,
					pw_hash		 TEXT   	 NOT NULL,
					username     TEXT        UNIQUE NOT NULL,
					family_id    INTEGER     NOT NULL
					)""")
					
					
	print("Succesfully created table.")

	cursor.close()
