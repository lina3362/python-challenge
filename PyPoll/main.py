# open csv file
import os
import csv
path = os.path.join("..","Resources","election_data.csv")
with open(path) as file:
    csvreader = csv.reader(file, delimiter=",")
    print(csvreader)
    csv_header = next(csvreader)
    for row in csvreader:
        print(row)
        
