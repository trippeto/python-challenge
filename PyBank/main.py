#!/usr/bin/env python
# coding: utf-8

# In[43]:


import os
import csv

inpath = os.path.join('Resources', 'budget_data.csv')
outpath = os.path.join('Analysis', 'Financial_Analysis.txt')


# In[44]:


month_count = 0
total_PnL = 0
PnL_change_list = []
month_of_change = []

with open(inpath, 'r') as infile, open(outpath, 'w') as outfile:

    reader = csv.reader(infile, delimiter = ',')  
    header = next(reader)
    writer = csv.writer(outfile)
    
    first_row = next(reader)
    month_count += 1 
    total_PnL += int(first_row[1])
    prev_row = int(first_row[1])
    
    for row in reader:
        
        month_count += 1
        
        total_PnL += int(row[1])        
        
        PnL_change = int(row[1]) - prev_row        
        prev_row = int(row[1])        
        PnL_change_list.append(PnL_change)
        month_of_change.append(row[0])
        avg_change = sum(PnL_change_list)/len(PnL_change_list)
    
    writer.writerow(['Financial Analysis'])
    writer.writerow(['---------------------------'])
    writer.writerow(['Total Months: ' + f'{month_count}'])
    writer.writerow(['Total: ' + f'${total_PnL}'])
    writer.writerow(['Average Change: ' f'${(avg_change):.2f}'])
    writer.writerow(['Greatest Increase in Profits: ' + month_of_change[PnL_change_list.index(max(PnL_change_list))] + " " + f'(${max(PnL_change_list)})'])
    writer.writerow(['Greatest Decrease in Profits: ' + month_of_change[PnL_change_list.index(min(PnL_change_list))] + " " + f'(${min(PnL_change_list)})'])

print('Financial Analysis')
print('---------------------------')
print('Total Months: ', month_count)
print('Total: ', f'${total_PnL}')
print('Average Change: ', f'${(avg_change):.2f}')
print('Greatest Increase in Profits: ', month_of_change[PnL_change_list.index(max(PnL_change_list))], f'(${max(PnL_change_list)})')
print('Greatest Decrease in Profits: ', month_of_change[PnL_change_list.index(min(PnL_change_list))], f'(${min(PnL_change_list)})')


# In[ ]:




