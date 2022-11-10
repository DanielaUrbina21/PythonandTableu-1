# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 05:59:00 2022

@author: David
"""

import json

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

#method 1 to read json data
json_file=open("loan_data_json.json")

data=json.load(json_file)

#method 2 to read json data
with open ("loan_data_json.json")as json_file:
    data=json.load(json_file)
    
#transform to dataframe

loandata = pd.DataFrame(data)

 #Choose unique values in a column 
 #finding unique values for the purpose column
 
loandata["purpose"].unique()
 
 #Describe fountion
 #Describe the data
 
loandata.describe()
 
#for specific column

loandata["int.rate"].describe()
loandata["fico"].describe()
loandata["dti"].describe()

#Using EXP() to get the annual income

income = np.exp(loandata["log.annual.inc"])
loandata["annualincome"]=income

#Working with arrays/matrices

#1D array
arr=np.array([1,2,3,4])

#0D array
arr=np.array(43)

#2D array
arr=np.array([[1,2,3],[4,5,6]])


#Working with IF Statements

a=40
b=500
if b>a:
    print("b is greater than a")
    
#Let's add more conditions

a=40
b=500
c=1000

if b>a and b<c:
    print("b is greater than a but less than c")

#what if a condition is not met?

a=40
b=500
c=20

if b>a and b<c:
    print("b is greater than a but less than c")
else:
    print("No conditions met")

#another condition different metrics

a=40
b=0
c=30

if b>a and b<c:
   print("b is greater than a but less than c")
elif b>a and b>c:
    print("bi is greater than a and c")
else: 
    print("No conditions met")

#using or
a=40
b=500
c=30

if b>a or b<c:
   print("b is greater than a but less than c")
else: 
    print("No conditions met")

#FICO score

fico=500

# fico >= 300 and < 400:'Very Poor'
# fico >= 400 and ficoscore < 600: 'Poor'
# fico >= 601 and ficoscore < 660: 'Fair'
# fico >= 660 and ficoscore < 780: 'Good'
# fico >=780: 'Excellent

if fico>= 300 and fico < 400:
    ficocat="Very Poor"
elif fico>= 400 and fico < 600:
    ficocat= "Poor"
elif fico>=601 and fico < 660:
    ficocat="Fair"
elif fico>=660 and fico < 700:
    ficocat="Good"
elif fico>=700:
    ficocat="Excellent"
else:
    ficocat= "Unknown"
print(ficocat)


#for loops

colors=["yellow", "purple", "pink", "blue"]

for x in colors:
    print(x)
    y = x+ " english color"
    print(y)

#applying for loops to loan data

#using first 10


length=len(loandata)
ficocat = []
for x in range (0,length):
    category=loandata ["fico"][x]
    
    try:        
        if category>= 300 and category < 400:
            cat ="Very Poor"
        elif category>= 400 and category < 600:
            cat = "Poor"
        elif category>=601 and category < 660:
            cat ="Fair"
        elif category>=660 and category < 700:
            cat="Good"
        elif category>=700:
            cat ="Excellent"
        else:
            category = "Unknown"
    except:
        cat="Unknown"
    ficocat.append(cat)

ficocat=pd.Series(ficocat)

loandata["Fico.category"]=ficocat


#df.loc as conditional statements
# df.loc[df[columname] condition, newcolumnname]="value if the condition is met"

#for interest rates, a new column is wanted. rate>0.12 then hight, else low.

loandata.loc[loandata ["int.rate"] >0.12, "int.rate.type"] = "hight"
loandata.loc[loandata ["int.rate"] <=0.12, "int.rate.type"] = "low"

#number of loans/rows by fico.category
#graficas

catplot=loandata.groupby(["Fico.category"]).size()
catplot.plot.bar(color= "gray", width=0.1)
plt.show()

purposecount=loandata.groupby(["purpose"]).size()
purposecount.plot.bar()
plt.show()

#scatter plots

ypoint=loandata["annualincome"]
xpoint=loandata["dti"]
plt.scatter(xpoint,ypoint, color="purple")
plt.show()


#writing to csv

loandata.to_csv("loand_cleanes.csv", index=True)




















