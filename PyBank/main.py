import csv

#Defining variables for our financial analysis
total_months = 0
total_profit_losses = 0
previous_profit_loss = None
profit_changes = []

#For Greatest increase and Greatest decrese created dictionaries to track the largest increase and decrease in amount

greatest_increase = {"date": None, "amount": float("-inf")} #float("-inf") ensures that any positive increase will be considered larger
greatest_decrease = {"date": None, "amount": float("inf")} #float("inf") ensures that any negative decrease will be considered smaller

#My CSV file path 
csvpath = "Pybank/Resources/budget_data.csv"

#Read in the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skiping the header row
    next(csvreader, None)

    #Looping over each row in the CSV file
    for row in csvreader:
        #extract date and profit/loss value from the row
        date = row[0]
        profit_loss = int(row[1])

        #add to total_months and total_profit/loss value
        total_months +=1
        total_profit_losses +=profit_loss

        #calculate the profit change if this is not the header row
        if previous_profit_loss is not None:
            profit_change = profit_loss - previous_profit_loss
            profit_changes.append(profit_change)

            #Calculate greatest increase and greatest decrease

            if profit_change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = profit_change
            if profit_change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = profit_change

        #Update previous_profit_loss for the next iteration
        previous_profit_loss = profit_loss
    
    #calculate average profit change
    average_change = sum(profit_changes)/len(profit_changes)

#Print the results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

#Having all our results in a string for our text file
financial_analysis = f"Financial Analysis\n" \
                     f"------------------\n" \
                     f"Total Months: {total_months}\n" \
                     f"Total: ${total_profit_losses}\n" \
                     f"Average Change: ${average_change:.2f}\n" \
                     f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n" \
                     f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"

#Write our results to a text file
with open("PyBank/analysis/financial_analysis.txt", 'w') as txtfile:
    txtfile.write(financial_analysis)