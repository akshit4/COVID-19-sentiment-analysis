# -*- coding: utf-8 -*-
"""
Created on Mon May 25 15:01:47 2020

@author: lenovo
"""

from textblob import TextBlob
import pandas as pd
import seaborn as sns

TweetsDataSet = pd.read_csv('COVID-19.csv')

## function to get subjectivity
def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

## function to get polarity
def getPolarity(text):
    return TextBlob(text).sentiment.polarity

##Adding subjectivity and polarity to dataframe
TweetsDataSet['Subjectivity'] = TweetsDataSet['text'].apply(getSubjectivity)
TweetsDataSet['Polarity'] = TweetsDataSet['text'].apply(getPolarity)

## checking for NULL value
TweetsDataSet.isnull().sum()

## Basic analysis of data
TweetsDataSet.describe()

##Graph of subjectivity
sns.distplot(TweetsDataSet['Subjectivity'])


##Graph of polarity
sns.distplot(TweetsDataSet['Polarity'])

## regression plot for subjectivity and polarity   
sns.regplot(x='Subjectivity',y='Polarity',scatter=True,fit_reg=True,data=TweetsDataSet)