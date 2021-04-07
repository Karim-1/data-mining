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


def trim_gender():
    pass


ODI_2021 = []
with open("ODI-2021.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        ODI_2021.append(row)