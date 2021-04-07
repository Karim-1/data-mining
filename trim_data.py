import csv
import datetime
import pandas as pd


def trim_programma():
    programme = df.iloc[:, 1]
    pass

def trim_prev_courses():
    # marlon
    courses = df.iloc[:, 2:6]
    pass

def trim_gender():
    # daan
    gender = df.iloc[:, 6]
    # all genders are conform the list, so no trimming needed
    genders = ["male", "female", "unknown"]
    if gender not in genders:
        print(gender)
    pass

def trim_choc():
    chocolate = df.iloc[:, 7]
    # five radio options from the form so no trimming needed
    pass

def trim_birthday():
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
          'august', 'september', 'october', 'november', 'december']
    pass

def trim_neighbours():
    pass

def trim_stand():
    pass

def trim_stress():
    pass

def trim_competition():
    pass

def trim_RN():
    pass

def trim_bedtime():
    pass

def trim_good_day():
    pass



df = pd.read_csv("ODI-2021.csv")

trim_programma()
trim_prev_courses()
trim_gender()
trim_choc()
trim_birthday()
trim_neighbours()
trim_stand()
trim_stress()
trim_competition()
trim_RN()
trim_bedtime()
trim_good_day()