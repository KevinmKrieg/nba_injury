import pandas as pd
import requests
import numpy as np
import datetime
from bs4 import BeautifulSoup


class Scrape_Injuries(object):
    '''
    This class scrapes the ProSportsTransactions website for injury data.
    The data is stored in a Pandas dataframe and then saved to a CSV file.
    '''

    def __init__(self, fn='/data/injuries.csv'):
        '''
        INPUT: The location and filename of the csv file to be saved
        OUTPUT: None
        '''

        self.fn = fn

    # scraping for injuries
    def get_injuries(self):
        '''
        INPUT: None
        OUTPUT: None
        '''

        # Create columns for dataframe
        df = pd.DataFrame(columns=['Date', 'Team', 'Acquired','Relinquished', 'Notes'])

        # url for Prosportstransactions
        url = 'http://www.prosportstransactions.com/basketball/Search/' +\
              'SearchResults.php?Player=&Team=&BeginDate=&EndDate=' +\
              '&InjuriesChkBx=yes&Submit=Search&start='

        # loop through all available pages and store info in a dataframe
        for i in range(20500, 26500, 25):
            r = requests.get(url + str(i))
            soup = BeautifulSoup(r.content)

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
        df['Player'] = df['Player'].decode('utf-8')
        df['Player'] = df['Player'].str.strip()
        # save to csv
        df.to_csv(self.fn)
        
#for player in df['Player']:
freak = df[df['Player'] == 'Giannis Antetokounmpo']
for i in range(0, length(freak)-1):
    if in['Relinquished'] != 'b' '':

for col in df:
    df[col] = df[col].str.decode('utf-8')
    df[col] = df[col].str.strip()
    
    