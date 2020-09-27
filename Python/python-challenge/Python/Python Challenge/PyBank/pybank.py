# Modules
import os
import csv

# Create lists
date=[]
profit=[]
delta=[]

# change = delta = 0

# Set a path for the file
csvpath = os.path.join('Resources/budget_data.csv')

# Open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    for row in csvreader:
      date.append(row[0])
      profit.append(row[1])

# Calculate the total number of months
month_total=(len(date))

# Calculate the total profit and return as an integer
for i in range(0, len(profit)):
    profit[i] = int(profit[i])

profit_total = sum(profit)

# Calculate profit change and add to list "delta"
for i in range(1, len(profit)):
    d = (profit[i] - profit[i-1])

    delta.append(d)

add_total = 0

for i in range(0, len(delta)):
    add_total = add_total + delta[i]

avg_delta = (add_total/len(delta))

# Locate maximum delta value and link it with date
max_d = max(delta)

for i in range(0, len(delta)):
    if delta[i] == max_d:
        max_date = date[i+1]

# Locate minimum delta value and link it with date
max_l = min(delta)

for i in range(0, len(delta)):
    if delta[i] == max_l:
        min_date = date[i+1]

print("Financial Analysis")
print("------------------------------------")
print(f"Total Months: {month_total}")
print(f"Total: ${profit_total}")
print(f"Average Change: {avg_delta}")
print(f"Greatest Increase in Profits: {max_date} ({max_d})")
print(f"Greatest Decrease in Profits: {min_date} ({max_l})")

# Set an output path for the file
output = os.path.join('analysis/budget_data.txt')
with open(output, 'w') as txtfile:
    txtfile.writelines("Financial Analysis")
    txtfile.writelines("------------------------------------")
    txtfile.writelines(f"Total Months: {month_total}")
    txtfile.writelines(f"Total: ${profit_total}")
    txtfile.writelines(f"Average Change: {avg_delta}")
    txtfile.writelines(f"Greatest Increase in Profits: {max_date} ({max_d})")
    txtfile.writelines(f"Greatest Decrease in Profits: {min_date} ({max_l})")