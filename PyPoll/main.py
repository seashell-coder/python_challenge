
import csv

#Initialize Variables
total_votes = 0
candidates = []
candidate_votes = {}
candidate = " "

#Defining the CSV file path
csv_file_path = 'PyPoll/Resources/election_data.csv'

#Read the CSV file line bt line

with open(csv_file_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skipping the header row
    next(csvreader, None)

    #Looping over each row in the CSV file to retrive the data 
    for row in csvreader:
        try:
            voter_id = row[0]
            county = row[1]
            candidate = row[2]
        except IndexError:
            pass
        #calculating the total amount of votes
        total_votes +=1

        #Adding candidate to the candidates[] if not already present
        if candidate not in candidates:
                candidates.append(candidate)

        #count the votes for each candidate
        if candidate in candidate_votes:
                candidate_votes[candidate] +=1

        else:
                candidate_votes[candidate] = 1

#Calculate the percentage of votes each candidate won
percentages = {}
for candidate,votes in candidate_votes.items():
    percentage = (votes/total_votes) * 100
    percentages[candidate] = percentage

#Finding the winner based on maximum votes
max_votes = max(candidate_votes.values())
winners = []
for candidate, votes in candidate_votes.items():
    if votes == max_votes:
        winners.append(candidate)

# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
print("Winner: ", winners[0])
print("-------------------------")

#Write our analysis results into a txt file
with open("PyPoll/analysis/election_analysis.txt", "w") as txtfile:
     txtfile.write("Election Results\n")
     txtfile.write("-------------------------\n")
     txtfile.write(f"Total Votes: {total_votes}\n")
     txtfile.write("-------------------------\n")
     for candidate in candidates:
            txtfile.write(f"{candidate}: {percentages[candidate]:.3f}% ({candidate_votes[candidate]})\n")
     txtfile.write("-------------------------\n")
     txtfile.write("Winner: " + winners[0] + "\n")
     txtfile.write("-------------------------\n")