# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:47:36 2020

@author: lenovo
"""

from twitterscraper import query_tweets
import datetime as dt
import pandas as pd

"""
    Importing tweets between 4-MARCH-2020 to 24-MARCH-2020 about COVID-19. 
"""
begin_date = dt.date(2020,3,4)
end_date = dt.date(2020,3,24)
limit = 5000
lang = 'english'
tweets = query_tweets('coronavirus',begindate = begin_date, enddate = end_date, limit = limit, lang = lang)
MarchDataSet = pd.DataFrame(t.__dict__ for t in tweets)

"""
    Importing tweets between 4-APRIL-2020 to 24-APRIL-2020 about COVID-19. 
"""
begin_date = dt.date(2020,4,4)
end_date = dt.date(2020,4,24)
limit = 5000
lang = 'english'
tweets = query_tweets('coronavirus',begindate = begin_date, enddate = end_date, limit = limit, lang = lang)
AprilDataSet = pd.DataFrame(t.__dict__ for t in tweets)

"""
    Importing tweets between 4-MAY-2020 to 24-MAY-2020 about COVID-19. 
"""
begin_date = dt.date(2020,5,4)
end_date = dt.date(2020,5,24)
limit = 5000
lang = 'english'
tweets = query_tweets('coronavirus',begindate = begin_date, enddate = end_date, limit = limit, lang = lang)
MayDataSet = pd.DataFrame(t.__dict__ for t in tweets)


"""
    Combining MARCH,APRIL,MAY dataset into one dataset.
"""
DataSet = [MarchDataSet,AprilDataSet,MayDataSet]
RawDataSet = pd.concat(DataSet)



"""
    Cleaning RawDataSet and save into CSV file to doing sentiment analysis
"""
CleanDataSet = RawDataSet[['screen_name','username','timestamp','text','hashtags']]

CleanDataSet.to_csv(r'C:\Users\lenovo\Desktop\Twitter Analysis of COVID-19\COVID-19.csv',index=False)





