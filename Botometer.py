#!/usr/bin/env python
# coding: utf-8

pip install botometer

import botometer
import numpy as np
import pandas as pd
import sys


rapidapi_key = "51917898a3msh34d9ae2cbcd6f5dp13c506jsn1e0da8daeaff" # now it's called rapidapi key
twitter_app_auth = {
    'consumer_key': 'XXXX',
    'consumer_secret': 'XXXX',
    'access_token': 'XXXX',
    'access_token_secret': 'XXXX',
  }
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

# Check a single account by screen name
#result = bom.check_account('@accountname')

# Check a single account by account name
#result = bom.check_account(accountid)

final1=pd.read_excel("inputfilename.xlsx")

i = 0
def get_bot_score(user_name):
    global i
    print(i," ",user_name)
    i=i+1
    score = []
    try:
        result = bom.check_account('@'+user_name)
        english_score = result['scores']['english']
        universal_score = result['scores']['universal']
        score.append(english_score)
        score.append(universal_score)
        print(str(english_score) +","+str(universal_score))
        #print(universal_score)
    except:
        e = sys.exc_info()[0]
        #print(e)
        score.append(-1)
        score.append(-1)
        print("-1,-1")
        
        return(score)
    return(score)


bot_score = final1.user_name.apply(get_bot_score)
bot_score = list(bot_score)
bot_score_df = pd.DataFrame(bot_score)
bot_score_df.columns = ['english_score','universal_score']
bot_score_df.to_csv('outputfilename.csv', index = None, header=True)








