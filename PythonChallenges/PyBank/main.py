# ByBank Homework
# ---------------------------------------------------------------------------
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
# Final script should both print the analysis to the terminal and export a text file with the results.

# ----------------------------------------------------
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join(".","python-challenge","PythonChallenges","PyBank",'budget_data.csv')

# Create lists
total_months = []
months = 0
profit = 0
total_profit = []
monthly_change = []

# Method 2: Improved Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Go through file and add all the numbers in the second column to get Total Net Profit for entire data set
    csv_header = next(csvreader)
    for row in csv.reader(csvfile):
        months = months + 1  #Used for Total Months
        # profit = profit + int(row[1])

        total_months.append(row[0]) 
        total_profit.append(int(row[1]))

    # Iterate through all profits by month to get the changes
    for i in range(len(total_profit)-1):
        monthly_change.append(total_profit[i+1]-total_profit[i])
    
    # In the monthly change list, find max and min of monthly change value
    max_increase_change = max(monthly_change)
    max_decrease_change = min(monthly_change)

    # print(monthly_change.index(max(monthly_change))) #Position of Greatest Increase in Profits
    # print(monthly_change.index(min(monthly_change))) #Position of Greatest Decrease in Profits

    max_position = (monthly_change.index(max(monthly_change)))
    min_position = (monthly_change.index(min(monthly_change)))

    total_months.pop(0)
    
    # print(total_months[max_position])
    # print(total_months[min_position])

# -----------------------------------------------------------------------
# Print Financial Analysis Summary
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {(months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: ${round(sum(monthly_change)/len(monthly_change),2)}") 
print(f"Greatest Increase in Profits: {(total_months[max_position])} (${(str(max_increase_change))})")
print(f"Greatest Decrease in Profits: {(total_months[min_position])} (${(str(max_decrease_change))})")

# -----------------------------------------------------------------------
# Specify the file to write to
# output_path = os.path.join(".","python-challenge","PythonChallenges","PyBank",'FinancialAnalysisSummary.txt')

# Open the file using "write" mode. Specify the variable to hold the contents
with open('python-challenge\PythonChallenges\PyBank\FinancialAnalysisSummary.txt','w') as outfile:
    
    # # Initiate csv.writer
    # csvwriter = csv.writer(csvfile, delimiter=',')

    #Write Header
    print('----------------------------', file=outfile)
    print(["Financial Analysis"], file=outfile)

    # Write second Row - Dotted Line
    print('----------------------------', file=outfile)

    print([f"Total Months: {round(len(total_months))}"], file=outfile)
    print([f"Total: $ {sum(total_profit)}"], file=outfile)
    print([f"Average Change: $ {round(sum(monthly_change)/len(monthly_change),2)}"], file=outfile)
    print([f"Greatest Increase in Profits: {(total_months[max_position])} (${(str(max_increase_change))})"], file=outfile)
    print([f"Greatest Increase in Profits: {(total_months[min_position])} (${(str(max_decrease_change))})"], file=outfile)

   