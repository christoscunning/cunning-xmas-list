# Contains various functions for use with the users database
#
# Author: Christos Cunning
#
# Version: 0.1 (alpha)
# Last Updated: 2019-11-28
#
# Notes:
#	Usernames: FirstnameLastname (no space) *unique
#   passwords: hashed in auth.py
#	family_id is 1,2,3,4,5 depending on what family they are in

import sqlite3 as sql
import create_user_db as createdb
import auth
DB_NAME = 'users.db'


# prints the username and family_id of every user in the database
def printDB():
	conn = sql.connect(DB_NAME)
	cursor = conn.cursor()
	
	for row in cursor.execute("SELECT username, family_id, pw_hash FROM users"):
		print("username = ", row[0], "family_id = %d", row[1], "pw_hash = ", row[2])
	
	#commit and close connection
	conn.commit()
	conn.close()

#adds a new user with the specifed username and family ID
def addNewUser(newUserame,familyID,newPassword):
	conn = sql.connect(DB_NAME)
	cursor = conn.cursor()
	
	pwHash = auth.hash_password(newPassword)
	
	# add new row to the table for the new user
	cursor.execute("INSERT INTO users (pw_hash, username, family_id) VALUES (?, ?, ?)",
					(pwHash, newUserame, familyID))
	
	#commit and close
	conn.commit()
	conn.close()

#updates a user record in the database
def updateNameByUserID(newUserame, userID):
	conn = sql.connect(DB_NAME)
	cursor = conn.cursor()

	conn.execute("UPDATE users SET username = ? WHERE user_id = ?", (newUserame, userID))
	
	conn.commit()
	conn.close()

#finds a user by username
# returns a list of the info of the user
# row[0] is the user_id, row[1] is hashed_password, row[2] is the username, row[3] is the family_id
def findUserByUsername(s_username):
	conn = sql.connect(DB_NAME)
	cursor = conn.cursor()
	
	#conn.execute("SELECT user_id, username, family_id FROM users WHERE username = ?", (s_username,) )
	#row = cursor.fetchone()[0]
	returnRow = []
	
	for row in cursor.execute("SELECT user_id, pw_hash, username, family_id FROM users WHERE username = ?", (s_username,)):
		returnRow = row
	
	
	conn.commit()
	conn.close()
	
	if returnRow == []:
		print("Error: User does not exist")
		return 1
	else:
		return returnRow

#verify a user password
# p_ = provided 
def verifyUserPassword(p_username,p_password):
	#find user
	user = findUserByUsername(p_username)
	#if user does not exist then return false right away
	if user == 1:
		return false
	
	storedPassword = user[1]
	
	result = auth.verify_password(storedPassword, p_password)
	
	return result
	
#deletes a user by username
def deleteUserByUsername(p_username):
	conn = sql.connect(DB_NAME)
	cursor = conn.cursor()
	
	cursor.execute("DELETE FROM users WHERE username = ?", (p_username,))
	
	conn.commit()
	conn.close()

def deleteAllUsers():
	conn = sql.connect(DB_NAME)
	cursor = conn.cursor()
	
	cursor.execute("DELETE FROM users")
	
	conn.commit()
	conn.close()



### TESTING ###
#deleteAllUsers()
#printDB()

#print(verifyUserPassword("Coral2","coralreef"))

#name = "Coral2"
#row = findUserByUsername(name)
#print("user= ",row)

#addNewUser("PerryRink", 1, "coralsreef")
#updateNameByUserID("Coral2", 1)

#printDB()


