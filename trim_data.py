import csv
from numpy.core.numeric import NaN
import pandas as pd
from datetime import datetime
import dateparser
import copy


def trim_programma():
    programme = df.iloc[:, 1]
    pass

def trim_prev_courses():
    # marlon
    courses = df.iloc[:, 2:6]
    pass

def trim_gender():
    gender = df.iloc[:, 6]
    # all genders are conform the list, so no trimming needed
    genders = ["male", "female", "unknown"]
    for sex in gender:
        if sex not in genders:
            print("if you seet his we need to trim more:", sex)
    pass

def trim_choc():
    chocolate = df.iloc[:, 7]
    # five radio options from the form so no trimming needed
    pass

def trim_birthday():
    birthday = df.iloc[:, 8]

    for i in range(len(birthday)):
        birthday[i] = dateparser.parse(birthday[i])
        if birthday[i] != None:
            birthday[i] = birthday[i].date()

def trim_neighbours():
    neighbours = df.iloc[:, 9]
    # print(neighbours)

    for i in range(len(neighbours)):
        if not str(neighbours[i]).isdigit():
            # old = neighbours[i]
            neighbours[i] = None

def trim_stand():
    standing = df.iloc[:, 10]
    correct_options = ["yes", "no", "unknown"]

    for row in standing:
        if row not in correct_options:
            print("standing needs trimming:", row)

def trim_stress():
    stress = df.iloc[:, 11]
    count = 0
    
    for i in range(len(stress)):
        
        try:
            if int(stress[i]) > 100:
                stress[i] = 100
            elif int(stress[i]) < 0:
                stress[i] = 0
        except:
            stress[i] = None

def trim_competition():
    comp = df.iloc[:, 12]
    # print(comp)

    # for i in range(len(comp)):
    #     try:
    #         int(comp[i])
    #     except:
    #         print(comp[i])
    pass

def trim_RN():
    rn = df.iloc[:, 13]

    for i in range(len(rn)):
        try:
            rn[i] = int(round(float(rn[i])))
        except:
            rn[i] = None

def trim_bedtime():
    bed = df.iloc[:, 14]
    print(bed)

    for i in range(len(bed)):
        bed[i] = bed[i].replace(".", ":")
        bed[i] = bed[i].replace(",", ":")

        if ":" in bed[i]:
            bed[i] = bed[i].replace("am", "")
            if "pm" in bed[i]:
                bed[i] = bed[i].replace("pm", "")
                temp = bed[i].split(":")
                temp[0] = str(int(temp[0]) + 12)
                bed[i] = ":".join(temp)
        elif "pm" in bed[i] or "PM" in bed[i]:
            bed[i] = bed[i].replace("pm", "")
            bed[i] = bed[i].replace("PM", "")
            bed[i] = int(bed[i]) + 12
            bed[i] = str(bed[i]) + ":00"
        elif "am" in bed[i] or "AM" in bed[i]:
            bed[i] = bed[i].replace("am", "")
            bed[i] = bed[i].replace("AM", "")
        else:
            try:
                int(bed[i])
                if len(str(bed[i])) == 2:
                    print(bed[i])
                    if int(bed[i]) > 24:
                        bed[i] = None
                    else:
                        pass
            except:
                # print("oh shit")
                pass
                # print(bed[i])

def trim_good_day():
    pass



df = pd.read_csv("ODI-2021.csv")

# trim_programma()
# trim_prev_courses()
# trim_gender()
# trim_choc()
# trim_birthday()
# trim_neighbours()
# trim_stand()
# trim_stress()

# trim_competition()
# trim_RN()

trim_bedtime()
trim_good_day()