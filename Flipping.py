#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np


# In[1]:


def Left(arr,token):
    i = len(arr)
    length = len(arr)
    for index in token:
         index = int(index)
         a = np.flip(arr[length-i,:index+1])
         b = np.flip(arr[length-i,index+1:])
         arr[length-i,:] = np.concatenate((a,b))
         i = i - 1
    return arr


# In[2]:


def Up(arr,token):
    i = len(arr)
    length = len(arr)
    for index in token:
         index = int(index)
         a = np.flip(arr[:index+1,length-i])
         b = np.flip(arr[index+1:,length-i])
         arr[:,length-i] = np.concatenate((a,b))
         i = i - 1
    return arr


# In[3]:


def Right(arr,token):
    i = len(arr)
    length = len(arr)
    for index in token:
         index = int(index)
         index = length - index
         a = np.flip(arr[length-i,:index-1])
         b = np.flip(arr[length-i,index-1:])
         arr[length-i,:] = np.concatenate((a,b))
         i = i - 1
    return arr


# In[4]:


def Down(arr,token):
    i = len(arr)
    length = len(arr)
    for index in token:
         index = int(index)
         index = length - index
         a = np.flip(arr[:index-1,length-i])
         b = np.flip(arr[index-1:,length-i])
         arr[:,length-i] = np.concatenate((a,b))
         i = i - 1
    return arr


# In[ ]:




