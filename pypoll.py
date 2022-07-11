import csv
import os
# Assign a variable for the file to load the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Prepare the file where the output will go
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open (file_to_load) as election_data:

    #Do some analysis
    #read the data file
    file_reader= csv.reader(election_data)
    #Print the headers
    headers = next(file_reader)
    print(headers)
