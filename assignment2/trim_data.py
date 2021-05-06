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
from numba import njit

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

def trim_dates(data):
    '''
    replaces datetime column with separate month and daypart column
    '''
    df = data.copy()

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

def trim_avg_rating(data):
    '''
    rounds average rating to halves
    '''
    df = data.copy()

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
            ratings[i] = 'NA'
        
    return df

def trim_avg_spent(data):
    '''
    trims average price spent per night for customers

    TODO: kijken of de distributie heel hoog is rondom een getal, en daar misschien meer 'bins' maken
    '''
    df = data.copy()

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
            spent[i] = 'NA'
        
    return df

def trim_loc_score(data):
    '''
    rounds location score to halves or adds 'NA' for missing values
    '''
    df = data.copy()

    try:
        loc_score1 = df['prop_location_score1']
        loc_score2 = df['prop_location_score2']
    except:
        print("column 'prop_location_score1' or 'prop_location_score2' has been removed, can't be trimmed")
        return df

    
    for i in range(len(loc_score1)):
        try:
            loc_score1[i] = round(loc_score1[i] * 2) / 2
        except:
            loc_score1[i] = 'NA'
            
        try:
            loc_score2[i] = round(loc_score2[i] * 2) / 2
        except:
            loc_score2[i] = 'NA'

    return df

def trim_hist_price(data):
    '''
    rounds prices or add NA for values of 0
    '''
    df = data.copy()

    try:
        hist_price = df['prop_log_historical_price']
    except:
        print("column 'prop_log_historical_price' has been removed, can't be trimmed")
        return df
    
    for i in range(len(hist_price)):    
        if hist_price[i] > 0:
            hist_price[i] = round(hist_price[i] * 2) / 2
        else:
            hist_price[i] = 'NA'
    
    return df

def trim_price(data):
    df = data.copy()
    try:
        price = df['price_usd']
    except:
        print("column 'price_usd' has been removed, can't be trimmed")
        return df

    
    for i in range(len(price)):    
        price[i] = round(price[i])

    return df
    

def trim_book_window(data):
    '''
    changes booking window from days to weeks
    '''
    df = data.copy()
    try:
        booking_window = df['srch_booking_window']
    except:
        print("column 'srch_booking_window' has been removed, can't be trimmed")
        return df

    
    for i in range(len(booking_window)):
        try:
            booking_window[i] = round(booking_window[i]/7)
        except:
            booking_window[i] = 'NA'

    return df


def trim_dest_dist(data):
    '''
    divides distance to destination by 100 miles
    '''
    df = data.copy()

    try:
        dest_dist = df['orig_destination_distance']
    except:
        print("column 'orig_destination_distance' has been removed, can't be trimmed")
        return df

    for i in range(len(dest_dist)):
        try:
            dest_dist[i] = round(dest_dist[i]/100)
        except:
            # booking_window[i] = 'NA'
            dest_dist[i] = 'NA'

    return df    




def trim_data(df):
    # remove hotels that are not picked
    # TODO

    # remove columns with >95% missing data values
    trim_cols(df)
    
    # restructure data
    # df = trim_dates(df)
    # df = trim_avg_rating(df)
    # df = trim_avg_spent(df)
    # df = trim_loc_score(df)
    # df = trim_hist_price(df)
    # df = trim_price(df)
    # df = trim_book_window(df)
    # df = trim_dest_dist(df)
    
    return df
    
data = trim_data(df)

# data.to_csv('small_data/trimmed_data.csv')

