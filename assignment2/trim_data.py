
'''
trims the data, add
_________________________________________________________________
try-excepts have been added in each function to check whether the 
column has not been removed due to >95% of data values missing.
'''

from trim_functions import *
import time


def trim_data(df):
    # track time
    start_time = time.time()
    
    # # trim dates
    # dates = df['date_time'].to_numpy()    
    # months, dayparts = trim_dates(dates)
    # df['month'] = months
    # df['daypart'] = dayparts

    # # change column order df
    # cols = df.columns.tolist()
    # cols = cols[1:2] + cols[-2:] + cols[4:-3]
    # df = df[cols]
    
    # trim ratings
    print('Trimming visitor_hist_starrating:')
    ratings = df['visitor_hist_starrating'].to_numpy()
    ratings = round_halves(ratings)
    df['visitor_hist_starrating'] = ratings

    # trim avg spent
    spent = df['visitor_hist_adr_usd'].to_numpy()
    avg_spent = trim_avg_spent(spent)
    df['visitor_hist_adr_usd'] = avg_spent

    # trim location scores
    loc_score1 = df['prop_location_score1'].to_numpy()
    loc_score2 = df['prop_location_score2'].to_numpy()
    loc_score1, loc_score2 = trim_loc_score(loc_score1, loc_score2)
    df['prop_location_score1'] = loc_score1
    df['prop_location_score2'] = loc_score2

    # trim hist price
    hist_price = df['prop_log_historical_price'].to_numpy()
    trimmed_hist_price = trim_hist_price(hist_price)
    df['prop_log_historical_price'] = trimmed_hist_price

    # trim price
    price = df['price_usd'].to_numpy()
    trimmed_price = trim_price(price)
    df['price_usd'] = trimmed_price

    # trim booking window
    booking_window = df['srch_booking_window'].to_numpy()
    trimmed_booking_window = trim_booking_window(booking_window)
    df['srch_booking_window'] = trimmed_booking_window

    # df = trim_dest_dist(df)
    dest_dist = df['orig_destination_distance'].to_numpy()
    trimmed_dest_dist = trim_dest_dist(dest_dist)
    df['orig_destination_distance'] = trimmed_dest_dist
    
    
    print("--- trimming took %s seconds ---" % (round(time.time() - start_time)))
    
    return df

df = pd.read_csv("../training_set_VU_DM.csv")
# df = pd.read_csv("small_data/3000_training_set_VU_DM.csv")
data = trim_data(df)

# data.to_csv('../TRIMMED_training_set_VU_DM.csv')

