#!/usr/bin/env python
# coding: utf-8

# In[41]:


import os
import csv

# Import Files
file_path = os.path.join("election_data.csv")
output_file = os.path.join("PyPoll", "election_data.txt")

# Set File Path
output_dir = os.path.dirname(output_file)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Set Variables
total_votes = 0
candidate_votes = {}

# Read the CSV file
try:
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        for row in csvreader:
            total_votes += 1
            candidate = row[2]
            if candidate in candidate_votes:
                candidate_votes[candidate] += 1
            else:
                candidate_votes[candidate] = 1

    # Calculate Analysis
    percentage_votes = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

    # Calculate Winner
    winner = max(candidate_votes, key=candidate_votes.get)

    # Create Analysis Print
    analysis = (
        "Election Results\n"
        "-------------------------\n"
        f"Total Votes: {total_votes}\n"
        "-------------------------\n"
    )
    for candidate, votes in candidate_votes.items():
        analysis += f"{candidate}: {percentage_votes[candidate]:.3f}% ({votes})\n"
    analysis += (
        "-------------------------\n"
        f"Winner: {winner}\n"
        "-------------------------\n"
    )

except FileNotFoundError:
    print("File not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Print Analysis
print(analysis)

# Write Analysis to Output File
with open(output_file, "w") as file:
    file.write(analysis)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[37]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




