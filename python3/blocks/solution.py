import copy
import os
import sys

def initialMatrix():
	''' function to creat and initialize a matrix '''
	### creat defaut matrix of square
	matrix = [['0' for x in range(5)] for x in range(5)]
#	print '--initial matrix:\n', matrix, '\n'
	return matrix

def readBlocks():
	''' function to read blocks which are input files '''
	### length of argv
	argvLen = len(sys.argv)
	#print argvLen
	if argvLen < 8:
		print 'input is less than 7 files, please restart'
		exit()
	### read file names	
	fileNames = []
	for i in range(1, argvLen):
		fileNames.append(sys.argv[i])
		#print fileNames
	### open files
	fileHandlers = []
	for i in range(0, argvLen - 1):
		fileHandlers.append(open(fileNames[i]))	
	#print fileHandlers
	### read blocks
	blocks = []
	for i in range(0, argvLen - 1):
		blocks.append(fileHandlers[i].read(20))
	### treat block c which is an exception
#	print '--blocks\n', blocks, '\n'
	return blocks

def printMatrix(matrix):
	''' function to print Matrix '''
	for i in range(5):
		line =''
		for j in range(5):
			line +=  str(matrix[i][j])
		print line

# function to copy Matrix
def copyMatrix(matrix1, matrix2):
	''' function to copy matrix1 from matrix2'''
	for i in range(5):
		for j in range(5):
			matrix1[i][j] = matrix2[i][j]

def findPosMatrix(matrix, x):
	''' function to find the first position of x in matrix. If non '0' exist, return 25'''
	pos = 0
	for i in range(5):
		for j in range(5):
			if matrix[i][j] == x:
				return pos
			pos = pos + 1
	return pos

def putAChar(matrix, row, column, char):
	''' function to put a char in matrix[row][column]. Return True if succeed, else return False '''
	if matrix[row][column] != '0':
#		print '[putAChar error] matrix[', row, '][', column, '] = ', matrix[row][column]
		return False
	else:
		matrix[row][column] = char
#		print '[putAChar ok]\t  matrix[', row, '][', column,'] = ', matrix[row][column]
		return True

def delAllChar(matrix, char):
	''' function to delete all the char in matrix '''
	for i in range(5):
		for j in range(5):
			if matrix[i][j] == char:
				matrix[i][j] = '0'

def findCharOfBlock(chars):
	''' function to find the char of the block, return the char'''
	for i in range(len(chars)):
		if chars[i] != ' ' and chars[i] != '\n':
			return chars[i]

def delABlock(matrix, blocks, putedList):
	''' function to delete last block putted in matrix '''
	indexLastBlock = putedList[-1]
	del putedList[-1]
 	delAllChar(matrix, findCharOfBlock(blocks[indexLastBlock]))
	return indexLastBlock	


def putABlock(matrix, block):
	''' put a block to the matrix. Return True if suceed, else return False '''
	pos = findPosMatrix(matrix, '0')
	if pos > 25:
		return False
	initialRow = pos / 5
	initialColumn = pos % 5
	row = initialRow
	column = initialColumn
	beginWithSpace = True
	for i in range(len(block) - 1): # deal with the last '\n'
		### to trait the case beginning with space
		if beginWithSpace:
			if block[i] == ' ' and column > 0:
				initialColumn = initialColumn - 1
				column = column - 1		
			else:
				beginWithSpace = False
	
		if block[i] == '\n':
			row = row + 1
			column = initialColumn
			if row > 4:
#				print '[putABlock error] row out of index'
				return False	
		elif block[i] == ' ':
			column = column + 1
			if column > 4:
				if block[i+1] != '\n':
#					print '[putABlock error] column out of index'
					return False
		else:
			if putAChar(matrix, row, column, block[i]) == False:
				return False
			column = column + 1
			if column > 4:
				if block[i+1] != '\n':
#					print '[putABlock error] column out of index'
					return False
#	print '[putABlock] OK for block:', list(block)
#	printMatrix(matrix)
	return True

def clearList(l):
	''' function to clear the list '''
	for i in range(len(l)):
		del l[-1]

def copyList(l1, l2):
	clearList(l1)
	for i in range(len(l2)):
		l1.append(l2[i])

# function to try to put a block
def tryPutABlock(matrix, blocks, putedList, notputList, dic):
	''' function to put a good block in the matrix orderly, if succeed return True, else returns False '''
	for i in range(len(blocks)):
		if i in putedList or i in notputList:
			continue
#		print 'try block: ', list(blocks[i])
#		print 'matrix before trying'
#		printMatrix(matrix)
		### back up matrix in case that putABlock can change the matrix
		backupMatrix = copy.deepcopy(matrix)
		if putABlock(matrix, blocks[i]):
			putedList.append(i)
			### clear notputList when we suceed putABlock
			clearList(notputList)
#			print 'putedList', putedList
#			print 'notputedList :', notputList
#			print 'dict :', dic.items()
			return True
		else:
#			print '[tryPutABlock error]', list(blocks[i]) 
			### recover matrix
			copyMatrix(matrix, backupMatrix)
#			print 'putedList', putedList
#			print 'notputedList :', notputList
	### fail to put a block, putedList is done in the delABlock fuction. indexLastBlock is the postion of last block putted
	indexLastBlock = delABlock(matrix, blocks, putedList)
	### look for the notputList in the dict, dict store respectively the putedList and notputList as key-value paires
	### key of dict must be immutable, so we change the notputList from list to tuple. Also values are list which are 
	### references in dict, that is why I used copyList function
	putedTuple = tuple(putedList)
	if putedTuple in dic:	
		### copy the previous notputList
		copyList(notputList, dic[putedTuple])	
		### add the deleted block	
		notputList.append(indexLastBlock)
	else:
		clearList(notputList)
		notputList.append(indexLastBlock)
	### update dicionary
	tmpNotputList = []
	copyList(tmpNotputList, notputList)
	dic[putedTuple] = tmpNotputList		
#	printMatrix(matrix)
#	print 'putedList ', putedList
#	print 'notputedList :', notputList
#	print 'dict :', dic.items()
	return False

def checkImplementation(matrix):
	''' function to check if succeed  '''
	for i in range(5):
		for j in range(5):
			if matrix[i][j] == '0':
				return False
	return True


def implementation(matrix, blocks):
	'''function of implementing algo. Return True if succeed, else return False'''
	putedList = list()
#	i = 0
	backupMatrix = copy.deepcopy(matrix)
	indexLastBlock = None
	notputList = list()
	dic = dict()
	while not checkImplementation(matrix):
#		print '\n----- i:', i
#		i = i + 1
		tryPutABlock(matrix, blocks, putedList, notputList, dic)
	return True
	
def main():
	matrix = initialMatrix()
	blocks = readBlocks()
	implementation(matrix, blocks)
	printMatrix(matrix)

################################### begin the program ###############################
main()
################################### test ############################################
