import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def pie_chart(data, title):
    # count number of times similar values are in a list
    data_counts = {i:data.count(i) for i in data}
    total_data_counts = sum(data_counts.values())
    
    # only use keys with values > 4, put rest in 'Other'
    relevant_data_counts = {k:v for (k,v) in data_counts.items() if v > 4}
    other_count = total_data_counts - sum(relevant_data_counts.values())
    if other_count:
        relevant_data_counts['Other'] = other_count

    # retrieve values from dictionary
    labels = relevant_data_counts.keys()
    sizes = relevant_data_counts.values()

    # function to only show percentage if >5%
    def pct_filter(pct):
        return ('%.1f%%' % pct) if pct > 5 else ''

    # create pie chart
    fig1, ax1 = plt.subplots()
    patches, texts, autotexts = ax1.pie(sizes, labels=labels, startangle=90, autopct=pct_filter)
    # change font size if more than 4 labels
    if len(labels) > 4:
        texts = [text.set_fontsize(8) for text in texts]
    ax1.axis('equal')  
    # ax1.set_title(title)


def correlation(data, x_label, y_label):
    # sns.catplot(data=data)
    sns.catplot(x=x_label, y=y_label, kind="box", data=data)



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

- opmerking over ja/nee
    
'''

# pie_chart(programs, 'Background')
# pie_chart(took_ML, 'Took a course on machine learning?')
# pie_chart(took_IR, 'Took a course on information retrieval?')
# pie_chart(took_Stats, 'Took a course on statistics?')
# pie_chart(took_DB, 'Took a course on databases?')
# pie_chart(gender, 'Gender')

# plt.show()

# gender_vs_stress = pd.DataFrame(gender, [float(i) for i in stress])
# for i in range(len(gender)):
#     if gender[i] == 'female':
#         gender[i] = 0
#     elif gender[i] == 'male':
#         gender[i] = 1
#     else:
#         gender[i] = 2

for i in range(len(gender)-1, 0, -1):
    try:
        stress[i] = int(stress[i])
    except:
        del stress[i]
        del gender[i]

gender_vs_stress = pd.DataFrame({'stress level': stress})
print(gender_vs_stress.head())
correlation('gender', 'stress level', gender_vs_stress)

# plt.show()