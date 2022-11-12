# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 07:38:35 2022

@author: DanielaUrbina
"""

import pandas as pd
data = pd.read_csv("transaction.csv")
data = pd.read_csv("transaction.csv",sep=";")

data.info()

#Profir per Item:

ProfitPerItem=SellingPricePerItem-CostPerItem

#Profit per Transaction:
    
ProfirPerTransaction=NumberofItemsPurchased*ProfitPerItem

#Cost per Transaction:
    
CostPerTransaction=NumberofItemsPurchased*CostPerItem

#Selling Prices per Transaction:
    
SellingPricePerTransaction=NumberofItemsPurchased*SellingPricePerItem

#Cost Per Transaction Column Calculation

CostPerItem=data["CostPerItem"]
NumberofItemsPurchased=data["NumberOfItemsPurchased"]
CostPerTransaction=NumberofItemsPurchased*CostPerItem

#Adding a new colum to a dataframe

data["CostPerTransaction"]=CostPerTransaction

#Sales Per Transations

data["SalesPerTransaction"]=data["SellingPricePerItem"]*data["NumberOfItemsPurchased"]


#Profit Per transactions

data["ProfitPerTransaction"]=data["SalesPerTransaction"]-data["CostPerTransaction"]

#Markup 

data["Markup"]=(data["ProfitPerTransaction"])/data["CostPerTransaction"]

#Rounding Marking 

roundmarkup=round(data["Markup"],2)


data["Markup"]=round(data["Markup"],2)

#Creating Dates

my_date="Day"+"-"+"Month"+"-"+"Year"

#Change Colums Type

day=data["Day"].astype(str)
print(day.dtype)

year=data["Year"].astype(str)
print(year.dtype)

#Unifying Dates
    
my_date=day+"-"+data["Month"]+"-"+year+"-"

data["Date"]=my_date

#creating new columns for the split colums in client keywords
Split_col=data["ClientKeywords"].str.split(",",expand=True)

data["ClientAge"]=Split_col[0]
data["Type"]=Split_col[1]
data["LengthofContract"]=Split_col[2]

#Replace funtion to delet of change items on the info

data["ClientAge"]=data["ClientAge"].str.replace("[","")

data["LengthofContract"]=data["LengthofContract"].str.replace("]","")

#Changing to lowercase

data["ItemDescription"]=data["ItemDescription"].str.lower()

#add info form another file
seasons=pd.read_csv("value_inc_seasons.csv",sep=";")

#merching files

data=pd.merge(data,seasons, on="Month")

#Deleting columns

data=data.drop("ClientKeywords",axis=1)
data=data.drop("Year",axis=1)
data=data.drop("Day",axis=1)
data=data.drop("Month",axis=1)

#Export into CSV

data.to_csv("ValueInc_Cleaned.csv", index = False)



