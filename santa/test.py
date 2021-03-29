# need to update these import statements for py3
# need to state the relative directory (in this case, it is this dir)
from . import xmaslist as xl
from . import users_db_functions as userdb
from . import santa_db_functions as santadb
from . import create_user_db as createdb

#full path
filename = '/home/pi/cunning-xmas-site/santa/names.txt'

#userdb.deleteAllUsers()

#createdb.createDatabase()
#santadb.loadNamesFromCSV(filename)
#userdb.printDB()
#shuffle = xl.xmasShuffle(46)
#shuffle.printList()
print("test success!")
"""
dict = shuffle.toDictionary()

for x, y in dict.items():
	print(x,y)
"""

def test():
    return "test good"
