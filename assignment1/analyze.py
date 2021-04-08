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


def correlation(var1, var2):
    plt.scatter(var1, var2)



df = pd.read_csv('data/ODI-2021_trimmed.csv')
programs = list(df.iloc[:, 2])
took_ML = list(df.iloc[:, 3])
took_IR = list(df.iloc[:, 4])
took_Stats = list(df.iloc[:, 5])
took_DB = list(df.iloc[:, 6])
took_courses = list(df.iloc[:, 3:6])
gender = list(df.iloc[:, 7])
choc = list(df.iloc[:, 8])
bday = list(df.iloc[:, 9])
neighbours = list(df.iloc[:, 10])
stand = list(df.iloc[:, 11])
stress = list(df.iloc[:, 12])
money = list(df.iloc[:, 13])
random_nr = list(df.iloc[:, 14])
bedtime = list(df.iloc[:, 15])
goodday1 = list(df.iloc[:, 15])
goodday2 = list(df.iloc[:, 16])

'''
ideeen:
- piecharts van categoriale vragen
- correlaties tussen:
    - stress + (gender, programs, neighbours, prev_courses, bedtime) [Karim]
    - Stats + ML, IR, DB (mu/sigma = nee/ja?) [Karim]
    - choc + gender [Karim]
    - neighbours + stand
    - program + money
- goodday1 + goodday2 wordcounts [Daan]
- random_nr (uniform histogram?) [Daan]
    
'''



# pie_chart(programs)
# pie_chart(took_ML)
# pie_chart(took_IR)
# pie_chart(took_Stats)
# pie_chart(took_DB)
# pie_chart(gender)

# correlation(gender, stress)

# plt.show()