#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as nm
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('customers.csv')
df


# In[5]:


df_ = df.rename(columns = {'Annual Income ($)':'annual_income','Spending Score (1-100)	':'spending_score','Work Experience	':'work_experience'},inplace = True)
df


# In[6]:


df.drop(['CustomerID'], axis=1, inplace=True)


# In[7]:


df.describe()


# In[8]:


df.isnull().sum()


# In[9]:


plt.hist(x = df['Age'])


# In[10]:


sns.countplot(x= df['Gender'])


# In[11]:


plt.hist(x = df['annual_income'])


# In[12]:


df[df['annual_income'] == 0]


# In[13]:


df['annual_income'].mean()


# In[15]:


df.loc[df['annual_income'] == 0, 'annual_income'] = 110731.8215


# In[17]:


df.loc[df['annual_income'] == 110731.8215]


# In[18]:


plt.hist(x = df['annual_income'])


# In[19]:


import plotly.express as px


# In[22]:


chart =  px.scatter_matrix(df, dimensions=['Profession', 'annual_income', 'Family Size', 'Work Experience'], color='Spending Score (1-100)')
chart.show()


# In[24]:


chart = px.parallel_categories(df, dimensions=['Family Size', 'Profession'],
                                 title='Parallel of the family size and profession of customers',)
chart.show()


# In[26]:


df.loc[df['Profession'].isin(['Artist'])]


# In[28]:


prof = df['Profession'].value_counts()
prof.plot.barh(figsize=(15,7), xlabel='Profession', title='Counting by Profession')


# In[29]:


prof = df['Profession'].value_counts() / 2000
prof.plot.barh(figsize=(15,7), xlabel='Profession', title='Percents by Profession')


# In[ ]:




