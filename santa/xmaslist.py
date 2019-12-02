# Python program to automate the selection of the Cunning
# family Christmas list.
#
# Author: Christos Cunning
#
# Version: 0.5 (alpha)
# Last Updated: 2019-11-26
#
# Notes:
# - Based on the extended families of the five children of Clive Leonard Cunning.
# - should we count cousins with kids as seperate families for overlap purposes?


import copy
import random
import santa_db_functions as santadb

### CLASSES ###

#Person Class
# init parameters:
#	name: the persons first name
# 	family: the family they are from (cunning1,2,3,4 or 5 from the list above)
#	difficulty: How difficult it is to buy for the person (out of 10)
#	
#	giving: gift giving ability? (TODO : add this?)
class Person:
	# constructor
	def __init__(self, name, family, difficulty):
		self.name = name
		self.family = family
		self.difficulty = difficulty
	
	# example function
	def getDiff(self):
		return self.difficulty
		
# Santa class
# represents a person in the secret santa
# iden: in the identity of the person, (a Person object)
# givingTo: the recipeint of the gift (a Santa Object)

# for linked list
# next
# next and # givingTo should be the same
class Santa:
	# constructor
	def __init__(self, iden, givingTo, next):
		self.iden = iden
		self.givingTo = givingTo
		self.next = None ##
	
	def getIden(self):
		return self.iden
		
	def getGivingTo(self):
		return self.givingTo
		
	#deprecated
	def setGivingTo(self,newGivingTo):
		self.givingTo = newGivingTo
		self.next = newGivingTo
		
	# check if match is compatibal based on family
	def sameFamily(self):
		if self.iden.family is None or self.givingTo is None:
			return "Cannont compare if iden or givingTo is None"
		elif self.iden.family == self.givingTo.family:
			return True
		else:
			return False
	
# SantaList class
# this class is a linkedlist of santas that are buying for each other
class SantaList:
	def __init__(self):
		self.head = None
		self.start = None
		self.count = 0
	
	def addSanta(self,newSanta):
		if self.start == None:
			self.head = newSanta
			self.start = newSanta
			self.count = 1
		else:
			self.head.givingTo = newSanta
			self.head.next = newSanta
			self.head = newSanta
			if newSanta != self.start:
				self.count += 1
	
	def printList(self):
		node = self.start
		while node is not None:
			print(node.iden.name)
			node = node.next
			if node == self.start:
				node = None
				
	#returns the list as a dictionary
	def toDictionary(self):
		xmasDict = {}
		node = self.start
		while node is not None:
			xmasDict[node.iden.name] = node.givingTo.iden.name
			node = node.next
			if node == self.start:
				node = None
		return xmasDict
	
	def getSize(self):
		return self.count



