# open csv file
import os
import csv
path = os.path.join("..","Resources","election_data.csv")
Output = os.path.join("..","Resources","Output.txt")
# variables
totalcount = 0
khancount = 0
khanpercent = 0.00
correycount = 0
correypercent = 0.00
licount = 0
lipercent = 0.00
otooleycount = 0
otooleypercent = 0.00
winner = ""
with open(path) as file:
    csvreader = csv.reader(file, delimiter=",")
    csvheader = next(csvreader)
# The total number of votes cast
    for row in csvreader:
        totalcount += 1
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won

        if (row[2] == 'Khan'):
            khancount = khancount + 1
        elif (row[2] == 'Correy'):
            correycount = correycount +1
        elif (row[2] == 'Li'):
            licount = licount + 1
        elif (row[2] == "O'Tooley"):
            otooleycount = otooleycount + 1
    khanpercent = round(khancount / totalcount *100, 2)
    correypercent = round(correycount / totalcount *100 ,2)
    lipercent = round(licount / totalcount *100, 2)
    otooleypercent = round(otooleycount / totalcount *100, 2)

# The winner of the election based on popular vote.
winnercount = max(khancount, correycount, licount, otooleycount)
if (winnercount == khancount):
    winner = "Khan"
elif (winnercount == correycount):
    winner = "Correy"
elif (winnercount == licount):
    winner = "Li"
elif (winnercount == otooleycount):
    winner = "O'Tooley"
# print out the results
print("Election Results")
print("-----------------------")
print("Total Votes:", totalcount)
print("-----------------------")
print(f"Khan:,{round(khanpercent,3)}%, ({khancount})")
print(f"Correy:,{round(correypercent,3)}%, ({correycount})")
print(f"Li:,{round(lipercent,3)}%, ({licount})")
print(f"O'Tooley:,{round(otooleypercent,3)}%, ({otooleycount})")
print("------------------------")
print("Winner:", winner)
print("------------------------")

# Output a textfile
with open("Output.txt", "w") as text_file:
    print("Election Results", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Total Votes: {totalcount}", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Khan: {round(khanpercent, 3)}% ({khancount})", file=text_file)
    print(f"Correy: {round(correypercent, 3)}% ({correycount})", file=text_file)
    print(f"Li: {round(lipercent, 3)}% ({licount})", file=text_file)
    print(f"O'Tooley: {round(otooleypercent, 3)}% ({otooleycount})", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Winner: {winner}", file=text_file)
    print("-------------------------", file=text_file
