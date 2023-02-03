#!/usr/bin/env python
# coding: utf-8

# In[1]:


km = input("Enter kilometer: ")
KM = float(km)
klm = 1.61
miles = KM/klm
print("Miles: %.2f"%miles)


# In[23]:


km = input("Enter kilometer: ")
KM = float(km)
klm = 1.61
miles = KM/klm

min = 42
avem = KM/miles
print("Average time per mile in minutes: %f"%avem)

sec = 42
aves = sec/miles
print("Average time per mile in seconds: %f"%aves)

secperh = 42/60
avemph = 6.21/secperh
print("Average speed in miles per hour: %f"%avemph)


# In[ ]:




