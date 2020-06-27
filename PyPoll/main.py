#!/usr/bin/env python
# coding: utf-8

# In[96]:


import os
import csv

inpath = os.path.join('Resources', 'election_data.csv')
outpath = os.path.join('Analysis', 'Election_Results.txt')


# In[101]:


tot_votes = 0 
election_data = {}

with open(inpath, 'r') as infile, open (outpath, 'w') as outfile:
    
    reader = csv.reader(infile, delimiter = ',')
    header = next(reader)
    writer = csv.writer(outfile)
    
    for row in reader:
        
        tot_votes += 1
        election_data[row[2]] = election_data.get(row[2], 0) + 1
        
    writer.writerow(['Election Results'])
    writer.writerow(['-------------------------'])
    writer.writerow(['Total Votes: ' + f'{tot_votes}'])
    writer.writerow(['-------------------------'])
        
    print('Election Results')
    print('-------------------------')
    print('Total Votes: ' + f'{tot_votes}')
    print('-------------------------')
        
    for key, value in election_data.items(): 
        percent_votes = (value/tot_votes) * 100        
        writer.writerow([f'{key}' + ': ' + f'{(percent_votes):.3f}%' + ' ' + f'({value})'])
        print(str(key) + ': ' + f'{(percent_votes):.3f}%' + ' ' + f'({value})')
        max_votes = max(election_data, key=election_data.get)  
    
    writer.writerow(['-------------------------'])
    writer.writerow(['Winner: ' + max_votes])
    writer.writerow(['-------------------------']) 
    
    print('-------------------------')
    print('Winner: ' + max_votes)
    print('-------------------------')


# In[ ]:




