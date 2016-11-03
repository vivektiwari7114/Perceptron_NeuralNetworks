#Basic Program needs
import sys
import os
from collections import defaultdict

def makeModelDict(file):
    tempDict = defaultdict(int)
    fileContent = open(file, "r", encoding="latin1").read().strip()
    queryContent = fileContent.split('\n')
    for item in queryContent:
        itemsList = item.split()
        tempDict[itemsList[0]] = float(itemsList[1])
    return tempDict

def readFilesToBeClassified(rootDir):
    fileNameDict = defaultdict(defaultdict)
    for root, dirs, files in os.walk(rootDir):
        for name in files:
            if name.endswith((".txt")):
                nameOfFiles = os.path.join(root, name)
                fileNameDict[nameOfFiles] = getTheContentOfTheIndividualFile(nameOfFiles)
    return fileNameDict

def getTheContentOfTheIndividualFile(nameOfFile):
    contentOfFileDict= defaultdict(int)
    fileContent = open(nameOfFile, "r", encoding="latin1").read()
    listOfWords = fileContent.split()
    for words in listOfWords:
        contentOfFileDict[words]+= 1
    return contentOfFileDict

def fileWrite(label, fileName):
    outputString = label +" "+ fileName+ "\n"
    outputHandle.write(outputString)

#Main Exection of classifier
modelDict = defaultdict(int)
readModelFile = "per_model.txt"
modelDict = makeModelDict(readModelFile)
bias = modelDict["bias"]
del modelDict['bias']

#Algorithm to classify New files using perceptron model
inputDirectory = sys.argv[1]
outputFile = sys.argv[2]
outputHandle = open(outputFile, "w", encoding="latin1")

readFileDict = readFilesToBeClassified(inputDirectory)

'''
totalSpamCount = 0
totalHamCount = 0
predictedSpam  = 0
predictedHam = 0
expectedSpam =0
expectedHam =0
'''

for k,v in readFileDict.items():
    '''
    getFileType = k.split('/')
    typeOfFile = getFileType[len(getFileType) - 2].lower()
    if (typeOfFile == "spam"):
        totalSpamCount = totalSpamCount + 1
    else:
        totalHamCount =  totalHamCount + 1
    '''


    alpha =0
    for ks, vs in v.items():
        if ks in modelDict:
            alpha = alpha + (vs * modelDict[ks])
    alpha = alpha + bias
    if alpha > 0:
        label = "spam"
        #predictedSpam = predictedSpam + 1;
    else:
        label = "ham"
        #predictedHam = predictedHam + 1;
    '''
    if(label == "spam" and  typeOfFile == "spam"):
        expectedSpam = expectedSpam + 1
    if (label == "ham" and typeOfFile == "ham"):
        expectedHam = expectedHam + 1

    '''
    fileWrite(label, k,)

'''
#Calculating Recall, Precison, F1
#Check for divide by zero error in case dev data donot contain spam/ham directory both
if (predictedSpam != 0 and predictedHam != 0 and totalSpamCount != 0 and totalHamCount !=0 ):
    precisionForSpam =  expectedSpam/predictedSpam
    precisionForHam =   expectedHam/ predictedHam

    recallForSpam = expectedSpam/totalSpamCount
    recallForHam =  expectedHam/ totalHamCount

    fscoreForSpam = (2 * precisionForSpam * recallForSpam)/(precisionForSpam +  recallForSpam)
    fscoreForHam =  (2 * precisionForHam * recallForHam)/(precisionForHam +  recallForHam)

    print("HAM")
    print("Precision ",precisionForHam)
    print( "Recall ",recallForHam)
    print( "F-Score ",fscoreForHam)
    print("SPAM")
    print( "Precison",precisionForSpam)
    print("Recall", recallForSpam)
    print("F-Score",fscoreForSpam)
'''

