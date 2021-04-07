import csv
import datetime
import pandas as pd


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
    # daan
    gender = df.iloc[:, 6]
    # all genders are conform the list, so no trimming needed
    genders = ["male", "female", "unknown"]
    # if gender not in genders:
    #     print(gender)
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
