from numpy.lib.function_base import delete
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas.core.accessor import PandasDelegate
import math
import seaborn as sns

def pie_chart(data):
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

    # create pie chart
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, startangle=90)
    ax1.axis('equal')  


def correlation(data, x_label, y_label):
    # sns.catplot(data=data)
    sns.catplot(x=x_label, y=y_label, kind="box", data=data)

def random_nrs(data):
    data = [float(value) for value in data]
    data = [int(value) for value in data if not math.isnan(value)]
    data = sorted(data)
    data = np.array(data)

    x = [value for value in data if value < 1000000]

    count = {}

    for value in x:
        count[value] = x.count(value)

    # count = dict((k, v) for k, v in count.items() if v > 1)

    # count = dict(sorted(count.items(), key=lambda item: item[1]))

    labels = count.keys()
    counts = count.values()

    x = np.arange(len(labels))
    
    fig, ax = plt.subplots()
    ax.barh(x, counts)
    ax.set_yticks(x)
    ax.set_yticklabels(labels)
    ax.set_xlabel('Counts')
    ax.set_title('Counts of different random numbers')

    fig.tight_layout()
    plt.show()
    

    # fig.tight_layout()
    # plt.hist(data, orientation="horizontal")

    # ax.set_yticks()
    # plt.yticks(data)
    plt.show()

def good_day(day1, day2):  
    goodwords1 = set()
    goodwords2 = set()
    count = {}
    count1 = {}
    count2 = {}

    # first that comes to mind
    for good_day in day1:
        sentence = good_day.strip()
        words = (good_day.lower()).split(" ")
        for word in words:
            goodwords1.add(word)
            count[word] = 0
            count1[word] = 0
    
    # do same for 2nd day
    for good_day in day2:
        sentence = good_day.strip()
        words = (good_day.lower()).split(" ")
        for word in words:
            goodwords2.add(word)
            count[word] = 0
            count2[word] = 0

    # count words in both dicts
    for good_day in day1:
        for word in goodwords1:
            if word in good_day:
                count[word] += 1
                count1[word] += 1

    for good_day in day2:
        for word in goodwords2:
            if word in good_day:
                count[word] += 1
                count2[word] += 1

    # delete words with counts below threshold
    threshold = 8
    delete_counts = set()
    delete_extra = ["the", "with", "some", "out", "time", "for", "off", "nice", "good", "friends", "and", "day", "sunny", "work"]
    for key in delete_extra: delete_counts.add(key)

    for key in count.keys():
        if len(key) <= 2:
            delete_counts.add(key)
        elif count[key] < threshold: 
            delete_counts.add(key)

    for key in delete_counts: del count[key]

    count["no stress"] = count["stress"]
    count["friends"] = count["friend"]
    count["sports"] = count["sport"]

    delete_counts = ["stress", "friend", "sport"]
    for key in delete_counts: del count[key]

    # sort counts from low to high
    count = dict(sorted(count.items(), key=lambda item: item[1]))

    labels = count.keys()
    counts = count.values()

    x = np.arange(len(labels))
    
    fig, ax = plt.subplots()
    ax.barh(x, counts)
    ax.set_yticks(x)
    ax.set_yticklabels(labels)
    ax.set_xlabel('Counts')
    ax.set_title('Counts of different key words')

    fig.tight_layout()
    plt.show()

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
goodday1 = list(df.iloc[:, 16])
goodday2 = list(df.iloc[:, 17])

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

random_nrs(random_nr)

good_day(goodday1, goodday2)

# gender_vs_stress = pd.DataFrame(gender, [float(i) for i in stress])
# for i in range(len(gender)):
#     if gender[i] == 'female':
#         gender[i] = 0
#     elif gender[i] == 'male':
#         gender[i] = 1
#     else:
#         gender[i] = 2

# for i in range(len(gender)-1, 0, -1):
#     try:
#         stress[i] = int(stress[i])
#     except:
#         del stress[i]
#         del gender[i]

# gender_vs_stress = pd.DataFrame({'stress level': stress})
# print(gender_vs_stress.head())
# correlation('gender', 'stress level', gender_vs_stress)

# print(goodday2)
