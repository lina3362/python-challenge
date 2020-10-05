# open csv file
import os
import csv
path = os.path.join("..","Resources","budget_data.csv")

with open(path) as file:
    csvreader = csv.reader(file, delimiter=",")
  # The total number of months included in the dataset
    row_count = sum(1 for row in file) -1
  # The net total amount of "Profit/Losses" over the entire period
    Total = 0
    totalrev = Total + int(row["Profit/Losses"])
  # The average of the changes in "Profit/Losses" over the entire period

  # The greatest increase in profits (date and amount) over the entire period

  # The greatest decrease in losses (date and amount) over the entire period

print("Financial Analysis")
print("-----------------------")
print("Total Months:", row_count)
print("Total:", totalrev)



  