import os
import hashlib


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
