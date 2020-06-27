import os
import csv

Tally = []
votecount = []
winner = []
candidates = []
cancount = []
count = []
vote_percent = []

election_csv = os.path.join("..","Resources", "election_data.csv")
with open(election_csv,newline="") as csvfile:      
        csvreader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csvreader)

        for row in csvreader:
            Tally.append(row[2])
            
        for i in set(Tally):
            candidates.append(i)
            counter = Tally.count(i)
            votecount.append(counter)
            avg = round(counter/len(Tally)*100, 3)
            vote_percent.append(avg)

winnerindex = votecount.index(max(votecount))
winner = candidates[winnerindex]
print(winner)

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