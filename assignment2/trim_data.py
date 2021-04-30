'''
trims the data, add
_________________________________________________________________
try-excepts have been added in each function to check whether the 
column has not been removed due to >95% of data values missing.
'''

import copy
import dateparser
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from numpy.core.numeric import NaN


df = pd.read_csv("small_data/3000_training_set_VU_DM.csv")

def trim_cols(data):
    '''
    removes columns with >95% missing data values
    '''
    df = data.copy()
    total_values = len(df.index)
    
    for col in df:
        missing_values = sum(df[col].isnull()==True)
        if missing_values > .95 * total_values:
            print('column', col, 'removed')
            df.drop(col, 1)

    return df

def trim_dates(df):
    '''
    replaces datetime column with separate month and daypart column
    '''
    try:
        dates = df['date_time']
    except:
        print("column 'date_time' has been removed, can't be trimmed")
        return df
    

    months, dayparts = [], []
    for i in range(len(dates)):
        # split date and time
        datetime = dateparser.parse(dates[i])

        # retrieve month and add to df
        month = datetime.date().month
        months.append(month)

        # retrieve daypart and add to df
        def get_daypart(hour):
            ''' 
            retrieves daypart string based on hour of the day
            '''
            if (hour > 6) and (hour <= 12):
                return 'Morning'
            elif (hour > 12) and (hour <= 18 ):
                return 'Afternoon'
            elif (hour > 18) and (hour <= 24):
                return 'Noon'
            else:
                return 'Night'
                
        hour = datetime.time().hour
        daypart = get_daypart(hour)
        dayparts.append(daypart)

    df['month'] = months
    df['daypart'] = dayparts

    # change column order df
    cols = df.columns.tolist()
    cols = cols[1:2] + cols[-2:] + cols[4:-3]
    df = df[cols]

    return df

def trim_avg_rating(df):
    '''
    rounds average rating to halves
    '''
    try:
        ratings = df['visitor_hist_starrating']
    except:
        print("column 'visitor_hist_starrating' has been removed, can't be trimmed")
        return df
    
    
    # round ratings to halves, or add NA if data is missing
    for i in range(len(ratings)):
        try:
            ratings[i] = round(ratings[i] * 2) / 2
        except:
            # ratings[i] = 'NA'
            continue
        
    return df

def trim_avg_spent(df):
    '''
    trims average price spent per night for customers

    TODO: kijken of de distributie heel hoog is rondom een getal, en daar misschien meer 'bins' maken
    '''
    try:
        spent = df['visitor_hist_adr_usd']
    except:
        print("column 'visitor_hist_adr_usd' has been removed, can't be trimmed")
        return df

    # round to every 50 dollars spent or add 'NA'
    for i in range(len(spent)):
        try:
            multiplier = round(spent[i]/50)
            spent[i] = multiplier * 50
        except:
            # spent[i] = 'NA'
            continue
        
    return df

def trim_data(df):
    # remove columsn with >95% missing data values
    trim_cols(df)

    # restructure data
    df = trim_dates(df)
    df = trim_avg_rating(df)
    df = trim_avg_spent(df)
    df = trim_avg_spent(df)

    return df
    
data = trim_data(df)

