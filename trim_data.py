import csv

def trim_programma():
    pass

def trim_prev_courses(arg1, arg2, arg3, arg4):
    # marlon
    pass

def trim_gender(arg1):
    # daan
    pass

def trim_choc(arg1):
    pass 

def trim_birthday():
    pass

def trim_birthday():
    pass

def trim_neighbours():
    pass

def trim_birthday():
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

def trim_good_day(arg1, arg2):
    pass




ODI_2021 = []
with open("ODI-2021.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        ODI_2021.append(row)

for line in data:
    # tranform programme names
    programme = line[1].upper()
    # remove words that are not needed
    stopwords = ['MSC', 'MASTERS', 'MASTER', 'OF', 'SCIENCE', 'IN']
    words = ' '.join(filter(lambda x: x.lower() not in stopwords, programme.split()))
    letters = [word[0].upper() for word in row[1].split()]
    print("".join(letters))