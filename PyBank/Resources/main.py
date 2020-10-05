# open csv file
import os
import csv
path = os.path.join("..","Resources","budget_data.csv")
outputFile = os.path.join("..","Resources","PyBank.txt")

#variables
current = 0
month_count = 0
totalrev = 0
prior = 0
averagechange = 0
totalchange = 0
Highest_profit = ["",0]
Profitdate = ""
Lossdate = ""
Lowest_profit = ["",999999999999999999999999]

totalchange = []
# read the csv file
with open(path) as file:
    csvreader = csv.reader(file, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
  # The total number of months included in the dataset
      month_count += 1
  # The net total amount of "Profit/Losses" over the entire period
      totalrev += int(row[1])
      if(prior !=0):
        averagechange = int(row[1]) - prior
      prior = int(row[1])
  # The average of the changes in "Profit/Losses" over the entire period
  # The greatest increase in profits (date and amount) over the entire period
  # The greatest decrease in losses (date and amount) over the entire period
      if(averagechange > Highest_profit[1]):
        Highest_profit[1] = averagechange
        Profitdate = str(row[0])
      if(averagechange < Lowest_profit[1]):
        Lowest_profit[1] = averagechange
        Lossdate = str(row[0])
      totalchange.append(averagechange)

    difference = sum(totalchange)/(len(totalchange)-1)


print("Financial Analysis")
print("-----------------------")
print("Total Months:", month_count)
print("Total:",  totalrev)
print("Average Change:",{round(difference,2)})
print("Greatest Increase in Profit:",Profitdate,{Highest_profit[1]})
print("Greatest Decrease in Profit:",Lossdate,{Lowest_profit[1]})

# output to a text file
with open(outputFile, "w") as txt:
  print(textFile)
      txt.write("Total Months:"+ str(month_count))
      txt.write("\n")
      txt.write("Total:"+ "$" + str(totalrev))
      txt.write("\n")
      txt.write("Average Change:"+ "$" + str(month_count))
      txt.write("\n")
      txt.write("Greatest Increase in Profit:"+ str(Profitdate) + str(Highest_profit[1])
      txt.write("\n")
      txt.write("Greatest Decrease in Profit:"+ str(Lossdate) + str(Lowest_profit))
      

  