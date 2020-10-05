# open csv file
import os
import csv
path = os.path.join("..","Resources","budget_data.csv")
#variables
month_count = 0
totalrev = 0
differences = 0
averagechange = 0
Highest_profit = 0
Lowest_profit = 0
# read the csv file
with open(path) as file:
    csvreader = csv.reader(file, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
  # The total number of months included in the dataset
      month_count += 1
  # The net total amount of "Profit/Losses" over the entire period
      totalrev += int(row[1])
  # The average of the changes in "Profit/Losses" over the entire period
  # The greatest increase in profits (date and amount) over the entire period

  # The greatest decrease in losses (date and amount) over the entire period

print("Financial Analysis")
print("-----------------------")
print("Total Months:", month_count)
print("Total:", totalrev)



  