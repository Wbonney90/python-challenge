#+![Revenue](Images/revenue-per-lead.jpg)

#* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company.
# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv).
# The dataset is composed of two columns: `Date` and `Profit/Losses`.
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)

import os
import csv

total = 0

csvpath = os.path.join("..","PyBank","budget_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # * The total number of months included in the dataset
    numline=len(csvfile.readlines())
    print("Total Month: ", numline)

    # * The total net amount of "Profit/Losses" over the entire period
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    net_profit=[]
    for rows in csvreader:
        net_profit.append(rows[1])
    net_profit.remove("Profit/Losses")
    net_profit = [int(rows) for rows in net_profit]
    total_net = ("Total: $" + str(sum(net_profit)))
    print(total_net)

    #Failed attempt to total column 2
    #for row in csv.reader(csvfile):
        #total += float(row[column2])
    #print(total)

  #* The average change in "Profit/Losses" between months over the entire period

  

  #* The greatest increase in profits (date and amount) over the entire period

  #* The greatest decrease in losses (date and amount) over the entire period

#* As an example, your analysis should look similar to the one below:

  #```text
  #Financial Analysis
  #----------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
 # Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
  #```

#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.
