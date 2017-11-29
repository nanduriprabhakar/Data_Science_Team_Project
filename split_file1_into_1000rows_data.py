
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from testing_initial_analysis import means_for_file2
get_ipython().magic('matplotlib inline')


# In[2]:


thresholds_for_disturbance=np.array([0,18.0,18.0,18.0,18.0,18.0,18.0,18.0,18.0,18.0,18.0,18.0,18.0])
thresholds_for_no_failure=np.array([0,1.67,1.52,1.66,1.59,1.67,2.34,1.96,1.75,1.77,2.02,5.27,1.99])
probabilities_df = pd.DataFrame({'No Failure':0.5*100,'leaf1':1/24*100,'leaf2':1/24*100,'leaf3':1/24*100,'leaf4':1/24*100,'leaf5':1/24*100,'leaf6':1/24*100,'leaf7':1/24*100,'leaf8':1/24*100,'spine1':1/24*100,'spine2':1/24*100,'spine3':1/24*100,'spine4':1/24*100},index=[0])


# In[3]:


bargraph=probabilities_df.iloc[-1].plot(kind='bar', title="Failure Probabilites(%)", figsize=(10,5), legend=False, fontsize=12)


# In[4]:


raw_file=pd.read_csv('file_1_copy.csv',index_col='time')


# In[5]:


for i in range(0,len(raw_file)+1,1000):
    testing_file=raw_file[i:i+1000]
    raw_data_test=testing_file
    


# In[6]:


test1=raw_file[0:1000]
test2=raw_file[1000:2000]
test3=raw_file[2000:3000]
test4=raw_file[3000:4000]
test5=raw_file[4000:5000]
test6=raw_file[5000:6000]
test7=raw_file[6000:7000]
test8=raw_file[7000:8000]
test9=raw_file[8000:9000]
test10=raw_file[9000:10000]
test11=raw_file[10000:11000]
test12=raw_file[11000:1200]
test13=raw_file[12000:13000]
test14=raw_file[13000:14000]
test15=raw_file[14000:15000]
test16=raw_file[15000:16000]
test17=raw_file[16000:17000]
test18=raw_file[17000:18000]
test19=raw_file[18000:19000]
test20=raw_file[19000:20000]
test21=raw_file[20000:21000]


# In[7]:


test21

