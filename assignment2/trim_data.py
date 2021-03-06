
'''
trims the data, adds new features
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
    
    # # trim ratings
    # print('Trimming visitor_hist_starrating:')
    # ratings = df['visitor_hist_starrating'].to_numpy()
    # ratings = round_halves(ratings)
    # df['visitor_hist_starrating'] = ratings

    # # trim avg spent
    # spent = df['visitor_hist_adr_usd'].to_numpy()
    # avg_spent = trim_avg_spent(spent)
    # df['visitor_hist_adr_usd'] = avg_spent

    # # trim location scores
    # loc_score1 = df['prop_location_score1'].to_numpy()
    # loc_score2 = df['prop_location_score2'].to_numpy()
    # loc_score1, loc_score2 = trim_loc_score(loc_score1, loc_score2)
    # df['prop_location_score1'] = loc_score1
    # df['prop_location_score2'] = loc_score2

    # # trim hist price
    # hist_price = df['prop_log_historical_price'].to_numpy()
    # trimmed_hist_price = trim_hist_price(hist_price)
    # df['prop_log_historical_price'] = trimmed_hist_price

    # trim price
    id = df['srch_id'].to_numpy()
    price = df['price_usd'].to_numpy()
    trimmed_price = trim_price(id, price)
    df['price_usd'] = trimmed_price

    # # trim booking window
    # booking_window = df['srch_booking_window'].to_numpy()
    # trimmed_booking_window = trim_booking_window(booking_window)
    # df['srch_booking_window'] = trimmed_booking_window

    # # trim destination distance
    # dest_dist = df['orig_destination_distance'].to_numpy()
    # trimmed_dest_dist = trim_dest_dist(dest_dist)
    # df['orig_destination_distance'] = trimmed_dest_dist


    #Hotel quality (2nd place feature engineering solution)
    hotel_quality = pd.DataFrame(df.prop_id.value_counts(dropna = False))

    hotel_quality = hotel_quality.join(pd.DataFrame(df.prop_id[df.booking_bool == 1].value_counts().astype(int)), rsuffix = "book")
    hotel_quality = hotel_quality.join(pd.DataFrame(df.prop_id[df.click_bool == 1].value_counts().astype(int)), rsuffix = "click")
    hotel_quality.columns = ["counts", "booked", "clicked"]


    hotel_quality["%booked_prop"] = hotel_quality.booked / hotel_quality.counts * 100
    hotel_quality["%clicked_prop"] = hotel_quality.clicked / hotel_quality.counts * 100

    df = df.join(hotel_quality['%booked_prop'], on = "prop_id").fillna(0)
    df = df.join(hotel_quality['%clicked_prop'], on = "prop_id").fillna(0)

    # #Add the same features to the test set
    # test = test.join(hotel_quality['%booked_prop'], on = "prop_id")
    # test = test.join(hotel_quality['%clicked_prop'], on = "prop_id")
    
    
    print("--- trimming took %s seconds ---" % (round(time.time() - start_time)))
    
    return df

df_old = pd.read_csv("../training_set_VU_DM.csv")
df_new = pd.read_csv("../train2.csv")

# df = pd.read_csv("small_data/cleaned_data_50000.csv")
df_old = trim_data(df_old)
df_new['position'] = df_old['position']
df_new['price_usd'] = df_old['price_usd']
# df_new['booking_bool'] = df_old['booking_bool']
# df_new = df_new.drop(columns=["Unnamed: 0"])

df_new.to_csv('../train2.csv')

