#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
files=["january.xlsx","february.xlsx",'march.xlsx']
#files.append('April.xlsx')
print(type(files))

combined=pd.DataFrame()

for file in files:
    df=pd.read_excel(file,skiprows=3)
    combined=combined.append(df,ignore_index=True)
    
    
combined.to_excel("combined.xlsx")


# In[40]:


import pandas as pd
files=input("Enter the months filename:")
print(list(files.split()))


# In[ ]:


empty=pd.DataFrame()
empty.append(jandf,febdf)
empty.to_excel("requo.lxs",index=False)


# In[3]:


print(df) # this df belongs to last excel file


# In[6]:


df_sel1=df['Location'].isin(['Los Angeles'])
print(df_sel1)
print()
print(df[df_sel1])


# In[12]:


df_sel2=df['Location'].isin(['Los Angeles','Atlanta'])
print(df_sel2)
print(df[df_sel2])


# In[13]:


# not in
df[~df['Location'].isin(['Los Angeles','Atlanta'])]


# In[15]:


# numeric selecting
df[df['Bananas']>2258]# 


# In[16]:


df[df['Location'].map(lambda x:x.startswith('To'))]


# In[17]:


df[df['Location'].map(lambda x:x.endswith('k'))]


# In[20]:


df[df['Location'].map (lambda x:x.startswith('To')) & (df['Total']> 12900)]


# In[22]:


df[df['Location'].str.contains('o')]


# In[41]:


o_contain_name_customer_data=df[df['Location'].str.contains('o')]


# In[23]:


df['Apples'].unique()


# In[24]:


df['Apples'].nunique()


# In[27]:


# drop duplciates
df.drop_duplicates(subset=['Apples'])


# In[30]:


# sorting
df.sort_values(by=['Location'],ascending=True)


# In[31]:


df.sort_values(by=['Location'],ascending=False)


# In[35]:


df.sort_values(by=['Location','Apples'],ascending=[True,False])


# In[36]:


df.sort_index(ascending=False)


# In[37]:


df


# In[45]:


a=10
print(b)


# In[48]:


import pandas as pd
df=pd.read_excel("march.xlsx")
print(dfmutual)


# In[ ]:




