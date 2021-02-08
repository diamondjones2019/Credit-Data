#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing data
import pandas as pd


# In[2]:


zoom = pd.read_csv('zoom.csv')


# In[13]:


zoom.describe()


# In[3]:


zoom.info()


# In[12]:


zoom.isnull()


# In[5]:


#dealing with missing values
zoom = pd.read_csv('zoom.csv', na_values='n/a')


# In[6]:


zoom.info()


# In[ ]:




