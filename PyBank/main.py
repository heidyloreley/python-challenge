import os
import csv

csvpath = os.path.join("..","budget_data.csv")

# Store data in: 
monthsList = []
PLValue = []
PLChangeValue = []
PLChangeList = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        
        # Fill empty lists
        monthsList.append(row[0])
        monthsCount = len(monthsList)
        
        PLValue.append(int(row[1]))
    #print(PLValue)
    PLValueLength = len(PLValue) 
    #print(PLValueLength)

    for x in range(PLValueLength-1):  
        PLChangeValue = (PLValue[x+1]) - (PLValue[x])
        PLChangeList.append(PLChangeValue)
    #print(PLChangeList)


# The total number of months included in the dataset    
    monthsCount = len(monthsList)
    #print(monthsCount)
    
    print("Finantial Analysis")
    print("---------------------------------")
    printMonths = (f'Total Months: {monthsCount}')
    print(printMonths)
    
# The net total amount of "Profit/Losses" over the entire period
    PLValueAmount = sum(PLValue)          # PLValue is INT
    #print("$"+str(PLValueAmount))
    printPLAmount = (f'Total: ${str(PLValueAmount)}')
    print(printPLAmount)
    
#   The average of the changes in "Profit/Losses" over the entire period   
    PLChangeAmount = round(sum(PLChangeList)/len(PLChangeList),2)
    printAvCh = (f'Average Change: ${str(PLChangeAmount)}')
    print(printAvCh)
    
    
# The greatest increase in profits (date and amount) over the entire period
    GIncreasePL =max(PLChangeList)
    IndexGIncreasePL= PLChangeList.index(GIncreasePL)
    MonthGIncreasePL= monthsList[IndexGIncreasePL+1]
    printIncrease = (f'Greatest Increase in Profits: {MonthGIncreasePL} (${str(GIncreasePL)})')
    print(printIncrease)
    
# The greatest decrease in losses (date and amount) over the entire period
    GDecreasePL =min(PLChangeList)
    IndexGDecreasePL= PLChangeList.index(GDecreasePL)
    MonthGDecreasePL= monthsList[IndexGDecreasePL+1]
    printDecrease = (f'Greatest Decrease in Profits: {MonthGDecreasePL} (${str(GDecreasePL)})')
    print(printDecrease)

    
# Write a new document with the final analysis

Analysis = ["Finantial Analysis",printMonths, printPLAmount,printAvCh,printIncrease,printDecrease]

NewFile = open ("budget_analysis.txt","w")
for line in Analysis:
    NewFile.write(line)
    NewFile.write("\n")
NewFile.close()
    
