# -*- coding: utf-8 -*-
"""
A script to algorithmically fetch csvs of state-level
search data, clean them up, and merge them into one nice
csv for importing into RStudio.
"""

from pytrends.request import TrendReq

pytrend = TrendReq()

listy = ['Trump', 'Clinton', 'CNN', 'WikiLeaks',
           'Make America Great Again', 'Benghazi',
           'Fox News', 'Facebook', 'Instagram',
           'Twitter', 'fake news', 'black lives matter',
           'antifa', 'healthcare', 'immigration', 'racism']

dfs = []

for item in listy:
    pytrend.build_payload(kw_list=[item], geo='US', timeframe='2016-09-01 2016-11-01')

    dfs.append(pytrend.interest_by_region())
    
df_final = dfs[0]

for df in dfs[1:]:
    df_final = df_final.join(df, how='inner')
    
df_final.to_csv('state_searches.csv')