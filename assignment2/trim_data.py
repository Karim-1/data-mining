
'''
trims the data, add
_________________________________________________________________
try-excepts have been added in each function to check whether the 
column has not been removed due to >95% of data values missing.
'''

from trim_functions import *


def trim_data(df):
    start_time = time.time()

    
    # dates = df['date_time'].to_numpy()    
    # months, dayparts = trim_dates(dates)
    # df['month'] = months
    # df['daypart'] = dayparts

    # # change column order df
    # cols = df.columns.tolist()
    # cols = cols[1:2] + cols[-2:] + cols[4:-3]
    # df = df[cols]
    


    df = trim_avg_rating(df)
    df = trim_avg_spent(df)
    df = trim_loc_score(df)
    df = trim_hist_price(df)
    df = trim_price(df)
    df = trim_book_window(df)
    df = trim_dest_dist(df)
    
    
    print("--- trimming took %s seconds ---" % (round(time.time() - start_time)))
    
    return df

df = pd.read_csv("../training_set_VU_DM.csv")
# df = pd.read_csv("small_data/3000_training_set_VU_DM.csv")
data = trim_data(df)

data.to_csv('../TRIMMED_training_set_VU_DM.csv')

