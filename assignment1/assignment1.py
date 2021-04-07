import csv
from tqdm import tqdm
import numba
import pandas as pd

def karim(data):
    for line in data:
        print(line)
        break
        # tranform programme names
        programme = line[1].upper()
        # remove words that are not needed
        stopwords = ['MSC', 'MASTERS', 'MASTER', 'OF', 'SCIENCE', 'IN']
        words = ' '.join(filter(lambda x: x.lower() not in stopwords, programme.split()))
        letters = [word[0].upper() for word in row[1].split()]
        print("".join(letters))

def daan():
    data = pd.read_csv("ODI-2021.csv")
    last_8 = data.columns[9:]
    print(len(last_8))

    for column in last_8:
        data[column] = data[column].fillna(0)
        column_data = data[column]

        # check which column, if column 0 then number of neighbours
        count=0
        if column == last_8[0]:
            neighbours = []
            for row in data[column]:
                if not str(row).isdigit():
                    print(row)
                    count+=1
            
            print("hoi", count)
        
        break

# ODI_2021 = pd.read_csv("ODI-2021.csv", header=None, skiprows=1)

ODI_2021 = []
with open("ODI-2021.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        ODI_2021.append(row)

karim(ODI_2021)
# daan(ODI_2021)