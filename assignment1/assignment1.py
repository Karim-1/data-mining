import csv
from tqdm import tqdm
import numba
import pandas as pd

def daan2():
    with open("ODI-2021.csv") as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            print(row)
            break




def karim(data):
    pass

def daan(data):
    last_8 = data.columns[9:]
    print(len(last_8))

    for column in last_8:
        data[column] = data[column].fillna(0)
        column_data = data[column]

        # check which column, if column 0 then number of neighbours
        count=0
        if column == last_8[0]:
            for row in data[column]:
                if not str(row).isdigit():
                    print(row)
                    count+=1
            
            print("hoi", count)
        
        break

ODI_2021 = pd.read_csv("ODI-2021.csv")
karim(ODI_2021)
daan(ODI_2021)