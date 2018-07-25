"""
Created on Tue May 22 13:59:55 2018

@author: Kevin
"""
import pandas as pd
import requests
import numpy as np
import datetime
from bs4 import BeautifulSoup

df = pd.DataFrame(columns=['Date', 'Team', 'Acquired','Relinquished', 'Notes'])
url = 'http://www.prosportstransactions.com/basketball/Search/' +\
              'SearchResults.php?Player=&Team=&BeginDate=&EndDate=' +\
              '&InjuriesChkBx=yes&Submit=Search&start='
for i in range(20500, 26500, 25):
            r = requests.get(url + str(i))
            soup = BeautifulSoup(r.content,'html')

            # Read from html
            transactions = [line.text.encode('ascii', 'ignore')
                            for line in soup.findAll('td')]
            # Remove irrelevant content
            #del transactions[transactions.index(''):]

            # Populate dataframe
            for i in range(5, len(transactions)-4, 5):
                df = df.append({'Date': transactions[i],
                                'Team': transactions[i+1],
                                'Acquired': transactions[i+2],
                                'Relinquished' : transactions[i+3],
                                'Notes': transactions[i+4]},
                               ignore_index=True)
                
            df['Player'] = np.where(df['Acquired']==b' ',df['Relinquished'], df['Acquired'])        
            #df['Player'] = df['Player'].decode('utf-8')
            #df['Player'] = df['Player'].str.strip()