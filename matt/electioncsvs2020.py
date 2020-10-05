# -*- coding: utf-8 -*-
"""
A script to algorithmically fetch csvs of state-level
search data, clean them up, and merge them into one nice
csv for importing into RStudio.
"""

from pytrends.request import TrendReq

pytrend = TrendReq()

listy = ['Trump', 'CNN', 
           'Keep America Great', 'Benghazi',
           'Fox News', 'Facebook', 'Instagram',
           'Twitter', 'fake news', 'black lives matter',
           'healthcare', 'immigration', 'racism',
           'Dow Jones', 'Russia', 'China', 'NASDAQ', 'Biden',
           'Sleepy Joe', 'Breonna Taylor', 'George Floyd', 'wildfires',
           'COVID-19', 'coronavirus', 'social distancing', 'face masks',
           'white supremacy', 'Trump covid']

dfs = []

for item in listy:
    pytrend.build_payload(kw_list=[item], geo='US',
                          timeframe='2020-08-01 2020-10-3')

    dfs.append(pytrend.interest_by_region())
    
df_final = dfs[0]

for df in dfs[1:]:
    df_final = df_final.join(df, how='inner')
    
df_final.to_csv('state_searches2020.csv')