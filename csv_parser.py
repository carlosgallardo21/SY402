import csv


def main():
  list = ["filename","/tmp/","hash_here","datetime"]
  csv_parser(list)


def csv_parser(list):
  with open("hash.csv", 'a+') as csv_file:
    csvwriter = csv.writer(csv_file)
    csvwriter.writerow(list)
    csv_file.close()
    return
    
main()
