#!/usr/bin/env python
# coding: utf-8

# In[22]:


import os
import csv

# Import Files

budget_data_csv = os.path.join("budget_data.csv")
output_file = os.path.join("output", "financial_analysis.txt")

# Set File Path

output_dir = os.path.dirname(output_file)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Set Variables

total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_change_list = []
greatest_increase = ['', 0]
greatest_decrease = ['', 99999999999]

# Read CSV File

try:
    with open(budget_data_csv) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        for row in csvreader:
            total_months += 1
            total_profit_loss += int(row[1])
            profit_loss_change = int(row[1]) - previous_profit_loss
            profit_loss_change_list.append(profit_loss_change)
            previous_profit_loss = int(row[1])
            
            if profit_loss_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = profit_loss_change

            if profit_loss_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = profit_loss_change

# Calculate Analysis

    average_profit_loss_change = sum(profit_loss_change_list[1:]) / len(profit_loss_change_list[1:])

# Print Analysis

    analysis = (
        "Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_profit_loss}\n"
        f"Average Change: ${average_profit_loss_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
        f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"
    )

    print(analysis)

# Out Put

    with open(output_file, "w") as file:
        file.write(analysis)
        
# Was Getting File Not Found Error and Added This

except FileNotFoundError:
    print("File not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {str(e)}")


# In[18]:





# In[ ]:





# In[ ]:





# In[ ]:




