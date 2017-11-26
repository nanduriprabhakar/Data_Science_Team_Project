
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as plt2
get_ipython().magic('matplotlib inline')


# In[2]:


raw_data_f1=pd.read_csv('File_1_copy.csv',index_col='time')
input_and_output_f1=pd.DataFrame(columns=['leaf1','leaf2','leaf3','leaf4','leaf5','leaf6','leaf7','leaf8','spine1','spine2','spine3','spine4'],index=raw_data_f1.index)
input_and_output_f1['leaf1']=raw_data_f1['leaf1 input packet rate']+raw_data_f1['leaf1 output packet rate']
input_and_output_f1['leaf2']=raw_data_f1['leaf2 input packet rate']+raw_data_f1['leaf2 output packet rate']
input_and_output_f1['leaf3']=raw_data_f1['leaf3 input packet rate']+raw_data_f1['leaf3 output packet rate']
input_and_output_f1['leaf4']=raw_data_f1['leaf4 input packet rate']+raw_data_f1['leaf4 output packet rate']
input_and_output_f1['leaf5']=raw_data_f1['leaf5 input packet rate']+raw_data_f1['leaf5 output packet rate']
input_and_output_f1['leaf6']=raw_data_f1['leaf6 input packet rate']+raw_data_f1['leaf6 output packet rate']
input_and_output_f1['leaf7']=raw_data_f1['leaf7 input packet rate']+raw_data_f1['leaf7 output packet rate']
input_and_output_f1['leaf8']=raw_data_f1['leaf8 input packet rate']+raw_data_f1['leaf8 output packet rate']
input_and_output_f1['spine1']=raw_data_f1['spine1 input packet rate']+raw_data_f1['spine1 output packet rate']
input_and_output_f1['spine2']=raw_data_f1['spine2 input packet rate']+raw_data_f1['spine2 output packet rate']
input_and_output_f1['spine3']=raw_data_f1['spine3 input packet rate']+raw_data_f1['spine3 output packet rate']
input_and_output_f1['spine4']=raw_data_f1['spine4 input packet rate']+raw_data_f1['spine4 output packet rate']
raw_data_f2=pd.read_csv('File_2_copy.csv',index_col='time')
input_and_output_f2=pd.DataFrame(columns=['leaf1','leaf2','leaf3','leaf4','leaf5','leaf6','leaf7','leaf8','spine1','spine2','spine3','spine4'],index=raw_data_f2.index)
input_and_output_f2['leaf1']=raw_data_f2['leaf1 input packet rate']+raw_data_f2['leaf1 output packet rate']
input_and_output_f2['leaf2']=raw_data_f2['leaf2 input packet rate']+raw_data_f2['leaf2 output packet rate']
input_and_output_f2['leaf3']=raw_data_f2['leaf3 input packet rate']+raw_data_f2['leaf3 output packet rate']
input_and_output_f2['leaf4']=raw_data_f2['leaf4 input packet rate']+raw_data_f2['leaf4 output packet rate']
input_and_output_f2['leaf5']=raw_data_f2['leaf5 input packet rate']+raw_data_f2['leaf5 output packet rate']
input_and_output_f2['leaf6']=raw_data_f2['leaf6 input packet rate']+raw_data_f2['leaf6 output packet rate']
input_and_output_f2['leaf7']=raw_data_f2['leaf7 input packet rate']+raw_data_f2['leaf7 output packet rate']
input_and_output_f2['leaf8']=raw_data_f2['leaf8 input packet rate']+raw_data_f2['leaf8 output packet rate']
input_and_output_f2['spine1']=raw_data_f2['spine1 input packet rate']+raw_data_f2['spine1 output packet rate']
input_and_output_f2['spine2']=raw_data_f2['spine2 input packet rate']+raw_data_f2['spine2 output packet rate']
input_and_output_f2['spine3']=raw_data_f2['spine3 input packet rate']+raw_data_f2['spine3 output packet rate']
input_and_output_f2['spine4']=raw_data_f2['spine4 input packet rate']+raw_data_f2['spine4 output packet rate']
raw_data_f3=pd.read_csv('File_3_copy.csv',index_col='time')
input_and_output_f3=pd.DataFrame(columns=['leaf1','leaf2','leaf3','leaf4','leaf5','leaf6','leaf7','leaf8','spine1','spine2','spine3','spine4'],index=raw_data_f3.index)
input_and_output_f3['leaf1']=raw_data_f3['leaf1 input packet rate']+raw_data_f3['leaf1 output packet rate']
input_and_output_f3['leaf2']=raw_data_f3['leaf2 input packet rate']+raw_data_f3['leaf2 output packet rate']
input_and_output_f3['leaf3']=raw_data_f3['leaf3 input packet rate']+raw_data_f3['leaf3 output packet rate']
input_and_output_f3['leaf4']=raw_data_f3['leaf4 input packet rate']+raw_data_f3['leaf4 output packet rate']
input_and_output_f3['leaf5']=raw_data_f3['leaf5 input packet rate']+raw_data_f3['leaf5 output packet rate']
input_and_output_f3['leaf6']=raw_data_f3['leaf6 input packet rate']+raw_data_f3['leaf6 output packet rate']
input_and_output_f3['leaf7']=raw_data_f3['leaf7 input packet rate']+raw_data_f3['leaf7 output packet rate']
input_and_output_f3['leaf8']=raw_data_f3['leaf8 input packet rate']+raw_data_f3['leaf8 output packet rate']
input_and_output_f3['spine1']=raw_data_f3['spine1 input packet rate']+raw_data_f3['spine1 output packet rate']
input_and_output_f3['spine2']=raw_data_f3['spine2 input packet rate']+raw_data_f3['spine2 output packet rate']
input_and_output_f3['spine3']=raw_data_f3['spine3 input packet rate']+raw_data_f3['spine3 output packet rate']
input_and_output_f3['spine4']=raw_data_f3['spine4 input packet rate']+raw_data_f3['spine4 output packet rate']


