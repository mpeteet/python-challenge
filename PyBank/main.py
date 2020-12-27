# Mona Peteet December 2020 - Python Homework - Py me up, Charlie. This is the script for the PyBank challenge.
# 
# Import dependencies
import os
import csv


# Tell the program where the input and output files are located
budgetdata_csv = os.path.join('Resources', 'budget_data.csv')
PyBank_output = os.path.join('..', 'Analysis', 'PyBank_output.txt')

# These are the lists that will store data for analysis
# NEW THOUGHTS - define a FUNCTION (give it a name) and assign variables and values (like these)
# NEW THOUGHTS - the functions name could be "BankPL_analysis"
# NEW THOUGHTS - sample calc for the fuction could be "Number_of_months = str(months + 1)"
# NEW THOUGHTS - sample calc "Total_PL = str(profits_losses)"
months = []
profits_losses = []



# Open and read the csv file
with open(budgetdata_csv, newline='') as csvfile:

    #Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    #print(header)
       
    for row in csvreader:
        # What are the total number of months in the dataset?
        month = str(row[0])
        months.append(month)

        # What is net total of Profit/Losses?
        profit_loss = int(row[1])
        profits_losses.append(profit_loss)
      
        # Determine the average change. Will need to perform a calculation
        #   (e.g. subtract row 2 from row1, subtract row 3 from row 2) on the prior row
        #   and capture the output in a new list "change" that can be evaluated
        #   to determine the greatest increase and decrease

        # This is the placeholder for average change
        avg_change = []

        # This is the list that will hold the changes 
        changes = []

        # Create the variables needed for the loop calculations
        x = 1, y = 0



      
        #changes = {(profit_losses[row])
        #changes.append(change)]
        





        # Find the greatest increase in profits for Feb 2012

        #profit_losses.max(profit_loss) = increase
       
        # Find the greatest decrease in profits for Sep 2013
        #profit_losses.min(profit_loss) = decrease




    print(f'Total Months: ', len(months))
    print(f'Total: $', sum(profits_losses)) 
    #print(f'Greatest Increase in Profits:' ()
    # Additional calcs testing out statiscal functions available for printing
    print(f'Min P/L: $', min(profits_losses))
    print(f'Max P/L: $', max(profits_losses))
    #print(f'P/L Average: $', statistics.mean(profits_losses))
    


# Open the output file
#with open(PyBank_output, "w", newline="") as datafile

    #Write to the output file
    #writer = csv.writer(datafile)

        
       
