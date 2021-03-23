#!/usr/bin/python

import csv
import hashlib
import os
<<<<<<< HEAD
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


def main():
    excludeDir = ['/dev', '/proc', '/run', 'sys', '/tmp', '/var/lib', '/var/run']


    return


if __name__ == "__main__":
    main()
=======

def main():
  ...
  
def hash():
  ...
  
def csv_parser(list):
    csv_file = open("/tmp/hash.csv","a+")
    filename = list[0]
    filepath = list[1]
    hash = list[2]
    date = list[3]
    csv_line = filename + ',' + filepath + ',' + hash + ',' + date
    csv_file.write(csv_line)
    csv_file.close()
>>>>>>> d28f487720520ac534bed8d824be801a6fe2e07e
