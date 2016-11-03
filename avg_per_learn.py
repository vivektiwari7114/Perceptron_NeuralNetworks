#Basic Program needs
import sys
import os
import random
from collections import defaultdict

modelDict = defaultdict(int)
averageModelDict = defaultdict(int)
#Function to get recursively search the directory
def storeTheEntireContent(rootDir):
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
        if words not in modelDict:
            modelDict[words] = 0;
            averageModelDict[words] = 0
    return contentOfFileDict;

def getYValue(absPath):
    pathName = absPath.split("/")
    lastFile = pathName[len(pathName) - 2].lower()
    if lastFile == "spam":
        return 1
    else:
        return -1

def fileWrite(modelDict,outputHandle):
    for k,v in modelDict.items():
        contentToSave = str(k) + " " + str(v) + "\n"
        outputHandle.write(contentToSave)

#Main Progra Execution
sourceRootDirectory = sys.argv[1]
mainFileNameDict = storeTheEntireContent(sourceRootDirectory)
maxIter = 30
bias = 0
beta = 0
count = 1

#Perceptron Training Algorithm
for i in range(0,maxIter):
    for k, v in sorted(mainFileNameDict.items(), key=lambda x: random.random()):
        y = getYValue(k)
        alpha = 0
        for ks,vs in v.items():
            alpha = alpha + (modelDict[ks]  * vs )
        alpha = alpha + bias
        if (y * alpha) <= 0:
            for ks, vs in v.items():
                modelDict[ks] = modelDict[ks] + (vs * y)
                averageModelDict[ks] = averageModelDict[ks] + (vs * y * count)
            bias = bias + y
            beta = beta + (y*count)
        count = count +1

#File write to to per_model.txt
outPutFile = "per_model.txt"
outputHandle = open(outPutFile, "w", encoding="latin1")
for k,v in averageModelDict.items():
    averageModelDict[k] =modelDict.get(k) - ( (1/count) * v )
beta = bias - ( (1/count) * beta )


sendBias = "bias" + " " + str(beta) + "\n"
outputHandle.write(sendBias)
fileWrite(averageModelDict,outputHandle)

