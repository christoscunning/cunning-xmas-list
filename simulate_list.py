import copy

from santa import test
from santa import users_db_functions as userdb
#from santa import auth
from santa import santa_db_functions as santadb
from santa import xmaslist as xl
from santa import create_user_db as createdb

#full path
#filename = '/home/pi/cunning-xmas-site/santa/names.txt'
filename = './santa/names.txt'

#delete old database
#userdb.deleteAllUsers()

#createdb.createDatabase()
#print("loading database from: " + filename + "...")
#santadb.loadNamesFromCSV(filename)
#print("printing database...")
#userdb.printDB()

num_sims = 50

print("Beginning sims. Running " + str(num_sims) + "  simulations...")

numErrors = 0
errorCountList = []

#save best
bestErrorCount = -1 #first time we set it instead of comparing!!!
bestShuffle = {}
bestSeed = -1
## need to get last years assignments
lastYear = {}
lastYear["Coral"] = "Efrosini"
lastYear["Perry"] = "Dimitri"
lastYear["Keegan"] = "Yiannis"
lastYear["Shawna"] = "Craig"
lastYear["Kohen"] = "Christos"
lastYear["Farley"] = "Sean"
lastYear["Sasha"] = "Jess"
lastYear["Joey"] = "Camilla"
lastYear["Keiran"] = "Mike"
lastYear["Stephanie"] = "Callum"
lastYear["Keanna"] = "Tessa"
lastYear["Marianne"] = "Shawna"
lastYear["Diann"] = "Stephanie"
lastYear["Hugh"] = "Len"
lastYear["Sean"] = "Sasha"
lastYear["Tessa"] = "Keanna"
lastYear["Rylan"] = "Keiran"
lastYear["Camilla"] = "Marianne"
lastYear["Mike"] = "Coral"
lastYear["Lucas"] = "John"
lastYear["Callum"] = "Kohen"
lastYear["Jess"] = "Keegan"
lastYear["Len"] = "Diann"
lastYear["Sylvia"] = "Rylan"
lastYear["Craig"] = "Farley"
lastYear["John"] = "Joey"
lastYear["Efrosini"] = "Lucas"
lastYear["Dimitri"] = "Perry"
lastYear["Christos"] = "Hugh"
lastYear["Yiannis"] = "Sylvia"

''' sample code!!!
shuffle = xl.xmasShuffle(0)
shuffle.printList()
print("test success!")

dict = shuffle.toDictionary()

for x, y in dict.items():
	print(x,y)
'''


'''
shuffle = xl.xmasShuffle(9)
shuffle.printList()

'''

for i in range(0,num_sims):
	numErrors = 0
	shuffle = xl.xmasShuffle(i)
	print(i)
	dict = shuffle.toDictionary()
	#print(i)
	# x -> y
	for x, y in dict.items():
		#dont want to print so much crap
		#print(x,y)
		
		#calculate errors
		
		#test how many are buying for same family
		if userdb.findUserByUsername(x)[3] == userdb.findUserByUsername(y)[3]:
			numErrors += 1
		
		#test how many are buying for same as last years
		if x in lastYear.keys():
			if lastYear[x] == y:
				numErrors += 1
			
		#test something else
	
	#update best error score if its better
	if bestErrorCount == -1:
		bestErrorCount = numErrors
		bestShuffle = dict
		bestSeed = i
	elif numErrors < bestErrorCount:
		bestErrorCount = numErrors
		bestShuffle = copy.deepcopy(dict)
		bestSeed = i
	
	#add error score to list
	errorCountList.append(numErrors)



#print errorCount and errorList at the end
i = 0
for s in errorCountList:
	if i == 0:
		i=1
	else:
		i += 1
	print("test#" + str(i) + " num errors: " + str(s))
	

#print best one
print("\nbest one with " + str(bestSeed) + " seed and num erros:" + str(bestErrorCount) + " errors!")
for x, y in bestShuffle.items():
	print(x + " buying for " + y)