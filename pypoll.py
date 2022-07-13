import csv
import os

# Assign a variable for the file to load the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Prepare the file where the output will go
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Establish variable to count votes and hold candidate list
candidate_options = []
total_votes = 0
candidate_votes = {}
winner = ""
winning_count=0
winning_percentage=0.0

# Open the election results and read the file
with open (file_to_load) as election_data:

    #read the data file
    file_reader= csv.reader(election_data)

    #Read the headers
    headers = next(file_reader)

    #Print the file
    for row in file_reader:
        #Count each vote
        total_votes += 1
        recipient = row[2]
        #Put the candidate in the list, if they aren't already there
        if recipient not in candidate_options:
            candidate_options.append(recipient)
            candidate_votes[recipient]=0

        candidate_votes[recipient]+=1

#Calculate and display vote percentages
    for person in candidate_votes:

        votes = candidate_votes[person]
        vote_percentage = float(votes)/float(total_votes)

        if votes > winning_count:
            winner = person
            winning_count = votes
            winning_percentage = vote_percentage

        print (f'{person}: received {vote_percentage:.1%} of the votes.')

#Print the total
print(total_votes)

print (candidate_options)

print(candidate_votes)

print(f'The winning candidate was {winner}, who had {winning_count} votes. That was {winning_percentage:.1%} of the total votes.')

