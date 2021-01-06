#!/usr/bin/env python
# coding: utf-8

# In[13]:


import json
import pandas as pd
import requests

r = requests.get('http://dataservices.imf.org/REST/SDMX_JSON.svc/Dataflow')

datasets = r.json()
#print(datasets)
#type(datasets)


# In[2]:


# this just converts to json format 
#data  = json.dumps(datasets) 
#print(data)
list(datasets)


# In[3]:


data = json.dumps(datasets, indent=2)
print(data)


# In[4]:


type(data)


# In[5]:


print(data[0][0]) 


# In[6]:


print(len(data))


# In[7]:


for item in data['Structure'][0]:
   print(item)


# In[8]:


type(data)


# In[9]:


def getList(data): 
    return data.keys()

print(getList(data))


# In[10]:


def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield from recursive_items(value)
        else:
            yield (key, value)

for key, value in recursive_items(data):
    print(key, value)


# In[11]:


import json

from urllib.request import urlopen

with urlopen("http://dataservices.imf.org/REST/SDMX_JSON.svc/Dataflow") as response:
    source = response.read()
    
print(source)


# In[12]:


url = 'http://dataservices.imf.org/REST/SDMX_JSON.svc/'
key = 'Dataflow'  # Method with series information
#search_term = 'Trade'  # Term to find in series names
series_list = requests.get(f'{url}{key}').json()            ['Structure']['Dataflows']['Dataflow']
# Use dict keys to navigate through results:
#for series in series_list:
#    if search_term in series['Name']['#text']:
#        print(f"{series['Name']['#text']}: {series['KeyFamilyRef']['KeyFamilyID']}")

for item in series_list['Name']['#text']:
    print(f"{series['Name']['#text']}: {series['KeyFamilyRef']['KeyFamilyID']}")


# In[ ]:


print(series_list)


# In[ ]:


newdata = json.dumps(series_list, indent=2)
print(newdata)


# In[ ]:


type(newdata)


# In[ ]:


datanewnew = json.loads(newdata)

print(datanewnew)


# In[ ]:


for item in datanewnew['id']['Name']:
   print(item)


# In[ ]:




