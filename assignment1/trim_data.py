import csv
from numpy.core.numeric import NaN
import pandas as pd
import dateparser
import datetime
import copy


def trim_programma():
    program_abbrev = {
    'AI':'Artificial Intelligence',
    'BA':'Business Administration',
    'CS':'Computer Science',
    'CLS':'Computional Science',
    'EDS':'Econometrics and Data Science',
    'EOR':'Econometrics and Operations Research',
    'HLT':'Human Language Technology',
    'OR':'Operations Research',
    'QRM':'Quantitative Risk Management',
    }

    stop_words = ['MSC', 'MASTERS', 'MASTER OF SCIENCE', 'MASTER', '(UVA)', ':', 'UVA', ' AT', '@']
    
    programs = df.iloc[:, 1]

    for i in range(len(programs)):
        # change input to upper case
        programs[i] = programs[i].upper()

        # remove stopwords
        for word in stop_words:
            if word in programs[i]:
                programs[i] = programs[i].replace(word, '')
        
        # change abbreviations to full program names 
        for abbrev in program_abbrev:
            # separate words, so that business analytics != business analyticomputational science
            prog_split = programs[i].split()

            if abbrev in prog_split:
                programs[i] = programs[i].replace(abbrev, program_abbrev[abbrev])

        # make only the first letter upper case and remove unnecessary spaces
        programs[i] = programs[i].lower()
        prog_words = programs[i].split()
        for j in range(len(prog_words)):
            if prog_words[j] == 'M':
                prog_words.remove(prog_words[j])
                continue
    
            prog_words[j] = prog_words[j].capitalize()
            # remove 'M' if this is the case (can't be in stop_words due to words containing 'M')
        
        programs[i] = " ".join(prog_words)
        



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
    pass

def trim_RN():
    rn = df.iloc[:, 13]

    for i in range(len(rn)):
        try:
            rn[i] = int(round(float(rn[i])))
        except:
            rn[i] = None

def trim_bedtime():
    """ it aint pretty but it does the job, a lot of different types of tiems are entered and we are filtering a lot like this """
    bed = df.iloc[:, 14]

    for i in range(len(bed)):
        bed[i] = bed[i].replace(" ", "")
        bed[i] = bed[i].replace("24", "00")
        bed[i] = bed[i].replace(".", ":")

        if "?" in bed[i]:
            bed[i] = None
            continue
        if "pm" in bed[i] or "PM" in bed[i]:
            bed[i] = bed[i].replace("pm", "")
            bed[i] = bed[i].replace("PM", "")
        elif "am" in bed[i] or "AM" in bed[i] or "a.m." in bed[i]:
            bed[i] = bed[i].replace("am", "")
            bed[i] = bed[i].replace("AM", "")
            bed[i] = bed[i].replace("a.m.", "")

        try:
            int(bed[i])
            if len(str(bed[i])) == 1:
                bed[i] = "0" + str(bed[i]) + ":00"
            if len(str(bed[i])) == 2:
                if int(bed[i]) > 24:
                    bed[i] = None
                else:
                    if int(bed[i]) > 6 and int(bed[i]) < 12:
                        bed[i] = int(bed[i]) + 12

                    if int(bed[i]) == 24:
                        bed[i] = "00"

                    bed[i] = str(bed[i]) + ":00"
            elif len(str(bed[i])) == 4:
                bed[i] = str(bed[i][0:2]) + ":" + str(bed[i][2:])
        except:
            pass

        try:
            bed[i] = datetime.datetime.strptime(bed[i], '%H:%M').time()
        except:
            try:
                bed[i] = datetime.datetime.strptime(bed[i], '%H.%M').time()
            except:
                try:
                    bed[i] = datetime.datetime.strptime(bed[i], '%H').time()
                except:
                    bed[i] = None

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
# trim_good_day()
