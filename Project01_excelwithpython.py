#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df1=pd.read_excel("movies.xls")
#print(df1)


# In[2]:


print(df1.head())


# In[3]:


# reading only sheet0 , first sheet.
df_sheetfirst=pd.read_excel('movies.xls',sheet_name=0)
df_sheetfirst.head()
#TRY TO READ NEXT SHEETS.


# In[4]:


sheetfirst=pd.read_excel("movies.xls",sheet_name=0)
sheetsecond=pd.read_excel("movies.xls",sheet_name=1)
sheetthird=pd.read_excel("movies.xls",sheet_name=2)


# In[5]:


print(sheetfirst.shape,sheetsecond.shape,sheetthird.shape)


# In[6]:


# MAKING ALL THREE SHEETS INTO ONE SHEETS
finalexcel=pd.concat([sheetfirst,sheetsecond,sheetthird])
print(finalexcel.columns)


# In[7]:


print(finalexcel.shape)
# NUMBER OF ROWS IT GOT INCREASED.


# In[8]:


# exploring the data


# In[36]:


print(finalexcel.head())
print(finalexcel.tail())


# In[10]:


finalexcel.info()


# In[ ]:


finalexcel.dropna()
finalexcel.fillna('9999')
finalexcel.fillna(method=ffill)
finalexcel.fillna(method=bfill)


# In[38]:


# sorting the dataframe.
sorted_by_gross=finalexcel.sort_values(['Gross Earnings'],ascending=False)


# In[39]:


# print / fetch top 10 movies whos revence is top 10.
sorted_by_gross['Gross Earnings'].head(10)


# In[40]:


sorted_by_gross.head(5)


# In[13]:


print(finalexcel.columns)


# In[14]:


print(sorted_by_gross.head(5))


# In[15]:


# visualization of data.
import matplotlib.pyplot as plt
sorted_by_gross['Gross Earnings'].head(10).plot(kind='barh')
plt.show()


# In[42]:


import matplotlib.pyplot as plt


labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 35, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]
men_std = [2, 3, 4, 1, 2]
women_std = [3, 5, 2, 3, 3]
width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(labels, men_means, width, yerr=men_std, label='Men')
ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
       label='Women')

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.legend()
plt.savefig("dsas.png")
plt.show()


# In[16]:


import matplotlib.pyplot as plt
sorted_by_gross['Gross Earnings'].head(10).plot(kind='bar')
plt.show()


# In[17]:


#different column plot.
finalexcel['IMDB Score'].plot(kind='hist')
plt.show()


# In[18]:


#statistical info.
finalexcel.describe()


# In[43]:


finalexcel[finalexcel['Year']==1916]


# In[19]:


print("MIN:",finalexcel['Duration'].min())
print("MAX:",finalexcel['Duration'].max())
print("STD:",finalexcel['Duration'].std())
print("MEAN:",finalexcel['Duration'].mean())
print("MEDIAN:",finalexcel['Duration'].median())
print("MODE:",finalexcel['Duration'].mode())


# In[20]:


print(finalexcel.corr())


# In[21]:


print(finalexcel['Budget'].corr(finalexcel['Gross Earnings']))


# In[22]:


# parse_cols=6  means read first 6 rows.
#By passing parse_cols=6, we are telling the read_excel method to read only the first columns till index six or first seven columns (the first column being indexed zero).
df_subset=pd.read_excel("movies.xls")
print(df_subset.columns)


# In[23]:


df_subset['Net Earnings']=df_subset['Gross Earnings']-df_subset['Budget']
print(df_subset.head(2))


# In[24]:


print(df_subset.columns)


# In[25]:


# sorting the data according to net earning columns
sorted_movies=df_subset[['Net Earnings']].sort_values(['Net Earnings'],ascending=[False])
sorted_movies.head(10)['Net Earnings'].plot.bar()
plt.show()


# In[26]:


#pivot table 
df2_subset=df_subset[['Year','Gross Earnings']]
df2_subset.head()


# In[27]:


earning_by_year=df2_subset.pivot_table(index=['Year'])
earning_by_year.head()


# In[28]:


earning_by_year=df2_subset.pivot_table(index=['Year'],aggfunc='sum')
earning_by_year.head()


# In[29]:


earning_by_year.plot()


# In[30]:


earning_by_year.plot.hist()
plt.show()


# In[31]:


df3=finalexcel[['Country','Language','Gross Earnings']]
df3.head()


# In[32]:


earnings_by_co_lang=df3.pivot_table(index=['Country','Language'])
earnings_by_co_lang.head(3)


# In[33]:


earnings_by_co_lang.head(20).plot(kind='bar',figsize=(20,8))
plt.show()


# In[34]:


df3.to_excel("newsubsetexcel.xlsx")


# In[35]:


df3.to_excel('withindexindex.xlsx',index=False)


# In[ ]:




