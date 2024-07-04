#!/usr/bin/env python
# coding: utf-8

# In[46]:
import numpy as np

def pattern():
    pattern_ID = {1:"779711611512197", 2:"7511711410997", 3:"86971149710497", 4:"78971149711510510910497", 5:"86971099711097",
           6:"8097114971151041171149710997", 7:"829710997", 8:"7511410511510411097", 9:"6697108971149710997", 10:"7597108107105"}
    num = np.random.randint(1,11)
    token = pattern_ID[num]
    return token,num

def tokkenning(t1,h,w):
    mul = h / len(t1)
    t1 = t1 + t1*(int(mul)-1)
    print(t1)
    dif = h - len(t1)
    t1 = t1 + t1[:dif]
    if h == w:
        return t1,t1
    else:
        t2 = t1
        dif = w - len(t1)
        if dif<=0:
            t2 = t2[:w] 
        else:
            t1 = t1 + t1[:dif]
        return t1,t2


# In[47]:


# Converting token to a string no
def tokenning_order(t):
    token = ""
    for i in t:
        if i >= '0' and i <= '9':
           token = token + str(i)
        else:
            token = token + str(ord(i))
    return token    


# In[52]:


def row_top_down(arr,token):
    i = len(token)
    length = len(token)
    for index in token:
        index = int(index)
        if (length-i)!=index-1:
            temp = arr[length-i,:].copy()
            arr[length-i,:] = arr[index-1,:]
            arr[index-1,:] = temp
        i = i - 1
    return arr


# In[36]:


def row_top_down_reverse(arr,token):
    i = len(token)
    length = len(token)
    for index in reversed(token):
        index = int(index)
        if (length-1)!=index-1:
            temp = arr[length-1,:].copy()
            arr[length-1,:] = arr[index-1,:]
            arr[index-1,:] = temp
        length = length - 1
    return arr

def col_left_right(arr,token):
   length = 0
   i = len(token)
   for index in token:
       index = int(index) - 1
       if length!= index:
           temp = arr[:,length].copy()
           arr[:,length] = arr[:,index]
           arr[:,index] = temp
       length = length + 1
   return arr

def col_left_right_reverse(arr,token):
   length = len(token)-1
   for index in reversed(token):
       index = int(index) - 1
       if length!= index:
           temp = arr[:,length].copy()
           arr[:,length] = arr[:,index]
           arr[:,index] = temp
       length = length - 1
   return arr