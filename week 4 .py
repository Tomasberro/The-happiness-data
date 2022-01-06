
# coding: utf-8

# In[11]:


import pandas as pd
data = pd.read_csv('happyscore_income.csv')
data


# In[2]:


import pandas as pd
data = pd.read_csv('happyscore_income.csv')
print(data)


# In[7]:



happy = data['happyScore']
income = data ['avg_income' ]
print(happy.min())
print(happy.max())
print(income.min())
income.max()


# In[10]:


import matplotlib.pyplot as plt
plt.xlabel('income')
plt.ylabel('happyScore')
plt.scatter(income, happy)


# In[13]:


data.sort_values('avg_income', inplace = True)

data


# In[14]:


data.sort_values('avg_income', inplace = True)

richest = data[ data [ 'avg_income']> 15000]
richest


# In[16]:


data.sort_values('avg_income', inplace = True)

richest = data[ data [ 'avg_income']> 15000]
richest.iloc[0]


# In[17]:


richest.iloc[-1]


# In[18]:


richest.iloc[0:5]


# In[19]:


import numpy as np

data.sort_values('avg_income', inplace = True)

richest = data[ data [ 'avg_income']> 15000]

rich_mean = np.mean(richest['avg_income'])

all_mean = np.mean(data['avg_income'])
print(all_mean, rich_mean)


# In[23]:


plt.scatter(richest['avg_income'], richest['happyScore'])

plt.text(richest.iloc[0]['avg_income'], richest.iloc[0]['happyScore'], richest.iloc[0]['country'])

plt.text(richest.iloc[-1]['avg_income'], richest.iloc[-1]['happyScore'], richest.iloc[-1]['country'])


# In[25]:


for k, row in richest.iterrows() :
    print(row['country'])


# In[26]:


plt.scatter(richest['avg_income'], richest['happyScore'])
for k, row in richest.iterrows() :
    plt.text(row['avg_income'], row['happyScore'], row['country'])
    #print (row['country'])


# In[27]:


ineq = data['income_inequality']
plt.scatter(income, ineq )


# In[29]:


plt.scatter(ineq, happy, s= ineq * 10 , alpha= 0.25)


# In[33]:


from sklearn.cluster import KMeans

income_happy = np.column_stack((income, happy))
# print(income_happy)
km_res = KMeans( n_clusters = 3).fit(income_happy)
km_res.cluster_centers_


# In[35]:


clusters = km_res.cluster_centers_
plt.scatter(clusters[:, 0], clusters[:, 1], s=1000)
plt.scatter(income, happy)


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('happyscore_income.csv')
avg_satisfaction = data['avg_satisfaction']
GDP = data ['GDP']
plt.xlabel('avg_satisfaction')
plt.ylabel('GDP')
plt.scatter(avg_satisfaction, GDP)


# In[10]:


data.sort_values('avg_satisfaction', inplace = True)

moreSatisf = data[ data [ 'avg_satisfaction']> 7]
moreSatisf


# In[18]:


plt.xlabel('avg_satisfaction')
plt.ylabel('GDP')
plt.scatter(moreSatisf['avg_satisfaction'], moreSatisf['GDP'])

for k, row in moreSatisf.iterrows() :
    plt.text(row['avg_satisfaction'], row['GDP'], row['country'], fontsize= 8)
    #print (row['country'])


# - I decided to graph the average satisfaction of each country compared to the respective GDP, to see if a higher level of satisfaction corresponded to a higher level of GDP for each country;
# - First, order the data by level of satisfaction from lowest to highest, and then filter the countries with an average satisfaction greater than 7;
# - The interesting thing about the labeled points is to see how Countries like Costa Rica and Mexico have a high satisfaction average and a relatively low GDP; on the contrary, the United Kingdom and the United States have a lower level of satisfaction and a relatively high GDP
