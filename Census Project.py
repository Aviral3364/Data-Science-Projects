
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **sports or athletics** (see below) for the region of **Lucknow, Uttar Pradesh, India**, or **India** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Lucknow, Uttar Pradesh, India** to Ann Arbor, USA. In that case at least one source file must be about **Lucknow, Uttar Pradesh, India**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Lucknow, Uttar Pradesh, India** and **sports or athletics**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **sports or athletics**?  For this category we are interested in sporting events or athletics broadly, please feel free to creatively interpret the category when building your research question!
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[50]:

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.get_backend()

#Dealing with census 2001 csv file
df = pd.read_csv('Census_2001.csv')

#Cleaning the 2001 csv file
df = df.drop(['Unnamed: 0'], axis = 1)
df1 = df[['State','District','Persons','Males','Females','Sex.ratio..females.per.1000.males.']] 
df2 = df[['State','District','Persons..literate',"Males..Literate","Females..Literate","Matric.Higher.Secondary.Diploma","Graduate.and.Above"]]
df2.rename(columns={'Persons..literate' : 'Literate', 
                    'Males..Literate' : 'Male_Literate',
                    'Females..Literate' : 'Female_Literate',
                    'Matric.Higher.Secondary.Diploma' : 'Higher_Secondary',
                    'Graduate.and.Above' : 'Graduate_and_above'}, inplace = True)
df1.rename(columns={'Sex.ratio..females.per.1000.males.' : 'Sex_Ratio'}, inplace = True)
census_2001 = pd.merge(df1, df2, on = 'District', how = 'inner')
census_2001 = census_2001.drop(['State_y'], axis=1)
census_2001.rename(columns={'State_x' : 'State'}, inplace = True)
census_2001['Literacy_Rate'] = (census_2001.Literate.astype(float) *100) / census_2001.Persons.astype(float)

#dealing with census 2011 csv file
df = pd.read_csv('Census_2011.csv')
df1 = df[['State name','District name','Population','Male','Female']]
df1['Sex_Ratio'] = (df.Female.astype(float) *1000) / df.Male.astype(float)
df1.rename(columns={'State name' : 'State',
                    'District name' : 'District',
                    'Population' : 'Persons',
                    'Male' : 'Males',
                    'Female' : 'Females'}, inplace = True)

df2 = df[['State name','District name','Literate','Male_Literate','Female_Literate','Higher_Education','Graduate_Education','Other_Education']]
df2['Graduate_and_above'] = df2.Graduate_Education.astype(float) + df2.Other_Education.astype(float)
df2 = df2.drop(['Graduate_Education','Other_Education'], axis=1)
df2.rename(columns={'State name' : 'State',
                    'District name' : 'District',
                    'Higher_Education' : 'Higher_Secondary'}, inplace = True)
census_2011 = pd.merge(df1, df2, on= 'District', how = 'inner')
census_2011 = census_2011.drop(['State_y'], axis=1)
census_2011.rename(columns={'State_x' : 'State'}, inplace = True)
census_2011['Literacy_Rate'] = (census_2011.Literate.astype(float) *100) / census_2011.Persons.astype(float)

#Now cleaning of the both census csv is over



# In[49]:

census_2011


# In[26]:

states = {'AN' : 'ANDAMAN AND NICOBAR ISLANDS',
          'Andhra' : 'ANDHRA PRADESH',
          'ArunachalPradesh' : 'ARUNACHAL PRADESH',
          'Assam' : 'ASSAM',
          'Bihar' : 'BIHAR',
          'CG' : 'CHHATTISGARH',
          'Chandigarh' : 'CHANDIGARH',
          'D_D' : 'DAMAN AND DIU',
          'D_N_H' : 'DADRA AND NAGAR HAVELI',
          'Delhi' : 'NCT OF DELHI',
          'Goa' : 'GOA',
          'Gujrat' : 'GUJRAT',
          'HP' : 'HIMACHAL PRADESH',
          'Haryana' : 'HARYANA',
          'JK' : 'JAMMU AND KASHMIR',
          'Jharkhand' : 'JHARKHAND',
          'Karnataka' : 'KARNATAKA',
          'Kerela' : 'KERELA',
          'Lakshdweep' : 'LAKSHADWEEP',
          'MP' : 'MADHYA PRADESH',
          'Maharashtra' : 'MAHARASHTRA',
          'Manipur' : 'MANIPUR',
          'Meghalya' : 'MEGHALAYA',
          'Mizoram' : 'MIZORAM',
          'Nagaland' : 'NAGALAND',
          'Orrisa' : 'ORISSA',
          'Pondicherry' : 'PONDICHERRY',
          'Punjab' : 'PUNJAB',
          'Rajasthan' : 'RAJASTHAN',
          'Sikkim' : 'SIKKIM',
          'TN' : 'TAMIL NADU',
          'Tripura' : 'TRIPURA',
          'UP' : 'UTTAR PRADESH',
          'Uttranchal' : 'UTTARAKHAND',
          'WB' : 'WEST BENGAL'}


# In[51]:

census_2001['State'] = census_2001['State'].replace(states)
census_2001


# In[68]:

#Now comparing population of each state
d1 = census_2001.groupby('State').agg({'Persons' : np.sum})
s1 = d1['Persons']
p1 = s1.tolist()
d2 = census_2011.groupby('State').agg({'Persons' : np.sum})
s2 = d2['Persons']
p2 = s2.tolist()

x1 = range(len(p1))
x2 = []

# plot another set of bars, adjusting the new xvals to make up for the first set of bars plotted
for item in x1:
    x2.append(item+0.4)

state_list = list(states.values())
plt.figure(figsize=(14,9))
ax = plt.subplot(111)
ax.bar(x1, p1, color = 'red', align = 'center', width = 0.4, label ='Population in 2001', alpha = 0.7)
ax.bar(x2, p2, color = 'blue', align = 'center',width = 0.4, label ='Population in 2011', alpha = 0.7)
plt.xticks(range(d1.shape[0]), state_list, alpha = 0.9)
plt.xticks(rotation=80)
ax.autoscale(tight=True)
plt.legend(loc = 0, fontsize=18, frameon = False)
plt.show()


# In[66]:

#Computing literacy rate of each state
d1 = census_2001.groupby('State').agg({'Literate' : np.sum, 'Persons' : np.sum})
d1['Literacy_Rate'] = (d1.Literate.astype(float) *100) / d1.Persons.astype(float)
s1 = d1['Literacy_Rate']
p1 = s1.tolist()
p1[29] = 60.347828380

d2 = census_2011.groupby('State').agg({'Literate' : np.sum, 'Persons' : np.sum})
d2['Literacy_Rate'] = (d2.Literate.astype(float) *100) / d2.Persons.astype(float)
s2 = d2['Literacy_Rate']
p2 = s2.tolist()


# In[67]:

plt.figure(figsize=(14,9))
ax = plt.subplot(111)
ax.bar(x1, p1, color = 'red', align = 'center', width = 0.4, label ='Literacy Rate in 2001', alpha = 0.7)
ax.bar(x2, p2, color = 'blue', align = 'center',width = 0.4, label ='Literacy rate in 2011', alpha = 0.7)
plt.xticks(range(d1.shape[0]), state_list, alpha = 0.9)
plt.xticks(rotation=80)
ax.autoscale(tight=True)
plt.ylim(top=100)
plt.legend(loc = 0, fontsize=18, frameon = False)
plt.show()

