import csv


def main():
  list = ["filename","/tmp/","hash_here","datetime"]
  csv_parser(list)

def csv_parser(list):
    csv_file = open("hash.csv","wa+")
    filepath = list[0]
    hashstring = list[1]
    date = list[2]
    csv_line = filepath + ',' + hashstring + ',' + date
    csv_file.write(csv_line)
    csv_file.close()

main()
