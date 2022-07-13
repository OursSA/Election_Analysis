#Dependencies
import csv
import os

# Assign a variable for the file to load the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Prepare the file where the output will go
file_to_save = os.path.join("analysis", "election_results.txt")

#Establish variable to count votes and hold candidate list
candidate_options = []
total_votes = 0
candidate_votes = {}
#Set up variables to hold properties of the winning candidate
winner = ""
winning_count=0
winning_percentage=0.0

# Open the election results and read the file
with open (file_to_load) as election_data:

    #read the data file
    file_reader= csv.reader(election_data)

    #Read the headers
    headers = next(file_reader)

    #Look at each vote in the CSV file
    for row in file_reader:
        #Count each vote
        total_votes += 1
        recipient = row[2]
        #Put the candidate in the list, if they aren't already there
        if recipient not in candidate_options:
            candidate_options.append(recipient)
            candidate_votes[recipient]=0

        #Count the vote for the appropriate person
        candidate_votes[recipient]+=1
    with open(file_to_save,"w") as txt_file:
    
        # Print the final vote count to the terminal.
        election_results = (
            f'\nElection Results\n'
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
    
        print(election_results, end="")
        #Save the final vote count to the text file.
        txt_file.write(election_results)

        #Calculate and display vote percentages
        for person in candidate_votes:

            votes = candidate_votes[person]
            vote_percentage = float(votes)/float(total_votes)*100

            #If this person is the new leader, update the info about the winner
            if votes > winning_count:
                winner = person
                winning_count = votes
                winning_percentage = vote_percentage

            #Output the candidate's results to the terminal and the text file
            candidate_results = (f'{person}: {vote_percentage:.1f}% ({votes:,})\n')
            print(candidate_results)
            txt_file.write(candidate_results)

        #Store and print info about the winner
        winning_candidate_summary = (
            f'-------------------------\n'
            f'Winner: {winner}\n'
            f'Winning Vote Count: {winning_count:,}\n'
            f'Winning Percentage: {winning_percentage:.1f}%\n'
            f'-------------------------\n')

        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)

