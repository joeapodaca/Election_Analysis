#The data we need to retrieve.
#1. The total number if votes cast.
#2. A complete list of candidates whoe received votes.
#3. The percentage of votes each candidate won.
#4 the total number of votes each candidate won.
#5 The winner of the election based on popular vote.

#Add dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources', 'election_results.csv')
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate_options
candidate_options = []

#Declare candiate dictionary.
candidate_votes={}


#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read the header row.
    headers = next(file_reader)
    #print (headers)
     
    #Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count.
        total_votes +=1

        #Print the candidate name from each row.
        candidate_name =row[2]

        #Add candidate name to the list.
        #candidate_options.append(candidate_name)

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
        #Add name to list of candidates.
            candidate_options.append(candidate_name)

            #Begin tracking that candidates vote count.
            candidate_votes[candidate_name]=0

        #add a vote to that candidates count.
        candidate_votes[candidate_name]+=1


#Winning candidate and winning Count tracekr
winning_canidate = ""
winning_count = 0
winning_percentage = 0


#Determine the percentage of votes for each candidate by looping through the counts.
#Iterate through the candaiate list.
for candidate_name in candidate_votes:
    #Retrieve vote count.
    votes = candidate_votes[candidate_name]
    #Calculate percentage of votes.
    vote_percentage = float(votes)/float(total_votes)*100
    #print the candidate name and percantage of votes
    #print(f"{candidate_name}:recieved {vote_percentage:.1f}% of the vote.")
    #Determine winning vote count and candidate
    if(votes > winning_count) and (vote_percentage > winning_percentage):
        #vote percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #Set winning_candidate equal to candidates name.
        winning_candidate = candidate_name
#votes to terminal.
    print(f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")
winning_candidate_summary = (
f"--------------------------\n"
f"Winner:{winning_candidate}\n"
f"Winning Vote Count:{winning_count}\n"
f"Winning Percentage:{winning_percentage:.1f}%\n"
f"--------------------------\n")
print(winning_candidate_summary)


