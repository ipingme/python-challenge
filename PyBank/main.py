import os
import csv

total_months = []
total = []
monthly_profit_change = []

print("Financial Analysis")
print("----------------------------")

# Open the CSV
file = os.path.join("Resources", "budget_data.csv")

with open(file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the header
    header = next(csvreader)  

    # Loop through each row
    for row in csvreader:
        # Add total months and total profit
        total_months.append(row[0])
        total.append(int(row[1]))

    # Get the monthly change in profits
    for row2 in range(len(total)-1):
        monthly_profit_change.append(total[row2+1]-total[row2])
    
    # print(monthly_profit_change)

    # Finds the max and min values
    max_value = str(max(monthly_profit_change))
    # print(max_value)
    min_value = str(min(monthly_profit_change))
    # print(min_value)
    
    # Loop through the monthly change in profits
    for row3 in range(len(monthly_profit_change)):
        month = str(total_months[row3+1])
        target = str(monthly_profit_change[row3])
        # print(month)
        # print(target)

        # condition to find max and min
        if target == max_value:
            max_value_conc = (str(month + " ($" + target))
        elif target == min_value:
            min_value_conc = (str(month + " ($" + target))

    # Prints all the results
    print(f"Total Months: {len(total_months)}")
    print(f"Total: ${sum(total)}")
    print(f"Average Change: ${round(sum(monthly_profit_change) / len(monthly_profit_change),2)}")
    print(f"Greatest Increase in Profits: {max_value_conc})")
    print(f"Greatest Decrease in Profits: {min_value_conc})")

    # Specify the file to write to
    output_path = os.path.join("Resources", "PyBank_Summary.txt")

    # Open the file using "write" mode.
    with open(output_path, 'w') as text_file:
        text_file.write(f"Financial Analysis")
        text_file.write(f"\n----------------------------")
        text_file.write(f"\nTotal Months: {len(total_months)}")
        text_file.write(f"\nTotal: ${sum(total)}")
        text_file.write(f"\nAverage Change: ${round(sum(monthly_profit_change) / len(monthly_profit_change),2)}")
        text_file.write(f"\nGreatest Increase in Profits: {max_value_conc})")
        text_file.write(f"\nGreatest Decrease in Profits: {min_value_conc})")
        text_file.close()