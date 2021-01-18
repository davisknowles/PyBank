#import os and csv modules 
import os
import csv

#find file path for csv and store as variable 
csvpath = os.path.join("resources", "pybank_data.csv")

#define variables
total_months = 0
current_pl = 0
previous_pl = 0
net_pl = 0
total_change_pl = 0 
current_change_pl = 0

max_increase = 0
max_decrease = 0
net_prof = 0
#reading using csv module
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    next(csvreader)

    print(csvreader)  

   #read each row of data 
    for row in csvreader:
    
        # count total number of months
        total_months += 1
        # calculate net total amount in profit/losses
        current_pl = int(row[1])
        net_prof += current_pl
        # calculate changes in profit/losses over entire period, then find the average 
        if total_months == 1:
            current_pl = int(row[1])
            previous_pl = current_pl
            
        else:
            current_pl = int(row[1])
            current_change_pl = current_pl - previous_pl
            total_change_pl += current_change_pl
            #store current pl to previous pl
            previous_pl = current_pl
            
            
        # calculate the greatest increase in profits (date and amount) 
        if current_change_pl > max_increase:
            max_increase = current_change_pl
            max_increase_month = row[0] 
        # calculate the greatest decrease in profits (date and amount)
        elif current_change_pl < max_decrease:
            max_decrease = current_change_pl
            max_decrease_month = row[0] 

#print output to terminal 
print("Financial Analysis")
print("-------------------")
print(f"Total Months: {total_months}") 
print(f"Net Profit: ${net_prof}")
print(f"Average Change: ${total_change_pl / total_months}")
print(f"Greatest Increase in Profits: {max_increase_month} ({max_increase}) ")
print(f"Greatest Decrease in Profits: {max_decrease_month} ({max_decrease})")

#save output as text file 
# Specify the file to write to
output_path = os.path.join("analysis", "pybank_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, "w") as outfile:

    outfile.write("Financial Analysis:")
    
    outfile.write(f"Total Months: {total_months}") 
    outfile.write(f"Net Profit: ${net_prof}")
    outfile.write(f"Average Change: ${total_change_pl / total_months}")
    outfile.write(f"Greatest Increase in Profits: {max_increase_month} ({max_increase}) ")
    outfile.write(f"Greatest Decrease in Profits: {max_decrease_month} ({max_decrease})")