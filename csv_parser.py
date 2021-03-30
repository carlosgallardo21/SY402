import csv


def main():
  list = ["filename","/tmp/","hash_here","datetime"]
  csv_parser(list)

def csv_parser(list):
    csv_file = open("hash.csv","wa+")
    filename = list[0]
    filepath = list[1]
    hash = list[2]
    date = list[3]
    csv_line = filename + ',' + filepath + ',' + hash + ',' + date
    csv_file.write(csv_line)
    csv_file.close()

main()
