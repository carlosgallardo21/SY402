#!/usr/bin/python

import csv
import hashlib
import os
import datetime
import difflib

from os import path

'''1. Hash files baseline
    If hash file does not exist make the hash file
2. If baseline exists, then we hash check all the files and then print out the difference
'''
'''FILE FORMAT'''
'''filename, fullpath, hash, datetime'''

'''Breakdown'''


def csv_parser(inFlag, list):
    fileOpen = ""
    if inFlag == 0:
        fileOpen = "hash0.csv"
    else:
        fileOpen = "hash1.csv"

    with open(fileOpen, 'a+') as csv_file:
        csvwriter = csv.writer(csv_file)
        csvwriter.writerow(list)
        csv_file.close()
    return


def hashFunction(flag):
    excludeDir = ['/dev', '/proc', '/run', '/sys', '/tmp', '/var/lib', '/var/run']

    for subdir, dirs, files in os.walk(r'/'):
        if subdir in excludeDir:
            dirs[:]=[] # shallow copy, referenced from BeagleD
            files[:]=[] # shallow copy, refernce from BeagleD
            
        for filename in files:
            filepath = subdir + os.sep + filename
            
            hash = hashlib.sha256()
            hash.update(filepath.encode())
            hashStr = hash.hexdigest()
            hashtime = str(datetime.datetime.now())
            
            hashList = [filepath, hashtime, hashStr]
            csv_parser(flag, hashList)
    return


def baseline():
    hashFunction(0)
    return


# Take initial hash file and compare to the new file
def compHashFiles():
    initFile = "hash0.csv"
    recFile = "hash1.csv"

    oldDict = {}
    newDict = {}
    with open(initFile, "r+") as finit:
        for init in finit.readlines():
            oldDict[init[0]] = init[1]
    finit.close()

    with open(initFile, "r+") as frec:
        for rec in frec.readlines():
            newDict[rec[0]] = rec[1]
    frec.close()

    oldFilePaths = oldDict.keys() #list of keys
    newFilePaths = newDict.keys() #list of keys

    updateList = []
    newList = []

    for key in newFilePaths:
        if key not in oldFilePaths:
            newList.append({key,newDict[key]})
        else:
            if oldDict[key] == newDict[key]:
                continue
            else:
                updateList.append({key,newDict[key]})

    if ((len(updateList) and (newList)) == 0):
        print("NO FILE CHANGES")
        return

    print("UPDATED FILES") 
    for upDict in updateList:
        print("{:5} {:5}".format(upDict.keys(), upDict.values()))

    print("-----------------------------------------------------------")
    print("NEW FILES") 
    for newDict in newList:
        print("{:5} {:5}".format(newDict.keys(), newDict.values()))

    return



def main():
    if path.exists("hash0.csv"):
        hashFunction(1)
        compHashFiles()
    else:
        baseline()
        
    return


if __name__ == "__main__":
    main()