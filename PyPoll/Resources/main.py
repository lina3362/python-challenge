# open csv file
import os
import csv
path = os.path.join("..","Resources","election_data.csv")
with open(path) as file:
    csvreader = csv.reader(file, delimiter=",")
    csvheader = next(csvreader)
# The total number of votes cast
    row_count = sum(1 for row in file)
# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.
    
print("Election Results")
print("-----------------------")
print("Total Votes:", row_count)
print("-----------------------")

