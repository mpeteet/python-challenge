# Mona Peteet December 2020 - Python Homework - Py me up, Charlie. This is the script for the PyPoll challenge.
# 

# Import dependencies
import os
import csv

# Tell the program where the input and output files are located
election_csv = os.path.join('Resources', 'election_data.csv')
PyPoll_output = os.path.join('Analysis', 'PyPoll_output.txt')


# Create the lists and variables for data collection and calculation
candidates = []         # the list of candidates in the vote
number_votes = []       # number of votes each candidate got
vote_total = 0          # will hold the total number of votes cast
votes_percentage = []   # the percentage of the vote the candidate received, will be used to determine the winner
     

# Open and read the csv file
with open(election_csv, newline='') as csvfile:

    #Split the data by commas and read the header
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:      
        # Add to the counter that will be used for calculating the winner 
        vote_total = vote_total + 1

        # Create the list of candidates that recieved votes
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            number_votes.append(1)
        else:
            index = candidates.index(row[2])
            number_votes[index] += 1
    
    # Analysis on the votes received -- calcuate and format the percentage
    for votes in number_votes:
        percentage = (votes/vote_total) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        votes_percentage.append(percentage)
    
    # What are the results of the election and determine the winner
    most_votes = max(number_votes)
    index = number_votes.index(most_votes)
    election_winner = candidates[index]


# Display the results of the election
print(f'\nElection Results')
print(f'---------------------------')
print(f'Total Votes: {str(vote_total)}')
print(f'---------------------------')
for i in range(len(candidates)):
    print(f'{candidates[i]}: {str(votes_percentage[i])} ({str(number_votes[i])})') 
print(f'---------------------------')
print(f'Winner: {election_winner}')
print(f'---------------------------')

# Print the election results analysis to the output file
with open(PyPoll_output, "w") as datafile:
    datafile.write('Election Results\n')  
    datafile.write('---------------------------\n')
    datafile.write(f'Total Votes: {str(vote_total)}\n')
    datafile.write('---------------------------\n')
    for i in range(len(candidates)):
        nextline = str(f'{candidates[i]}: {str(votes_percentage[i])} ({str(number_votes[i])})') 
        datafile.write('{}\n'.format(nextline))
    datafile.write('---------------------------\n')
    datafile.write(f'Winner: {election_winner}\n')
    datafile.write('---------------------------\n')