# In[3]:


means_for_file1=[0]
for i in input_and_output_f1.columns:
    temp_df=input_and_output_f1[[i]].dropna()
    temp_df.plot(temp_df.index,i)
    means_for_file1.append(input_and_output_f1[[i]].dropna().mean())


# In[4]:


means_for_file2=[0]
for i in input_and_output_f2.columns:
    temp_df=input_and_output_f2[[i]].dropna()
    temp_df.plot(temp_df.index,i)
    means_for_file2.append(input_and_output_f2[[i]].dropna().mean()) 


# In[5]:


means_for_file3=[0]
for i in input_and_output_f3.columns:
    temp_df=input_and_output_f3[[i]].dropna()
    temp_df.plot(temp_df.index,i)
    means_for_file3.append(input_and_output_f3[[i]].dropna().mean())


# Oberservations from initial data analysis of all the three training files
# 1. File1 - One leaf fails (Leaf6)
# 2. File2 - Normal Operation
# 3. File3 - One Spine fails(Spine2)
# 
# We need to take into consideration the considerable amount of falls in both the input and output packet rates to completely determine whether the element has fallen or not. Just by looking at one parameter(say only input packet rate) we can not be completely sure whether that network element has failed or not.[Case of Spine1 in File3]

# ASSUMPTION: Both input packet rate and output packet rate have equal weightage/importance in determining whether the particular network element has failed or not. There is a linear relationship between the percentage increase or decrease of the packet rate data with change in probability of failure.  

# In[6]:


means_for_file2


# In[7]:


