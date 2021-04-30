import dateparser
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from numpy.core.numeric import NaN





df = pd.read_csv("small_data/3000_training_set_VU_DM.csv")


def trim_dates(df):
    '''
    replaces datetime column with separate month and daypart column
    '''
    dates = df['date_time']

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

    
    cols = df.columns.tolist()
    print(cols)
    # change column order df
    cols = cols[1:2] + cols[-2:] + cols[4:-3]
    print(cols)

    df = df[cols]

    return df

def trim_avg_rating(df):
    '''
    rounds average rating to halves
    '''
    ratings = df['visitor_hist_starrating']
    
    # round ratings to halves, or add NA if data is missing
    for i in range(len(ratings)):
        try:
            ratings[i] = round(ratings[i] * 2) / 2
        except:
            ratings[i] = 'NA'
        
    return df

def trim_avg_spent(df):
    '''
    trims average price spent per night for customers

    TODO: kijken of de distributie heel hoog is rondom een getal, en daar misschien meer 'bins' maken
    '''
    spent = df['visitor_hist_adr_usd']

    # round to every 50 dollars spent or add 'NA'
    for i in range(len(spent)):
        try:
            multiplier = round(spent[i]/50)
            spent[i] = multiplier * 50
        except:
            spent[i] = 'NA'
        
    return df

def trim_data(df):
    df = trim_dates(df)
    # df = trim_avg_rating(df)
    # df = trim_avg_spent(df)
    # df = trim_avg_spent(df)

    return df
    
data = trim_data(df)
print(data)

