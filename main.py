import hashlib
import os


def calculateHash(filePath):
    with open(filePath, "rb") as file:
        bytes = file.read()
        readableHash = hashlib.sha256(bytes).hexdigest()
    return readableHash


def scanFiles(directory):
    fileDict = {}
    for (
        foldername,
        subfolders,
        filenames,
    ) in os.walk(directory):
        for filename in filenames:
            filePath = os.path.join(foldername, filename)
            fileHash = calculateHash(filePath)
            if fileHash in fileDict:
                fileDict[fileHash].append(filePath)
            else:
                fileDict[fileHash] = [filePath]
    return fileDict


def deleteDuplicates(fileDict):
    for key in fileDict:
        fileList = fileDict[key]
        while len(fileList) > 1:
            itemToDelete = fileList.pop()
            os.remove(itemToDelete)


fileDict = scanFiles("diretoryToCheckPlaceholder")
deleteDuplicates(fileDict)
