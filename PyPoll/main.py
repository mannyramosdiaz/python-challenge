import os
import csv
#declaring lists to collect data
Tally = []
votecount = []
winner = []
candidates = []
cancount = []
count = []
vote_percent = []
#using database to read csv
election_csv = os.path.join("..","Resources", "election_data.csv")
with open(election_csv,newline="") as csvfile:      
        csvreader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csvreader)
#collecting all the votes
        for row in csvreader:
            Tally.append(row[2])
#going through all votes, counter counts for each candidates and votecount is a list for each candidate
        for i in set(Tally):
            candidates.append(i)
            counter = Tally.count(i)
            votecount.append(counter)
            avg = round(counter/len(Tally)*100, 3)
            vote_percent.append(avg)
#winner picks the largest of the votecount, winnerindex gives back the list element and winner calls on it.
winnerindex = votecount.index(max(votecount))
winner = candidates[winnerindex]
print(winner)
#print results and right a file with them
with open("ElectionResults.txt","w") as file:
    l = ("Election Results\n"
    "-------------------------\n"
    f"Total Votes: {len(Tally)}\n"
    f"-------------------------\n"
    f"{candidates[0]}: {vote_percent[0]}% ({votecount[0]})\n"
    f"{candidates[1]}: {vote_percent[1]}% ({votecount[1]})\n"
    f"{candidates[2]}: {vote_percent[2]}% ({votecount[2]})\n"
    f"{candidates[3]}: {vote_percent[3]}% ({votecount[3]})\n"
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------")

    file.write(l)

print(l)
