#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import dependencies
import pandas as pd


# In[2]:


csvPath = "../Resources/election_data.csv"
df = pd.read_csv(csvPath)


# In[3]:


# A complete list of candidates who received votes
candidates = df["Candidate"].unique()


# In[4]:


# The total number of votes cast
votes = len(df)


# In[5]:


# Lets sort
candidates = df["Candidate"].value_counts().to_dict()


# In[21]:


# print text
ln = [
    "Election Results",
    ('-'*25),
f'Total Votes: {votes}',
    ('-'*25),
    
]
winner = [0,""]
for can, vote in candidates.items():
    ln.append(f'{can}: {vote/votes*100:.3f}% ({vote})')
    if (winner[0]< vote):
        winner[0]=vote
        winner[1]=can
ln += [('-'*25)] 
ln += [f'Winner: {winner[1]}']
print(ln
    )


# In[26]:


# text file export
with open('electionResults.txt', 'w') as f:
    f.write('\n'.join(ln))


# In[ ]:




