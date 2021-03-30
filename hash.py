#!/usr/bin/python

import csv
import hashlib
import os
import datetime
import difflib


'''1. Hash files baseline
    If hash file does not exist make the hash file
2. If baseline exists, then we hash check all the files and then print out the difference
'''
'''FILE FORMAT'''
'''filename, fullpath, hash, datetime'''

'''Breakdown'''

def baseline():

    return

# Take initial hash file and compare to the new file
def compHashFiles(initFile, recFile):
    fd1 = open(initFile, 'r')
    fd2 = open(recFile, 'r')

    # Find difference
    for line in difflib.unified_diff(fd1.read(), fd2.read(), fromfile='initFile', tofile='recFile', lineterm=''):
        print(line)
    
    return

def csv_parser(list):
    csv_file = open("hash.csv","a+")
    filepath = list[0]
    date = list[1]
    hashstring = list[2]
    
    csv_line = filepath + ',' + hashstring + ',' + date
    csv_file.write(csv_line)
    csv_file.close()
    return

def main():
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


if __name__ == "__main__":
    main()