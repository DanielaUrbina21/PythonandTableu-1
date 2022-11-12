# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 05:59:00 2022

@author: DanielaUrbina
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#method 1 to read json data
json_file=open("loan_data_json.json")
data=json.load(json_file)

#transform to dataframe

loandata = pd.DataFrame(data)

#finding unique values for the purpose column
 
loandata["purpose"].unique()
 
loandata.describe()
 
loandata["int.rate"].describe()
loandata["fico"].describe()
loandata["dti"].describe()

#Using EXP() to get the annual income

income = np.exp(loandata["log.annual.inc"])
loandata["annualincome"]=income

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

#Using for loops

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

#For interest rates

loandata.loc[loandata ["int.rate"] >0.12, "int.rate.type"] = "hight"
loandata.loc[loandata ["int.rate"] <=0.12, "int.rate.type"] = "low"

#writing to csv

loandata.to_csv("loand_cleanes.csv", index=True)




















