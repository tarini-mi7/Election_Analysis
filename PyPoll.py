
# Total number of votes cast
#   Retrieve the data
#   Count of ballot id 
# A complete list of candidates who received votes
#   unique value from the column candidate
# Total number of votes each candidate received
#   create dictonary
#   populate the dictonary with candidate name as key ans number of votes for the candidate as values
# Percentage of votes each candidate won
#   output of thrid step divided by output of first step * 100
# The winner of the election based on popular vote
#  output of third step take the max value of all the values and return the corresponding candidate name.

import csv
from email.headerregistry import AddressHeader
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file
with open(file_to_load, 'r') as election_data:
    # To do: perform analysis.
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, 'w') as outfile:
    # Write some data to the file.
    outfile.write("Hello World")

with open(file_to_save, 'w') as txt_file:
    # Write three counties to the file.
    txt_file.write( "Counties in the election\n-------------------------\nArapahoe\nDenver\nJefferson")

# Open the election results and read the file
with open(file_to_load, 'r') as election_data: 
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)
# Print the header row.
    headers = next(file_reader)
    print(headers)


