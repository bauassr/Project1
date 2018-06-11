# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 10:10:18 2018

@author: Shivam Singh 
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df=pd.read_csv('https://raw.githubusercontent.com/jackiekazil/data-wrangling/master/data/chp3/data-text.csv')

df.head(2)
df1 =pd.read_csv('https://raw.githubusercontent.com/kjam/data-wrangling-pycon/master/data/berlin_weather_oldest.csv')
df1.head(2)
print('1. Get the Metadata from the above files.')

print("="*40,"\n Meta Data for df \n ")
print(df.info())

print("\n Meta Data for df1 \n")
print(df1.info(),"\n","="*40)

print('2. Get the row names from the above files.')
df.index.values

print('3. Change the column name from any of the above file.\n',"="*40)
temp=df.rename(columns={'Indicator':'Indicator_id'})
temp.head(2)


print('4. Change the column name from any of the above file and store the changes made permanently.\n',"="*40)
df.head(2)
df.rename(columns={'Indicator':'Indicator_id'},inplace=True)
df.head(2)

print("5. Change the names of multiple columns.","="*40)
df.rename(columns={'PUBLISH STATES':'Publication Status','WHO region':'WHO Region'},inplace=True)
df.head(2)

print("6. Arrange values of a particular column in ascending order.","="*40)
result = df.sort_values(['Year'], ascending=1)
result.head(5)

print("7. Arrange multiple column values in ascending order\n.","="*40)
result = df.sort_values(['Indicator_id','Country','Publication Status','Year','WHO Region'], ascending=[0,1,0,1,1])
result=result.loc[0:2,['Indicator_id','Country','Year','WHO Region','Publication Status']]
result.head(3)

print("8. Make country​ as the first column of the dataframe.\n","="*40)
result= result.loc[:,['Country','Indicator_id', 'Publication Status', 'Year', 'WHO Region',
       'World Bank income group', 'Sex', 'Display Value', 'Numeric',
       'Low', 'High', 'Comments']]
result.head(3)

print("9. Get the column array using a variable\n","="*40)
variable = df.Country.values
variable

print("10. Get the subset rows 11, 24, 37\n","="*40)
result=df.iloc[[11,24,37]]
print(result)
print("11. Get the subset rows excluding 5, 12, 23, and 56\n","="*40)
result=df.drop([5,12,23])
print(result[(result.index > 4)& (result.index < 24) ])

print("Load datasets from CSV\n","="*40)

users =pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/users.csv')
sessions = pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/sessions.csv')
products =pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/products.csv')
transactions =pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/transactions.csv')

print("User Data \n","*"*40)
print(users.head())
print("Session Data \n","*"*40)
print(sessions.head())
print("Transaction Data \n","*"*40)
print(transactions.head())
print("12. Join users to transactions, keeping all rows from transactions and only matchingrows from users (left join)\n","="*40)
result=pd.merge(transactions,users,on='UserID',how='left')
result


print("13. Which transactions have a UserID not in users?\n","="*40)
result=result[result['User'].isnull()]
result.iloc[:,0:5]

print("14. Join users to transactions, keeping only rows from transactions and users that match via UserID (inner join)\n","="*40)
result=pd.merge(transactions,users,on='UserID')
result

print("15. Join users to transactions, displaying all matching rows AND all non-matching rows(full outer join)\n","="*40)
result=pd.merge(transactions,users,on='UserID',how='outer')
result

print("16. Determine which sessions occurred on the same day each user registered\n","="*40)
result=pd.merge(users,sessions,on='UserID')
result[result.Registered==result.SessionDate]

print("17. Build a dataset with every possible (UserID, ProductID) pair (cross join)\n","="*40)
result=users.assign(yo=1).merge(products.assign(yo=1)).drop('yo', 1)
result1=result.iloc[:,[0,5]]

print("18. Determine how much quantity of each product was purchased by each user\n","="*40)
result= pd.merge(result,transactions,on=['UserID','ProductID'],how='outer')
 
result.fillna(0)
result=result.iloc[:,[0,5,10]]
print(result)
result=result.groupby(['UserID','ProductID']).sum()
print(result)

print("19. For each user, get each possible pair of pair transactions (TransactionID1,TransacationID2)\n","="*40)
result=pd.merge(transactions, transactions, on='UserID')
print(result)

print("20. Join each user to his/her first occuring transaction in the transactions table\n","="*40)
result=pd.merge(users, transactions.groupby('UserID').first().reset_index(), on='UserID',how='left')
print(result)

print("Question: 21 - test to see if we can drop columns\n","="*40)
my_columns = list(result.columns)
print(my_columns,"\n")
list(result.dropna(thresh=int(result.shape[0] * .9), axis=1).columns) #set threshold to drop NAs
missing_info = list(result.columns[result.isnull().any()])
print(missing_info,"\n")
for col in missing_info:
    num_missing = result[result[col].isnull() == True].shape[0]
    print('number missing for column {}: {}'.format(col, num_missing))
print("\n")    
for col in missing_info:
    percent_missing = result[result[col].isnull() == True].shape[0] / result.shape[0]
    print('percent missing for column {}: {}'.format(col, percent_missing))

print("="*40)