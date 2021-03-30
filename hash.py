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


def csv_parser(list):
    fileOpen = "hash0.csv"
    if path.exists(fileOpen) is True:
        fileOpen = "hash1.csv"
  
    with open(fileOpen, 'a+') as csv_file:
        csvwriter = csv.writer(csv_file)
        csvwriter.writerow(list)
        csv_file.close()
    return


def hashFunction():
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
            csv_parser(hashList)
    return


def baseline():
    hashFunction()
    return


# Take initial hash file and compare to the new file
def compHashFiles():
    initFile = "hash0.csv"
    recFile = "hash1.csv"
    ...
    return



def main():
    if path.exists("hash0.csv") is True:
        hashFunction()
        compHashFiles()
    else:
        print("HELLO")
        baseline()
                    
    return


if __name__ == "__main__":
    main()