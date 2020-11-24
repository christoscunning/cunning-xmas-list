# Functions to access and manipulate the database that
# have to do with xmas santa algorithm
#
# Author: Christos Cunning
#
# Version: 0.1
# Last Updated: 2019-11-28
#
# Notes:

import csv
import sqlite3 as sql
from . import users_db_functions as userdbf
DB_NAME = 'users.db'

# returns a list of the names of all the users
# in the database seperated by family.
# returns a list of list of strings
def getNames():
	conn = sql.connect(DB_NAME)
	cursor = conn.cursor()
	
	#create empty list of lists
	names = [[],[],[],[],[]]
	
	for row in cursor.execute("SELECT username, family_id FROM users"):
		listPos = row[1] - 1 #the family id is btwn [1,5], but lists start at 0
		names[listPos].append(row[0])
	
	
	#commit and close conneciton
	conn.commit()
	conn.close()
	
	return names
	
#loads names and family_id data from and csv file
def loadNamesFromCSV(filename):
	with open(filename) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			if line_count == 0:
				print("first row.......")
				line_count += 1
			else:
				#get name and family_id
				name = row[0]
				family_id = row[1]
				#add new user to database with default password
				userdbf.addNewUser(name,family_id,"password")
				#increment line count
				line_count += 1
		print("Processed ", line_count, " lines")
		
		
		
