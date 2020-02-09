import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join("..","election_data.csv")

# Store data in: 

VoterIDList = []
CountyName = []
Candidates = []
CandidateName = ["Khan","Correy","Li","O'Tooley"]
CandidateName2 = []
 

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        
        # Fill empty lists
        VoterIDList.append(row[0])
        VoterIDCount = len(VoterIDList)
        
        Candidates.append(row[2])
        CandidatesCount = len(Candidates)

# The total number of votes each candidate won

    Cand1Count = Candidates.count(CandidateName[0])
    Cand2Count = Candidates.count(CandidateName[1])
    Cand3Count = Candidates.count(CandidateName[2])
    Cand4Count = Candidates.count(CandidateName[3])
   
    
# The percentage of votes each candidate won

    Cand1Pct = round(Cand1Count/VoterIDCount,4)*100
    Cand2Pct = round(Cand2Count/VoterIDCount,4)*100
    Cand3Pct = round(Cand3Count/VoterIDCount,4)*100
    Cand4Pct = round(Cand4Count/VoterIDCount,4)*100
    
    printC1 = (f'{CandidateName[0]}: {Cand1Pct}% ({Cand1Count})')
    printC2 = (f'{CandidateName[1]}: {Cand2Pct}% ({Cand2Count})')
    printC3 = (f'{CandidateName[2]}: {Cand3Pct}% ({Cand3Count})')
    printC4 = (f'{CandidateName[3]}: {Cand4Pct}% ({Cand4Count})')

    
    print("Election Results")
    print("---------------------------------")
    
    #  The total number of votes cast
    printVotes = (f'Total Votes: {str(VoterIDCount)}')
    print(printVotes)

    # The total number of votes each candidate won
    print(printC1)
    print(printC2)
    print(printC3)
    print(printC4)
    
    # The winner of the election based on popular vote.

    VotesPerCand = [Cand1Count,Cand2Count,Cand3Count,Cand4Count]
    WinnerCount =max(VotesPerCand)
            
    if VotesPerCand[0] == WinnerCount:
        print("Winner: "+(CandidateName[0]))
    elif VotesPerCand[1] == WinnerCount:
        print("Winner: "+(CandidateName[1]))
    elif VotesPerCand[1] == WinnerCount:
        print("Winner: "+(CandidateName[2]))
    elif VotesPerCand[1] == WinnerCount:
        print("Winner: "+(CandidateName[3]))
        
print("---------------------------------")    
# Write a new document with the final analysis

Analysis = ["Election Results",printVotes,printC1,printC2,printC3,printC4,"Winner: Khan"]

NewFile = open ("election_analysis.txt","w")
for line in Analysis:
    NewFile.write(line)
    NewFile.write("\n")
NewFile.close()