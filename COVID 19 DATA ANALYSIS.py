#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[7]:


data = pd.read_csv("4. covid_19_data.csv")


# In[10]:


data


# In[11]:


#1.
#df.count
#df.isnull


# In[15]:


# number of non null values in every coloums
data.count()#removes null values


# In[19]:


data.isnull()


# In[21]:


data.isnull().sum()
#inference:
# most of the null values are present in state column


# In[22]:


#2.
#import seaborn as sns
#import matplotlib.pyplot as plt
#sns.heatmap(df.isnull())
#plt.show()


# In[23]:


import seaborn as sns


# In[25]:


sns.heatmap(data.isnull())
plt.show()


# In[52]:


x  = data.Region
y = data.Confirmed
plt.bar(x,y)
plt.title("Region VS conformed covid cases")
plt.show()


# In[26]:


#number of conformed , death and recovered


# In[27]:


data


# In[32]:


data.groupby('Region').sum().head()


# In[35]:


#conformed cases


# In[41]:


data.groupby("Region")['Confirmed'].sum().sort_values(ascending = False).head(20)


# In[42]:


data.groupby("Region")['Confirmed','Recovered'].sum()


# In[53]:


data


# In[55]:


data.groupby("Region")["Deaths"].sum()


# In[61]:


# Removeing all the records where Confirmed cases are less than 10

data  = data[~(data.Confirmed < 10)]
data


# In[62]:


g = data.groupby('Region')


# In[64]:


for region , region_df in g:
    print(region)
    print(region_df)
    
    
    # here key is region and value is region_df


# In[66]:


# Acessing specific data frame 
g.get_group("Netherlands")


# In[67]:


# getting maximum values of each group


# In[71]:


g.max()


# In[77]:


# minimum number of deaths
data.groupby("Region").Deaths.sum().sort_values(ascending  = True).head(50)


# In[ ]:




