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
    fileOpen = "/tmp/hash0.csv"
    if path.exists(fileOpen) is True:
        fileOpen = "/tmp/hash1.csv"
    csv_file = open(fileOpen,"a+")
    filepath = list[0]
    date = list[1]
    hashstring = list[2]
    
    csv_line = filepath + ',' + date + ',' + hashstring
    csv_file.write(csv_line)
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
def compHashFiles(initFile, recFile):
    initFile = "/tmp/hash0.csv"
    recFile = "/tmp/hash1.csv"
    fd1 = open(initFile, 'r')
    fd2 = open(recFile, 'r')

    # Find difference
    for line in difflib.unified_diff(fd1.read(), fd2.read(), fromfile='initFile', tofile='recFile', lineterm=''):
        print(line)
    
    return



def main():
    if path.exists("/tmp/hash0.csv") is True:
        hashFunction()
        compHashFiles()
    else:
        baseline()
                    
    return


if __name__ == "__main__":
    main()