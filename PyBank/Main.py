#import os
#import csv

#total = 0

#svpath = os.path.join("..","PyBank","budget_data.csv")
#with open(csvpath, newline="") as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)

    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #print("Financial Anaylsis")
    #print("----------------------------")

    #The total number of months included in the dataset
    #numline=len(csvfile.readlines())
    #tot_month = ("Total Month: " + str(numline))
    #print(tot_month)

    #The total net amount of "Profit/Losses" over the entire period
#with open(csvpath, newline="") as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=",")
    #net_profit=[]
    #list_of_av_change = []
    #reat_inc_value = 0
    #great_dec_value = 99999999
    #for rows in csvreader:
        #net_profit.append(rows[1])
    #net_profit.remove("Profit/Losses")
    #net_profit = [int(rows) for rows in net_profit]
    #total_net = ("Total: $" + str(sum(net_profit)))
    #print(total_net)

    #Failed attempt to total column 2
    #for row in csv.reader(csvfile):
        #total += float(row[column2])
    #print(total)

    #The average change in "Profit/Losses" between months over the entire period

    #copy of Charlotte's code to analyze
    #av_change = [y - x for x, y in zip(net_profit, net_profit[1:])]
    #import statistics
    #x = statistics.mean(av_change)
    # round(x,2) returns a rounded number to the second decimal point
    #Average_Change = (f"Average Change: ${round(x, 2)}")
    #list_of_av_change.append(x)
    #print(Average_Change)
    #print(list_of_av_change)
    #print(x)

# * The greatest increase in profits (date and amount) over the entire period
# * The greatest decrease in losses (date and amount) over the entire period

#f = open(csvpath, 'r')
#reader = csv.reader(f)
#months_profit = {}
#for row in reader:
    #months_profit[row[0]] = {'month':row[0],'profit':row[1]}

    #if list_of_av_change > great_inc_value:
        #high = max(av_change)
        #date_of_greatest_inc = rows[0]
    #elif list_of_av_change < great_dec_value:
        #low = min(av_change)
        #date_of_greatest_dec = rows[0]
    #great_dec = ("Greatest Decrease in Profits: $" + str(low))
    #great_inc = ("Greatest Increase in Profits: $" + str(high))
    #print(date_of_greatest_inc)
    #print(date_of_greatest_dec)
    #print(great_dec)

#def writetofile():
    #output = "Financial_Analysis.txt"
    #Fin = "Financial Analysis"
    #Break = "----------------------------"
    #file = open(output,"w")
    #print(great_inc)
    #file.write(Fin + '\n')
    #file.write(Break + '\n')
    #file.write(tot_month + '\n')
    #file.write(total_net + '\n')
    #file.write(Average_Change + '\n')
    #file.write(great_inc + '\n')
    #file.write(great_dec + '\n')
    #file.close()
#writetofile()


import os
import csv

budget_data_sheet = "budget_data.csv"
budget_result_sheet = "budget_analysis.txt"


with open(budget_data_sheet, newline="") as budget_data_fh:
    fh_reader = csv.reader(budget_data_fh, delimiter=',')
    header = next(fh_reader)
    bank_data_list = []
    prev_month = 0
    months = 0
    total = 0
    for row in fh_reader:
        bank_data_list.append(row)
        if months == 0:
            bank_data_list[months].append(0)
        elif months > 0:
            bank_data_list[months].append(int(bank_data_list[months][1]) - prev_month)
            prev_month = int(bank_data_list[months][1])
        total += int(row[1])
        months += 1
    list_profit_loss = []
    total_change = 0.0
    for counter in range(0,(months - 1)):
        list_profit_loss.append(int(bank_data_list[counter][2]))
        total_change += list_profit_loss[counter]
print(bank_data_list)
max_profit = max(list_profit_loss)
max_loss = min(list_profit_loss)
avg_change = total_change/months
print(f"Net amount of Profit/Loss: {total}\n")
print(f"Total months in balance sheet: {months}\n")
print(f"Max Profit: {max_profit}\n")
print(f"Max Loss: {max_loss}\n")
print(f"Average Change: {avg_change}\n")
budget_data_fh.close()