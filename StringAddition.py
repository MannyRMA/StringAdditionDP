'''
Manuel Rodriguez CPSC 413 Assignment 3 bonus
'''
import sys

# dictionary class, made it easier for me think if you just store values of substrings in a dictionary/hash table
class myDictionary(dict): 
    # __init__ function (constructor)
    def __init__(self): 
        self = dict() 
          
    # function to insert a key with a value
    def insert(self, key, value): 
        self[key] = [value]

    # function to add to a key
    def addToKey(self, key, value):
        lt = self[key]
        self[key] = lt + value

    # funtion to check a key value
    def checkKey(self, key):
        if key in self:
            return self[key]
        else:
            return ""
    
    # function to check if a key is in the dictionary
    def containsKey(self, key):
        return key in self

# Main function
def Main():
    # the possible outputs
    yesOutput = "YES, target symbol can be formed"
    noOutput = "NO, target symbol can NOT be formed"
    # making sure the input format is correct
    if len(sys.argv) != 2:
        print("error: correct input format is: python fileName.py inputFile.in")
        exit()
    # reading from the input file
    inputFile = open(sys.argv[1], 'r')
    alphabetSize = int(inputFile.readline().strip())
    targetSymbol = inputFile.readline().strip()
    # reading/creating the addition table
    additionTable = []
    for i in range(0, alphabetSize):
        row = inputFile.readline()
        additionRow = row.split()
        additionTable.append(additionRow)
    inputString = inputFile.readline().strip()
    n = len(inputString)
    inputFile.close() # gotta make sure to close the file

    # "memoization" dictionary
    memoDict = myDictionary()
    result = StringAddition(inputString, additionTable, memoDict, targetSymbol)
    if result == True:
        print(yesOutput)
    else:
        print(noOutput)
    




# String additon function, performs a slight variation of the algorithm
def StringAddition(opString, table, d, target):
    length = len(opString)
    # base case, when length one the begin index and the end idex of the string are the same, simply insert the string into the dictionary
    if length == 1:
        d.insert(opString, opString)
        return 
    # rest of the cases
    else:
        # for loop that incorporates the midpoint and ensures evey possible combination is tested
        for m in range(length-1):
            leftSubstring = opString[0:m+1]
            rightSubstring = opString[m+1:length]
            # checking if the dictionary contains a key for the left substring, if not then we have to calculate its entry
            if  not d.containsKey(leftSubstring):
                StringAddition(leftSubstring, table, d, target)
            # checking if the dictionary contains a key for the right substring, if not then we have to calculate its entry
            if not d.containsKey(rightSubstring):
                StringAddition(rightSubstring, table, d, target)
            # getting the results on the dictionary from the left substring and right substring
            leftResult = d.checkKey(leftSubstring)
            rightResult = d.checkKey(rightSubstring)
            combinationResult = combinationsOfTwoStrings(leftResult, rightResult, table)
            d.insert(opString, combinationResult)
            containsTarget = target in combinationResult
            if containsTarget:
                return True
        return False

# function that takes two strings and test possible addition based on the table
def combinationsOfTwoStrings(leftString, rightString, table):
    # creating an index string that would be inserted in the dictionary
    indexString = ""
    # for loop to iterate through every "letter" in the left substring
    for letter in leftString:
        # converting that "letter" to the integer
        left = int(letter)
        # nested for loop that iterates through every "character" in the right substring
        for char in rightString:
            # converting that "character" to the integer
            right = int(char)
            # getting the addtion result from the addition table at index ["letter"]["character"]
            resultFromTable = table[left][right]
            # checking if the addition result is already in the indexString (removes redundancy)
            if resultFromTable not in indexString:
                indexString = indexString + resultFromTable
    return indexString



Main()