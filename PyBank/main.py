# Mona Peteet December 2020 - Python Homework - Py me up, Charlie. This is the script for the PyBank challenge.
# 
# Import dependencies
import os
import csv

# Tell the program where the input files is located
budgetdata_csv = os.path.join('Resources', 'budget_data.csv')

# These are the lists that will store data for analysis
months = []
profits_losses = []
change =[]
increase = []
decrease = []


# Open and read the csv file
with open(budgetdata_csv, newline='') as csvfile:

    #Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
       
    for row in csvreader:
        # What are the total number of months in the dataset?
        month = str(row[0])
        months.append(month)

        #What is net total of Profit/Losses?
        profit_loss = int(row[1])
        profits_losses.append(profit_loss)


    print(f'Total Months:', len(months))
    print(f'Total: $', sum(profits_losses)) 


        
       
