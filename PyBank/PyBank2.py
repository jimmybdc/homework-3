import os
import csv

# Path to collect data from the PyBankfolder
PyBankCSV = os.path.join('..','PyBank','budget_data_2.csv')

# Define the function and have it accept the parameters
def getRevenue(months, revenue):
    
    diff = []

    # The total number of months included in the dataset
    totalMonths = len(months)

    # The total amount of revenue gained over the entire period
    totalRevenue = sum(revenue) 

    # The average change in revenue between months over the entire period
    for i in range(len(revenue) - 1):
        diff.append(revenue[i+1]-revenue[i])

    averageChanges = sum(diff) / len(diff)

    # The greatest increase in revenue (date and amount) over the entire period
    greatest_increase_date = months[diff.index(max(diff))]
    greatest_increase = max(diff)

    # The greatest decrease in revenue (date and amount) over the entire period
    greatest_decrease_date = months[diff.index(min(diff))]
    greatest_decrease = min(diff) 

    # Print Financial Analysis

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(totalMonths))
    print("Total Revenue: $" + str(int(totalRevenue)))
    print("Average Revenue Change: $" + str(int(averageChanges)))
    print("Greatest Increase in Revenue: " + str(greatest_increase_date) + " ($" + str(greatest_increase) + ")")
    print("Greatest Decrease in Revenue: " + str(greatest_decrease_date) + " ($" + str(greatest_decrease) + ")")

# Read in the CSV file (r is for read)
with open(PyBankCSV, 'r') as csvfile:
    
    # Making two lists
    months = []
    revenue = []

    # Split the data commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Loop through the data
    for row in csvreader:
        if row[0] == "Date": continue
        months.append(row[0])
        revenue.append(int(row[1]))
    
    getRevenue(months, revenue)