#function wrapper for all the code that was in this file so we can return the masterlist
#loads all users from database, then returns a smart shuffled list.
def xmasShuffle(seed = 0):
	random.seed(seed)
	
	
	#get names from database
	DB_NAMES_LIST = santadb.getNames()

	#get rows of database
	cunningNames1 = DB_NAMES_LIST[0]
	cunningNames2 = DB_NAMES_LIST[1]
	cunningNames3 = DB_NAMES_LIST[2]
	cunningNames4 = DB_NAMES_LIST[3]
	cunningNames5 = DB_NAMES_LIST[4]
	totalNumPeople = len(cunningNames1) + len(cunningNames2) + len(cunningNames3) + len(cunningNames4) + len(cunningNames5)
	#print("total num with db names", totalNumPeople)

	'''
	#####Preset Names
	
	cunningNames1 = ["Coral","Perry","Keegan","Shawna","Kohen","Farley","Sasha","Joey","Keiran","Stephanie","Keanna","Marianne"]
	cunningNames2 = ["Diann","Hugh","Sean","Tessa","Rylan","Camilla","Mike","Lucas","Callum","Jess"]
	cunningNames3 = ["Len"]
	cunningNames4 = ["Sylvia","Craig"]
	cunningNames5 = ["Efrosini","John","Dimitri","Christos","Yiannis"]
	totalNumPeople = len(cunningNames1) + len(cunningNames2) + len(cunningNames3) + len(cunningNames4) + len(cunningNames5)
	#print(totalNumPeople)
	'''
	
	#Main

	#num families!!
	num_fams = 5

	#manual
	# create lists
	cunning1 = []
	cunning2 = []
	cunning3 = []
	cunning4 = []
	cunning5 = []

	# Fill lists with Santas that only have the santa identity and not the recipeint yet.
	# TODO: custom difficulty
	for name in cunningNames1[:]:
		newPerson = Person(name,1,5)
		newSanta = Santa(newPerson, None,None)
		cunning1.append(newSanta)

	for name in cunningNames2[:]:
		newPerson = Person(name,2,5)
		newSanta = Santa(newPerson, None,None)
		cunning2.append(newSanta)
		
	for name in cunningNames3[:]:
		newPerson = Person(name,3,5)
		newSanta = Santa(newPerson, None, None)
		cunning3.append(newSanta)

	for name in cunningNames4[:]:
		newPerson = Person(name,4,5)
		newSanta = Santa(newPerson, None, None)
		cunning4.append(newSanta)

	for name in cunningNames5[:]:
		newPerson = Person(name,5,5)
		newSanta = Santa(newPerson, None, None)
		cunning5.append(newSanta)

	cunningLists = [cunning1[:],cunning2[:],cunning3[:],cunning4[:],cunning5[:]]
	
	# create linked list for santa 
	MasterList = SantaList()

	#get rand family
	randFamily = random.randint(0,(len(cunningLists) - 1))
	randFamily2 = randFamily
	while randFamily2 == randFamily:
		randFamily2 = random.randint(0,(len(cunningLists) - 1))
	
	# we set random person to 0 by default, and if the family has more than
	# one person left, it will asign it a random number
	randPerson = 0
	if len(cunningLists[randFamily]) > 1:
		randPerson = random.randint(0,len(cunningLists[randFamily])-1)
	
	#now create first santa
	firstSanta = cunningLists[randFamily][randPerson]
	#this does next
	MasterList.addSanta(firstSanta)
	currentSanta = cunningLists[randFamily][randPerson]

	#just .remove() them instead???
	removeOneName = cunningLists[randFamily][randPerson]
	#print("important", cunningLists[2])
	cunningLists[randFamily].remove(removeOneName)

	#forgot i need this here too
	#if list is empty, delete it
	if len(cunningLists[randFamily]) == 0:
		#print("note if in here",randFamily)
		cunningLists.remove(cunningLists[randFamily])
		'''
		newCunningLists = []
		for i in range(0,(len(cunningLists) - 1)):
			if cunningLists[randFamily] != []:
				newCunningLists.append(cunningLists[randFamily])
		cunningLists = newCunningLists
		'''

	while (MasterList.getSize() < totalNumPeople):
		
		#if onyl one left, we break loop
		if len(cunningLists) < 2:
			#print("here")
			break
		
		
		#get new rand family but cant be same as current
		currentFamily = currentSanta.iden.family - 1
		newFamily = currentFamily
		
		
		# go until we find a family that is different and not empty
		while (newFamily == currentFamily) or (cunningLists[newFamily] == None):
			newFamily = random.randint(0,(len(cunningLists) - 1))
		
		newPersonIndex = 0
		# if list has more than one, than randomize
		if len(cunningLists[newFamily]) > 1:
			#get index, get new person
			newPersonIndex = random.randint(0,len(cunningLists[newFamily])-1)
		
		#print(newFamily, " : ", newPersonIndex)
		#print(cunningLists[newFamily][newPersonIndex])
		
		count = 0
		for list in cunningLists:
			count += 1
			#print(count) 
			for name in list:
				#print(name.iden.name)
				nothing = 3
		
		#print(newFamily, " : ", newPersonIndex, "!!!")
		#print(cunningLists[newFamily])
		newPerson = cunningLists[newFamily][newPersonIndex].iden #.iden is the person of santa
		
		
		#now create new santa
		newIden = copy.deepcopy(cunningLists[newFamily][newPersonIndex].iden)
		newSanta = Santa(newIden,None,None)
		# add to list
		MasterList.addSanta(newSanta)
		#update current Santa
		currentSanta = cunningLists[newFamily][newPersonIndex]
		
		
		removePerson = cunningLists[newFamily][newPersonIndex]
		cunningLists[newFamily].remove(removePerson)
		
		
		#if list is empty, delete it
		if not cunningLists[newFamily]:
			#print("note if in here",newFamily)
			cunningLists.remove(cunningLists[newFamily])
			'''
			newCunningLists = []
			for i in range(0,(len(cunningLists) - 1)):
				if cunningLists[newFamily] != []:
					newCunningLists.append(cunningLists[newFamily])
			cunningLists = newCunningLists.deepcopy()
			'''
		
		
		"""
		for list in cunningLists:
			print(list)
		
		#check if cunningList is totally empty, if so make null
		empty = True #assume empty
		for santa in cunningLists[newFamily][:]:
			if santa.iden.name != "null":
				empty = False
		"""
		
		
		
	#end while loop

	#after we complete the master list
	#add whoever is left

	lastSanta = Santa(None,None,None)

	for santaList in cunningLists[:]:
		if santaList != None:		
			for santa in santaList[:]:
				MasterList.addSanta(santa)
				lastSanta = santa
				#remove from original list once taken
				santaList.remove(santa)

	#add the first santa again as the last santa to finish the loop
	MasterList.addSanta(firstSanta)
	
	return MasterList
	#### END OF FUNCTION #####



# end of file, old testing code below

#MasterList.printList()
#print("count= ", MasterList.getSize())
#print(MasterList.start.iden.name)
#print(MasterList.start.next.iden.name)




















