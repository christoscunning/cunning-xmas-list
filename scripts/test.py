import xmaslist as xl
import users_db_functions as userdb
import santa_db_functions as santadb
import create_user_db as createdb

createdb.createDatabase()
santadb.loadNamesFromCSV("names.txt")
userdb.printDB()
#shuffle = xl.xmasShuffle(3)
#shuffle.printList()
print("test success!")
"""
dict = shuffle.toDictionary()

for x, y in dict.items():
	print(x,y)
"""