percentage_change_for_file1_leaf1=[0]
i=0
while i < max(input_and_output_f1['leaf1'].dropna().index):
    for j in input_and_output_f1['leaf1'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file1_leaf1.append(((means_for_file2[1]-input_and_output_f1.leaf1.dropna().loc[i:j].mean())/means_for_file2[1])*100)
            break
    i=j


# In[8]:


percentage_change_for_file1_leaf2=[0]
i=0
while i < max(input_and_output_f1['leaf2'].dropna().index):
    for j in input_and_output_f1['leaf2'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file1_leaf2.append(((means_for_file2[2]-input_and_output_f1.leaf2.dropna().loc[i:j].mean())/means_for_file2[2])*100)
            break
    i=j


# In[9]:


percentage_change_for_file1_leaf3=[0]
i=0
while i < max(input_and_output_f1['leaf3'].dropna().index):
    for j in input_and_output_f1['leaf3'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file1_leaf3.append(((means_for_file2[3]-input_and_output_f1.leaf3.dropna().loc[i:j].mean())/means_for_file2[3])*100)
            break
    i=j


# In[10]:


percentage_change_for_file1_leaf4=[0]
i=0
while i < max(input_and_output_f1['leaf4'].dropna().index):
    for j in input_and_output_f1['leaf4'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file1_leaf4.append(((means_for_file2[4]-input_and_output_f1.leaf4.dropna().loc[i:j].mean())/means_for_file2[4])*100)
            break
    i=j


# In[11]:


percentage_change_for_file1_leaf5=[0]
i=0
while i < max(input_and_output_f1['leaf5'].dropna().index):
    for j in input_and_output_f1['leaf5'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file1_leaf5.append(((means_for_file2[5]-input_and_output_f1.leaf5.dropna().loc[i:j].mean())/means_for_file2[5])*100)
            break
    i=j


# In[12]:


percentage_change_for_file1_leaf6=[0]
i=0
while i < max(input_and_output_f1['leaf6'].dropna().index):
    for j in input_and_output_f1['leaf6'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file1_leaf6.append(((means_for_file2[6]-input_and_output_f1.leaf6.dropna().loc[i:j].mean())/means_for_file2[6])*100)
            break
    i=j


# In[13]:


percentage_change_for_file1_leaf7=[0]
i=0
while i < max(input_and_output_f1['leaf7'].dropna().index):
    for j in input_and_output_f1['leaf7'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file1_leaf7.append(((means_for_file2[7]-input_and_output_f1.leaf7.dropna().loc[i:j].mean())/means_for_file2[7])*100)
            break
    i=j


# In[14]:


percentage_change_for_file1_leaf8=[0]
i=0
while i < max(input_and_output_f1['leaf8'].dropna().index):
    for j in input_and_output_f1['leaf8'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file1_leaf8.append(((means_for_file2[8]-input_and_output_f1.leaf8.dropna().loc[i:j].mean())/means_for_file2[8])*100)
            break
    i=j


# In[15]:


percentage_change_for_file1_spine1=[0]
i=0
while i < max(input_and_output_f1['spine1'].dropna().index):
    for j in input_and_output_f1['spine1'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file1_spine1.append(((means_for_file2[9]-input_and_output_f1.spine1.dropna().loc[i:j].mean())/means_for_file2[9])*100)
            break
    i=j


# In[16]:


percentage_change_for_file1_spine2=[0]
i=0
while i < max(input_and_output_f1['spine2'].dropna().index):
    for j in input_and_output_f1['spine2'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file1_spine2.append(((means_for_file2[10]-input_and_output_f1.spine2.dropna().loc[i:j].mean())/means_for_file2[10])*100)
            break
    i=j


# In[17]:


percentage_change_for_file1_spine3=[0]
i=0
while i < max(input_and_output_f1['spine3'].dropna().index):
    for j in input_and_output_f1['spine3'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file1_spine3.append(((means_for_file2[11]-input_and_output_f1.spine3.dropna().loc[i:j].mean())/means_for_file2[11])*100)
            break
    i=j


# In[18]:


percentage_change_for_file1_spine4=[0]
i=0
while i < max(input_and_output_f1['spine4'].dropna().index):
    for j in input_and_output_f1['spine4'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file1_spine4.append(((means_for_file2[12]-input_and_output_f1.spine4.dropna().loc[i:j].mean())/means_for_file2[12])*100)
            break
    i=j


# In[19]:


percentage_change_for_file1=[percentage_change_for_file1_leaf1,percentage_change_for_file1_leaf2,percentage_change_for_file1_leaf3,percentage_change_for_file1_leaf4,percentage_change_for_file1_leaf5,percentage_change_for_file1_leaf6,percentage_change_for_file1_leaf7,percentage_change_for_file1_leaf8,percentage_change_for_file1_spine1,percentage_change_for_file1_spine2,percentage_change_for_file1_spine3,percentage_change_for_file1_spine4]


# In[20]:


percentage_change_for_file1


# In[21]:


percentage_change_for_file2_leaf1=[0]
i=0
while i < max(input_and_output_f2['leaf1'].dropna().index):
    for j in input_and_output_f2['leaf1'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file2_leaf1.append(((means_for_file2[1]-input_and_output_f2.leaf1.dropna().loc[i:j].mean())/means_for_file2[1])*100)
            break
    i=j

percentage_change_for_file2_leaf2=[0]
i=0
while i < max(input_and_output_f2['leaf2'].dropna().index):
    for j in input_and_output_f2['leaf2'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file2_leaf2.append(((means_for_file2[2]-input_and_output_f2.leaf2.dropna().loc[i:j].mean())/means_for_file2[2])*100)
            break
    i=j

percentage_change_for_file2_leaf3=[0]
i=0
while i < max(input_and_output_f2['leaf3'].dropna().index):
    for j in input_and_output_f2['leaf3'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file2_leaf3.append(((means_for_file2[3]-input_and_output_f2.leaf3.dropna().loc[i:j].mean())/means_for_file2[3])*100)
            break
    i=j

percentage_change_for_file2_leaf4=[0]
i=0
while i < max(input_and_output_f2['leaf4'].dropna().index):
    for j in input_and_output_f2['leaf4'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file2_leaf4.append(((means_for_file2[4]-input_and_output_f2.leaf4.dropna().loc[i:j].mean())/means_for_file2[4])*100)
            break
    i=j 

percentage_change_for_file2_leaf5=[0]
i=0
while i < max(input_and_output_f2['leaf5'].dropna().index):
    for j in input_and_output_f2['leaf5'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file2_leaf5.append(((means_for_file2[5]-input_and_output_f2.leaf5.dropna().loc[i:j].mean())/means_for_file2[5])*100)
            break
    i=j

percentage_change_for_file2_leaf6=[0]
i=0
while i < max(input_and_output_f2['leaf6'].dropna().index):
    for j in input_and_output_f2['leaf6'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file2_leaf6.append(((means_for_file2[6]-input_and_output_f2.leaf6.dropna().loc[i:j].mean())/means_for_file2[6])*100)
            break
    i=j

percentage_change_for_file2_leaf7=[0]
i=0
while i < max(input_and_output_f2['leaf7'].dropna().index):
    for j in input_and_output_f2['leaf7'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file2_leaf7.append(((means_for_file2[7]-input_and_output_f2.leaf7.dropna().loc[i:j].mean())/means_for_file2[7])*100)
            break
    i=j

percentage_change_for_file2_leaf8=[0]
i=0
while i < max(input_and_output_f2['leaf8'].dropna().index):
    for j in input_and_output_f2['leaf8'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file2_leaf8.append(((means_for_file2[8]-input_and_output_f2.leaf8.dropna().loc[i:j].mean())/means_for_file2[8])*100)
            break
    i=j

percentage_change_for_file2_spine1=[0]
i=0
while i < max(input_and_output_f2['spine1'].dropna().index):
    for j in input_and_output_f2['spine1'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file2_spine1.append(((means_for_file2[9]-input_and_output_f2.spine1.dropna().loc[i:j].mean())/means_for_file2[9])*100)
            break
    i=j

percentage_change_for_file2_spine2=[0]
i=0
while i < max(input_and_output_f2['spine2'].dropna().index):
    for j in input_and_output_f2['spine2'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file2_spine2.append(((means_for_file2[10]-input_and_output_f2.spine2.dropna().loc[i:j].mean())/means_for_file2[10])*100)
            break
    i=j

percentage_change_for_file2_spine3=[0]
i=0
while i < max(input_and_output_f2['spine3'].dropna().index):
    for j in input_and_output_f2['spine3'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file2_spine3.append(((means_for_file2[11]-input_and_output_f2.spine3.dropna().loc[i:j].mean())/means_for_file2[11])*100)
            break
    i=j

percentage_change_for_file2_spine4=[0]
i=0
while i < max(input_and_output_f2['spine4'].dropna().index):
    for j in input_and_output_f2['spine4'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file2_spine4.append(((means_for_file2[12]-input_and_output_f2.spine4.dropna().loc[i:j].mean())/means_for_file2[12])*100)
            break
    i=j    

percentage_change_for_file2=[percentage_change_for_file2_leaf1,percentage_change_for_file2_leaf2,percentage_change_for_file2_leaf3,percentage_change_for_file2_leaf4,percentage_change_for_file2_leaf5,percentage_change_for_file2_leaf6,percentage_change_for_file2_leaf7,percentage_change_for_file2_leaf8,percentage_change_for_file2_spine1,percentage_change_for_file2_spine2,percentage_change_for_file2_spine3,percentage_change_for_file2_spine4]    


# In[22]:


percentage_change_for_file2


# In[23]:


percentage_change_for_file3_leaf1=[0]
i=0
while i < max(input_and_output_f3['leaf1'].dropna().index):
    for j in input_and_output_f3['leaf1'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file3_leaf1.append(((means_for_file2[1]-input_and_output_f3.leaf1.dropna().loc[i:j].mean())/means_for_file2[1])*100)
            break
    i=j

percentage_change_for_file3_leaf2=[0]
i=0
while i < max(input_and_output_f3['leaf2'].dropna().index):
    for j in input_and_output_f3['leaf2'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file3_leaf2.append(((means_for_file2[2]-input_and_output_f3.leaf2.dropna().loc[i:j].mean())/means_for_file2[2])*100)
            break
    i=j

percentage_change_for_file3_leaf3=[0]
i=0
while i < max(input_and_output_f3['leaf3'].dropna().index):
    for j in input_and_output_f3['leaf3'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file3_leaf3.append(((means_for_file2[3]-input_and_output_f3.leaf3.dropna().loc[i:j].mean())/means_for_file2[3])*100)
            break
    i=j

percentage_change_for_file3_leaf4=[0]
i=0
while i < max(input_and_output_f3['leaf4'].dropna().index):
    for j in input_and_output_f3['leaf4'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file3_leaf4.append(((means_for_file2[4]-input_and_output_f3.leaf4.dropna().loc[i:j].mean())/means_for_file2[4])*100)
            break
    i=j 

percentage_change_for_file3_leaf5=[0]
i=0
while i < max(input_and_output_f3['leaf5'].dropna().index):
    for j in input_and_output_f3['leaf5'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file3_leaf5.append(((means_for_file2[5]-input_and_output_f3.leaf5.dropna().loc[i:j].mean())/means_for_file2[5])*100)
            break
    i=j

percentage_change_for_file3_leaf6=[0]
i=0
while i < max(input_and_output_f3['leaf6'].dropna().index):
    for j in input_and_output_f3['leaf6'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file3_leaf6.append(((means_for_file2[6]-input_and_output_f3.leaf6.dropna().loc[i:j].mean())/means_for_file2[6])*100)
            break
    i=j

percentage_change_for_file3_leaf7=[0]
i=0
while i < max(input_and_output_f3['leaf7'].dropna().index):
    for j in input_and_output_f3['leaf7'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file3_leaf7.append(((means_for_file2[7]-input_and_output_f3.leaf7.dropna().loc[i:j].mean())/means_for_file2[7])*100)
            break
    i=j

percentage_change_for_file3_leaf8=[0]
i=0
while i < max(input_and_output_f3['leaf8'].dropna().index):
    for j in input_and_output_f3['leaf8'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file3_leaf8.append(((means_for_file2[8]-input_and_output_f3.leaf8.dropna().loc[i:j].mean())/means_for_file2[8])*100)
            break
    i=j

percentage_change_for_file3_spine1=[0]
i=0
while i < max(input_and_output_f3['spine1'].dropna().index):
    for j in input_and_output_f3['spine1'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file3_spine1.append(((means_for_file2[9]-input_and_output_f3.spine1.dropna().loc[i:j].mean())/means_for_file2[9])*100)
            break
    i=j

percentage_change_for_file3_spine2=[0]
i=0
while i < max(input_and_output_f3['spine2'].dropna().index):
    for j in input_and_output_f3['spine2'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file3_spine2.append(((means_for_file2[10]-input_and_output_f3.spine2.dropna().loc[i:j].mean())/means_for_file2[10])*100)
            break
    i=j

percentage_change_for_file3_spine3=[0]
i=0
while i < max(input_and_output_f3['spine3'].dropna().index):
    for j in input_and_output_f3['spine3'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file3_spine3.append(((means_for_file2[11]-input_and_output_f3.spine3.dropna().loc[i:j].mean())/means_for_file2[11])*100)
            break
    i=j

percentage_change_for_file3_spine4=[0]
i=0
while i < max(input_and_output_f3['spine4'].dropna().index):
    for j in input_and_output_f3['spine4'].dropna().index:
        if j-i > 5000000000:
            percentage_change_for_file3_spine4.append(((means_for_file2[12]-input_and_output_f3.spine4.dropna().loc[i:j].mean())/means_for_file2[12])*100)
            break
    i=j    

percentage_change_for_file3=[percentage_change_for_file3_leaf1,percentage_change_for_file3_leaf2,percentage_change_for_file3_leaf3,percentage_change_for_file3_leaf4,percentage_change_for_file3_leaf5,percentage_change_for_file3_leaf6,percentage_change_for_file3_leaf7,percentage_change_for_file3_leaf8,percentage_change_for_file3_spine1,percentage_change_for_file3_spine2,percentage_change_for_file3_spine3,percentage_change_for_file3_spine4] 


# In[24]:


percentage_change_for_file3

