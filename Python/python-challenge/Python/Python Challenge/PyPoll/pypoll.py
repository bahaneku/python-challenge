# Modules
import os
import csv
import pandas as pd

# Create lists
votes = []
cand = []
cand_list = []

# Set a path for the file
csvpath = os.path.join('Resources/election_data.csv')

# Open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    for row in csvreader:
      votes.append(row[0])
      cand.append(row[2])

# Calculate the total number of votes cast
    vote_total = len(votes)

# Look for values in candidate list
    can_set = set(cand)
    cand_list = list(can_set)

# Create lists for each candidate
    khan = []
    correy = []
    li = []
    otooley = []

# Iterate through csv file and add each candidate to their respective list count
    for c in cand:
        if c == "Khan":
            khan.append(c)
        elif c == "Correy":
            correy.append(c)
        elif c == "Li":
            li.append(c)
        elif c == "O'Tooley":
            otooley.append(c)

# Calclate percentage of votes for each candidate
    khan_pct = len(khan)/vote_total
    correy_pct = len(correy)/vote_total
    li_pct = len(li)/vote_total
    otooley_pct = len(otooley)/vote_total

    print("Election Results")
    print("------------------------------")
    print(f"Total Votes: {vote_total}")
    print("------------------------------")
    print("Khan: " + str(len(khan)) + "    {:.2%}".format(khan_pct))
    print("Correy: " + str(len(correy)) + "    {:.2%}".format(correy_pct))
    print("Li: " + str(len(li)) + "    {:.2%}".format(li_pct))
    print("O'Tooley: " + str(len(otooley)) + "    {:.2%}".format(otooley_pct))
    print("------------------------------")
    print("Winner: Khan")
    print("------------------------------")

# Set an output path for the file
output = os.path.join('analysis/election_data.txt')
with open(output, 'w') as txtfile:
    txtfile.writelines("Election Results")
    txtfile.writelines("------------------------------")
    txtfile.writelines(f"Total Votes: {vote_total} \n")
    txtfile.writelines("------------------------------")
    txtfile.writelines("Khan: " + str(len(khan)) + "    {:.2%}".format(khan_pct))
    txtfile.writelines("Correy: " + str(len(correy)) + "    {:.2%}".format(correy_pct))
    txtfile.writelines("Li: " + str(len(li)) + "    {:.2%}".format(li_pct))
    txtfile.writelines("O'Tooley: " + str(len(otooley)) + "    {:.2%}".format(otooley_pct))
    txtfile.writelines("------------------------------ \n")
    txtfile.writelines("Winner: Khan")
    txtfile.writelines("------------------------------")
