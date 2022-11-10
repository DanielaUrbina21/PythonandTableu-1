# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 07:38:35 2022

@author: DanielaUrbina21
"""

import pandas as pd

#file_name=pd.read_csv("file.csv") --- format of read_csv

data = pd.read_csv("transaction.csv")

data = pd.read_csv("transaction.csv",sep=";")

#en size dice que hay una sola columna
#esto paso porque el archivo no estaba dividido por ,
#debemos agregar data = pd.read_csv("transaction.csv",sep=";")
#en este caso sep es por separación
#spyder te muestra todo lo que se puede hacer despues de la ,


#summary of datat

data.info()

#Working with calculations
#Defining Variables

CostPerItem=11.73
SellingPricePerItem=21.11
NumberofItemsPurchased=6

#Math Opperations on Tableau

#Profir per Item:

ProfitPerItem=21.11-11.73
ProfitPerItem=SellingPricePerItem-CostPerItem

#Profit per Transaction:
    
ProfirPerTransaction=NumberofItemsPurchased*ProfitPerItem

#Cost per Transaction:
    
CostPerTransaction=NumberofItemsPurchased*CostPerItem

#Selling Prices per Transaction:
    
SellingPricePerTransaction=NumberofItemsPurchased*SellingPricePerItem

#Cost Per Transactio9n Column Calculation

#CostPerTransaction=CostPerItem*NumberofItemsPurchases
#Variable=dataframe["column_name"]

CostPerItem=data["CostPerItem"]
NumberofItemsPurchased=data["NumberOfItemsPurchased"]

CostPerTransaction=NumberofItemsPurchased*CostPerItem

#Adding a new colum to a dataframe

data["CostPerTransaction"]=CostPerTransaction

# o asi. data["CostPerTransaction"]=data["CostPerItem"]*data["NumberOfItemsPurchased"]

#Sales Per Transations

data["SalesPerTransaction"]=data["SellingPricePerItem"]*data["NumberOfItemsPurchased"]


#Profit Per transactions

data["ProfitPerTransaction"]=data["SalesPerTransaction"]-data["CostPerTransaction"]

#Markup 

data["Markup"]=(data["ProfitPerTransaction"])/data["CostPerTransaction"]

#Rounding Marking -aproximando-

roundmarkup=round(data["Markup"],2)


data["Markup"]=round(data["Markup"],2)

#Dates, combinar columnas

my_date="Day"+"-"+"Month"+"-"+"Year"

#PYTHON no deja mezclar numeros con letras cuando se van a crear nuevas variables
#Revisar que tipo de variable es:
data.info()
#o asi:
print(data["Day"].dtype)

#Change Colums Type

day=data["Day"].astype(str)
print(day.dtype)

year=data["Year"].astype(str)
print(year.dtype)

#Ahora con todo en el mismo formato, combinamos:
    
my_date=day+"-"+data["Month"]+"-"+year+"-"

data["Date"]=my_date

#Using iloc to view specific columns/rows pdlibrary
# 0 es el sujeto- la fila- index 0
data.iloc[0]

data.iloc[0:3] #los primeros 3

data.iloc[-5:] #last five rows

data.head(5) #brings in first 5 rows

data.iloc[:,2] #todas las filas pero solo una columna

data.iloc[4,2]#dato preciso de un sujeto, ejemplo el año columna 2

#separar información en nuevas columnas/using split to split the client keywords field

#new-var=column.str.split("sep",expand=True)

Split_col=data["ClientKeywords"].str.split(",",expand=True)

#creating new columns for the split colums in client keywords
data["ClientAge"]=Split_col[0]
data["Type"]=Split_col[1]
data["LengthofContract"]=Split_col[2]

#Replace funtion to delet of change items on the info

data["ClientAge"]=data["ClientAge"].str.replace("[","")

data["LengthofContract"]=data["LengthofContract"].str.replace("]","")

#Changing to lowercase

data["ItemDescription"]=data["ItemDescription"].str.lower()

#add info form another file
#how to merge files
#bringin in a new dataset
seasons=pd.read_csv("value_inc_seasons.csv",sep=";")

#merching files: merge_df=pd.merge(df_old,df_new, on="key") key is the common data, ex: month

data=pd.merge(data,seasons, on="Month")

#eliminar columnas: df=df.drop("columnname",axis=1)

data=data.drop("ClientKeywords",axis=1)
data=data.drop("Year",axis=1)
data=data.drop("Day",axis=1)
data=data.drop("Month",axis=1)

#Export into CSV

data.to_csv("ValueInc_Cleaned.csv", index = False)



