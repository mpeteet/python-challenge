# Mona Peteet December 2020 - Python Homework - Py me up, Charlie. This is the script for the PyBank challenge.
# 
# Import dependencies
import os
import csv

# Tell the program where the input and output files are located
budgetdata_csv = os.path.join('Resources', 'budget_data.csv')
PyBank_output = os.path.join('..', 'Analysis', 'PyBank_output.txt')

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
    print(header)
       
    for row in csvreader:
        # What are the total number of months in the dataset?
        month = str(row[0])
        months.append(month)

        # What is net total of Profit/Losses?
        profit_loss = int(row[1])
        profits_losses.append(profit_loss)

        # The average change is:
        # 

        # Find the greatest increase in profits for Feb 2012
        #profit_losses.max(profit_loss) = increase
       
        # Find the greatest decrease in profits for Sep 2013
        #profit_losses.min(profit_loss) = decrease




    print(f'Total Months:', len(months))
    print(f'Total: $', sum(profits_losses)) 
    print(f'')
    #print(f'Greatest Increase in Profits:' increase[0], increase[1])

# Open the output file
#with open(PyBank_output, "w", newline="") as datafile

    #Write to the output file
    #writer = csv.writer(datafile)

        
       
