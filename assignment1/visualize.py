import pandas as pd
import matplotlib.pyplot as plt

def pie_chart(data):
    # count number of times similar values are in a list
    data_counts = {i:data.count(i) for i in data}
    total_data_counts = sum(data_counts.values())
    
    # only use keys with values > 4, put rest in 'Other'
    relevant_data_counts = {k:v for (k,v) in data_counts.items() if v > 4}
    other_count = total_data_counts - sum(relevant_data_counts.values())
    if other_count:
        relevant_data_counts['Other'] = other_count

    # put values in labels
    labels = relevant_data_counts.keys()
    sizes = relevant_data_counts.values()

    # create pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, startangle=90)
    ax1.axis('equal')  

    plt.show()



df = pd.read_csv('data/ODI-2021_trimmed.csv')
programs = list(df.iloc[:, 2])
took_ML = list(df.iloc[:, 3])
took_IR = list(df.iloc[:, 4])
took_Stats = list(df.iloc[:, 5])
took_DB = list(df.iloc[:, 6])
gender = list(df.iloc[:, 7])

# pie_chart(programs)
pie_chart(took_ML)
# pie_chart(took_IR)
# pie_chart(took_Stats)
# pie_chart(took_DB)
# pie_chart(gender)