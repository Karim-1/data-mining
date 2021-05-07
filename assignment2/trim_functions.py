import copy
import dateparser
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time

from numba import jit, njit
from numpy.core.numeric import NaN
from tqdm import tqdm



# @jit
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


# @jit
def trim_dates(dates):
    '''
    replaces datetime column with separate month and daypart column
    '''
    print('Trimming datetime:')

    months, dayparts = [], []
    
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


# @jit(nopython=False)
def round_halves(raw_values):
    '''
    rounds to halves
    '''
    values = np.nan_to_num(raw_values)
    
    # round ratings to halves, or add NA if data is missing
    for i in tqdm(range(len(values))):
        # progress bar    
        if i % (1/len(values)) == 0:
            print(i/len(values), '%', end='\r')
        
        values[i] = round(values[i] * 2) / 2
    
    return values


# @jit(nopython=True)
def trim_avg_spent(spent):
    '''
    trims average price spent per night for customers

    TODO: kijken of de distributie heel hoog is rondom een getal, en daar misschien meer 'bins' maken
    '''
    print('Trimming visitor_hist_adr_usd:')
    # spent = df['visitor_hist_adr_usd'].to_numpy()
    avg_spent = np.nan_to_num(spent)

    # round to every 50 dollars spent or add 'NA'
    for i in tqdm(range(len(avg_spent))):
        multiplier = round(avg_spent[i]/50)
        avg_spent[i] = multiplier * 50

    return avg_spent


# @jit(nopython=True)
def trim_loc_score(loc_score1, loc_score2):
    '''
    rounds location score to halves or adds 'NA' for missing values
    '''
    print('Trimming prop_location_scores:')
    score1 = np.nan_to_num(loc_score1)
    score2 = np.nan_to_num(loc_score2)

    for i in tqdm(range(len(score1))):
        score1[i] = round(score1[i] * 2) / 2
        score2[i] = round(score2[i] * 2) / 2    

    return score1, score2


# @jit(nopython=True)
def trim_hist_price(price):
    '''
    rounds prices or add NA for values of 0
    '''
    print('Trimming prop_log_historical_price:')
    hist_price = np.nan_to_num(price)
    for i in tqdm(range(len(hist_price))):
        hist_price[i] = round(hist_price[i] * 2) / 2
        
    return hist_price


# @jit(nopython=True)
def trim_price(price):
    print('Trimming price_usd:')
    trimmed_price = np.nan_to_num(price)
    for i in tqdm(range(len(trimmed_price))):    
        trimmed_price[i] = round(trimmed_price[i])

    return trimmed_price
    

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