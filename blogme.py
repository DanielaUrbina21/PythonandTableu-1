# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 17:48:56 2022

@author: Danielaurca
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
data = pd.read_excel("articles.xlsx")
data.describe()
data.info()

data.groupby(["source_id"])["article_id"].count()

# No. reactions by publisher
data.groupby(["source_id"])["engagement_reaction_count"].sum()

data = data.drop("engagement_comment_plugin_count" , axis=1)

#Creating a keyword flag

keyword="murder"

#creating a for loop in to a function to isolate each title

def keywordflag(keyword):
    lenght=len(data)
    keyword_flag = []
    for x in range (0,lenght):
        heading = data["title"][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag
    
keywordflag = keywordflag("murder")

#Adding a new column

data["keyword_flag"] = pd.Series(keywordflag)


#SentimentIntensityAnalyzer

sent_int = SentimentIntensityAnalyzer ()

text = data ["title"][14]
sent = sent_int.polarity_scores(text)

neg = sent["neg"]
pos = sent["pos"]
neu = sent["neu"]

#adding a for loop to extract sentiment per title

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

lenght=len(data)
for x in range (0, lenght):
    text = data ["title"][x]
    try:            
        sent_int = SentimentIntensityAnalyzer ()
        sent = sent_int.polarity_scores(text)
        neg = sent["neg"]
        pos = sent["pos"]
        neu = sent["neu"]
    except: 
        neg = 0
        pos = 0
        neu = 0  
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)
   

data ["title_neg_sentiment"] = pd.Series(title_neg_sentiment)
data ["title_pos_sentiment"] = pd.Series(title_pos_sentiment)
data ["title_neu_sentiment"] = pd.Series(title_neu_sentiment)


#writing the data

data.to_excel("blogme_clean.xlsx", sheet_name="blogmedata", index=False)









































       
 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

