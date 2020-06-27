import os
import csv

totalMonths = []
totalProfits = []
MonthlyChange = []
maxMonth = []
minMonth = []
maxChange = 0
minChange = 0
AvgChange = 0


budget = os.path.join("..","Resources", "budget_data.csv")
with open(budget,newline="") as csvfile:      
        csvreader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csvreader)
    #def Analysis(monthtotal, profitlosstotal):
        for row in csvreader:

                totalMonths.append(row[0])
                totalProfits.append(int(row[1]))

        for x in range(0,len(totalProfits)-1):

                MonthlyChange.append(totalProfits[x+1]-totalProfits[x])
                AvgChange = round(sum(MonthlyChange)/len(MonthlyChange),2)
                maxChange = max(MonthlyChange)
                minChange = min(MonthlyChange)
maxMonth = MonthlyChange.index(max(MonthlyChange))
minMonth = MonthlyChange.index(min(MonthlyChange))
                
with open("FinancialOutput.txt","w") as file:

        l = (f"Financial Analysis\n---------------------------\nTotal Months:  {len(totalMonths)}\n"
        f"Total:  ${sum(totalProfits)}\nAverage Change:  ${AvgChange}\n"
        f"Greatest Increase in Profits: {(totalMonths[maxMonth+1])}  (${maxChange}\n"
        f"Greatest Decrease in Profits: {(totalMonths[minMonth+1])}  (${minChange})")

        file.write(l)

print("Financial Analysis")
print("---------------------------")
print(f"Total Months:  {len(totalMonths)}")
print(f"Total:  ${sum(totalProfits)}")
print(f"Average Change:  ${AvgChange}")
print(f"Greatest Increase in Profits: {(totalMonths[maxMonth+1])}  (${maxChange})")
print(f"Greatest Decrease in Profits: {(totalMonths[minMonth+1])}  (${minChange})")          