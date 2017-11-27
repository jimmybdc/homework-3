import os
import csv

# Path to collect data from the PyPollfolder
PyPollCSV = os.path.join('..', 'PyPoll','election_data_1.csv')

# Define the function 
def getPoll(voting_info):
    
    # The total number of votes cast
    total_votes = len(voting) 

    # Dictionary for candidates
    
    candidate_results = {}
    for candidate in voting_info:
        candidate_results[candidate] = 0
    for candidate in voting_info:
        candidate_results[candidate] +=1    
     

    # Print Election Results

    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(total_votes))
    print("----------------------------")
    for candidate in candidate_results:
        print(candidate + ": " + str(float(candidate_results[candidate] / total_votes)*100) + "% (" + str(candidate_results[candidate]) + ")")

    print("----------------------------")
    print("Winner: " + list(candidate_results.keys())[list(candidate_results.values()).index(max(candidate_results.values()))])
    print("----------------------------")

    file = open("results1.txt", "w")
    file.write("Election Results")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write("Total Votes: " + str(total_votes))
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    for candidate in candidate_results:
        file.write(candidate + ": " + str(float(candidate_results[candidate] / total_votes)*100) + "% (" + str(candidate_results[candidate]) + ")")
        file.write("\n")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write("Winner: " + list(candidate_results.keys())[list(candidate_results.values()).index(max(candidate_results.values()))])
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.close()

# Read in the CSV file (r is for read)
with open(PyPollCSV, 'r') as csvfile:
    
    # Making three lists
    voting = []

    # Split the data commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Loop through the data
    for row in csvreader:
        if row[0] == "Voter ID": continue
        voting.append(row[2])
    
    getPoll(voting)
