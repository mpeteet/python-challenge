# Mona Peteet December 2020 - Python Homework - Py me up, Charlie. This is the script for the PyBank challenge.
# 
# Import dependencies
import os
import csv

# Tell the program where the input and output files are located
budgetdata_csv = os.path.join('Resources', 'budget_data.csv')
#PyBank_output = os.path.join('..', 'Analysis', 'PyBank_output.txt')

# List for storing data
months = []
profits_losses = []
changes = []

# Variables for calculations

change_from_prior = 0
total_change_profits_losses = 0 
initial_profits_losses = 0
average_monthly_change = 0
total_profits_losses = 0

# Open and read the csv file
with open(budgetdata_csv, newline='') as csvfile:

    #Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
          
    for row in csvreader:
        # What are the total number of months in the dataset?
        months.append(row[0])
        
        # What is net total of Profit/Losses?
        profits_losses.append(row[1])
        total_profits_losses = total_profits_losses + int(row[1])
                   
        # Calculate the month to month change and capture the change for use later
        final_profits_losses = int(row[1])
        change_from_prior = final_profits_losses - initial_profits_losses
           
        # Capture the average monthly changes 
        changes.append(change_from_prior)

        total_change_profits_losses = total_change_profits_losses + change_from_prior
        initial_profits_losses = final_profits_losses

        # Calculate the average monthly change in profits/losses
        average_monthly_change = (total_change_profits_losses/len(months))

        # Find the greatest increase and decrease in profits
        greatest_increase_profits = max(changes)
        greatest_decrease_profits = min(changes)

        increase_date = months[changes.index(greatest_increase_profits)]
        decrease_date = months[changes.index(greatest_decrease_profits)]
       
        # Find the greatest decrease in profits for Sep 2013
        #profit_losses.min(profit_loss) = decrease


    print(f'Total Months: ', len(months))
    print(f'Total: $', (total_profits_losses)) 
    print(f'Average Change: $', round(average_monthly_change))
    print(f'Greatest Increase in Profits: ' + str(increase_date) + ' ($'+ str(greatest_increase_profits) + ')')
    print(f'Greatest Decrease in Profits: ' + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ')')
      


# Open the output file
#with open(PyBank_output, "w", newline="") as datafile

    #Write to the output file
    #writer = csv.writer(datafile)

        
       
