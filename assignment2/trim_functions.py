import copy
import dateparser
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time

from numba import jit, njit
from numpy.core.numeric import NaN
from tqdm import tqdm



# @jit(nopython=True)
def trim_cols(data):
    '''
    removes columns with >95% missing data values
    '''
    print('Trimming columns with > 95% missing values:')

    df = data.copy()
    total_values = len(df.index)
    removed_cols=[]
    for col in tqdm(df, total = df.shape[1]):
        missing_values = sum(df[col].isnull()==True)
        if missing_values > .95 * total_values:
            removed_cols.append(col)
            df.drop(col, 1)

    print('Removed cols:')
    for col in removed_cols:
        print(col)
    print('\n')

    return df


def get_daypart(hour):
    ''' 
    retrieves daypart string based on hour of the day
    for trim_dates function
    '''
    if (hour > 6) and (hour <= 12):
        return 'Morning'
    elif (hour > 12) and (hour <= 18 ):
        return 'Afternoon'
    elif (hour > 18) and (hour <= 24):
        return 'Noon'
    else:
        return 'Night'


# @njit
def trim_dates(dates):
    '''
    replaces datetime column with separate month and daypart column
    '''
    months, dayparts = [], []
    print(dates)
    
    for i in tqdm(range(len(dates))):
        # split date and time
        datetime = dateparser.parse(dates[i])

        # retrieve month 
        month = datetime.date().month
        months.append(month)
                
        # retrieve daypart based on hour of the day
        hour = datetime.time().hour
        daypart = get_daypart(hour)
        dayparts.append(daypart)

    return months, dayparts


@jit(nopython=True)
def trim_avg_rating(ratings):
    '''
    rounds average rating to halves
    '''
    # round ratings to halves, or add NA if data is missing
    for i in tqdm(range(len(ratings))):
        try:
            ratings[i] = round(ratings[i] * 2) / 2
        except:
            ratings[i] = 'NA'
        
    return ratings


# @jit(nopython=True)
def trim_avg_spent(data):
    '''
    trims average price spent per night for customers

    TODO: kijken of de distributie heel hoog is rondom een getal, en daar misschien meer 'bins' maken
    '''
    df = data.copy()

    try:
        spent = df['visitor_hist_adr_usd']
        print('Trimming visitor_hist_adr_usd:')
    except:
        print("column 'visitor_hist_adr_usd' has been removed, can't be trimmed")
        return df

    # round to every 50 dollars spent or add 'NA'
    for i in tqdm(range(len(spent))):
        try:
            multiplier = round(spent[i]/50)
            spent[i] = multiplier * 50
        except:
            spent[i] = 'NA'
        
    return df


# @jit(nopython=True)
def trim_loc_score(data):
    '''
    rounds location score to halves or adds 'NA' for missing values
    '''
    df = data.copy()

    try:
        loc_score1 = df['prop_location_score1']
        loc_score2 = df['prop_location_score2']
        print('Trimming prop_location_score1 and prop_location_score2:')
    except:
        print("column 'prop_location_score1' or 'prop_location_score2' has been removed, can't be trimmed")
        return df

    
    for i in tqdm(range(len(loc_score1))):
        try:
            loc_score1[i] = round(loc_score1[i] * 2) / 2
        except:
            loc_score1[i] = 'NA'
            
        try:
            loc_score2[i] = round(loc_score2[i] * 2) / 2
        except:
            loc_score2[i] = 'NA'

    return df


# @jit(nopython=True)
def trim_hist_price(data):
    '''
    rounds prices or add NA for values of 0
    '''
    df = data.copy()

    try:
        hist_price = df['prop_log_historical_price']
        print('Trimming prop_log_historical_price:')
    except:
        print("column 'prop_log_historical_price' has been removed, can't be trimmed")
        return df
    
    for i in tqdm(range(len(hist_price))):
        if hist_price[i] > 0:
            hist_price[i] = round(hist_price[i] * 2) / 2
        else:
            hist_price[i] = 'NA'
    
    return df


# @jit(nopython=True)
def trim_price(data):
    df = data.copy()
    try:
        price = df['price_usd']
        print('Trimming price_usd:')
    except:
        print("column 'price_usd' has been removed, can't be trimmed")
        return df

    
    for i in range(len(price)):    
        price[i] = round(price[i])

    return df
    

# @jit(nopython=True)
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

    
    for i in tqdm(range(len(booking_window))):
        try:
            booking_window[i] = round(booking_window[i]/7)
        except:
            booking_window[i] = 'NA'

    return df


# @njit
def trim_dest_dist(data):
    '''
    divides distance to destination by 100 miles
    '''
    df = data.copy()

    try:
        dest_dist = df['orig_destination_distance']
        print('Trimming orig_destination_distance:')
    except:
        print("column 'orig_destination_distance' has been removed, can't be trimmed")
        return df

    for i in tqdm(range(len(dest_dist))):
        try:
            dest_dist[i] = round(dest_dist[i]/100)
        except:
            # booking_window[i] = 'NA'
            dest_dist[i] = 'NA'

    return df    