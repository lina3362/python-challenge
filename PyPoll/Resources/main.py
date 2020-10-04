# open csv file
import os
import csv
path = os.path.join("..","Resources","election_data.csv")
with open(path) as file:
    csvreader = csv.reader(file, delimiter=",")
    row_count = sum(1 for row in file)
    row1_count = sum(3 for row in file): row1_count=="Khan"
print("Election Results")
print("-----------------------")
print("Total Votes:", row_count)
print("-----------------------")
print("Khan:",row1_count)
