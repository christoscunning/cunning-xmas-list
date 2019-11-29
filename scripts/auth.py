# Preforms authentication for logining in and out of user accounts.
# Uses 
#
# Author: Christos Cunning
#
# Version: 0.2
# Last Updated: 2019-11-28
#
# Notes:
#	- do not have to specifty user_id when adding a user to the database
#

import hashlib,binascii,os


#takes the plain text password as input and returns the hashed version
def hash_password(password):
	#find salt and hash
	salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
	password_hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
	
	password_hash = binascii.hexlify(password_hash)
	return (salt+password_hash).decode('ascii')
	
#checks the provided password agaisnt the stored password hash.
# stored password is the salt + hashed password, provided password is the 
# plain text provided password

# returns true if same, false if not
def verify_password(stored_password, provided_password):
	salt = stored_password[:64] #first 64
	stored_password = stored_password[64:] # last 64 (this might be backwards??)
	password_hash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
	password_hash = binascii.hexlify(password_hash).decode('ascii')
	
	return password_hash == stored_password