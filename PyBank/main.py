import os
import csv
#declaring variables an lists
totalMonths = []
totalProfits = []
MonthlyChange = []
maxMonth = []
minMonth = []
maxChange = 0
minChange = 0
AvgChange = 0

#pathway  to read csv in python
budget = os.path.join("..","Resources", "budget_data.csv")
with open(budget,newline="") as csvfile:      
        csvreader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csvreader)
    #def Analysis(monthtotal, profitlosstotal):
        for row in csvreader:
#saving each parameter in different lists in the csv
                totalMonths.append(row[0])
                totalProfits.append(int(row[1]))

        for x in range(0,len(totalProfits)-1):
#getting differences from previous months, averaging it and max and min of those parameters
                MonthlyChange.append(totalProfits[x+1]-totalProfits[x])
                AvgChange = round(sum(MonthlyChange)/len(MonthlyChange),2)
                maxChange = max(MonthlyChange)
                minChange = min(MonthlyChange)
maxMonth = MonthlyChange.index(max(MonthlyChange))
minMonth = MonthlyChange.index(min(MonthlyChange))
#using the information to write a fie with data that is most revelant, as in profits, losses and averages
with open("FinancialOutput.txt","w") as file:

        l = (f"Financial Analysis\n---------------------------\nTotal Months:  {len(totalMonths)}\n"
        f"Total:  ${sum(totalProfits)}\nAverage Change:  ${AvgChange}\n"
        f"Greatest Increase in Profits: {(totalMonths[maxMonth+1])}  (${maxChange}\n"
        f"Greatest Decrease in Profits: {(totalMonths[minMonth+1])}  (${minChange})")

        file.write(l)
#displaying the results on the screen also
        print("Financial Analysis")
print("---------------------------")
print(f"Total Months:  {len(totalMonths)}")
print(f"Total:  ${sum(totalProfits)}")
print(f"Average Change:  ${AvgChange}")
print(f"Greatest Increase in Profits: {(totalMonths[maxMonth+1])}  (${maxChange})")
print(f"Greatest Decrease in Profits: {(totalMonths[minMonth+1])}  (${minChange})")          
