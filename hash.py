#!/usr/bin/python

import csv
import hashlib
import os

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
