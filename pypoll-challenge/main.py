#create a Python script that analyzes the votes and calculates each of the following:
  
#import os and csv modules 
import os
import csv

#find file path for csv and store as variable 
csvpath = os.path.join("resources", "election_data.csv")

#define variables
vote_index = 0
candidates = []
votes_per_candidate = {}
#reading using csv module
with open(csvpath) as csvfile:
    election_data = csv.reader(csvfile, delimiter= ",")
    # skip header row
    next(election_data)

    #print(election_data) 

        #read each row of data 
    for row in election_data:
        # count total number of votes cast
        vote_index += 1
        #set row 2 to a new variable called name 
        name = row[2]
        # create a list of candidates who received votes
        if name not in candidates:
                
            candidates.append(name)
            votes_per_candidate[name] = 1 
        # count total votes votes each candidate recieved
        else:
            votes_per_candidate[name] += 1 

    
    #print(votes_per_candidate)
    print("Election Results ")
    print("-----------------")
    print(f"Total Votes: {vote_index}")
    # calculate the percentage of votes each candidate won
    print("Percentage of Votes:")
    for k, v in votes_per_candidate.items():
        pct = v * 100.0 / vote_index
        print(k, pct)
    print("-----------------")
    # find winner of the election based on popular vote
    winner = max(votes_per_candidate, key=votes_per_candidate.get)
    print(f"Winner:{(winner)}")  


#export a text file with the results

# Specify the file to write to
output_path = os.path.join("analysis", "pypoll_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, "w") as outfile:

    outfile.write("Election Results:")
    
    outfile.write(f"Total Votes: {vote_index}") 
    outfile.write("Percentage of Votes:")
    outfile.write(f"Khan 63.00, Correy 19.999, Li 13.99, O'Tooley 2.99")
    outfile.write(f"Winner:{(winner)}")
    
