import csv
from os import name
from tqdm import tqdm
import numba

def karim():
    pass

def daan():
    with open("ODI-2021.csv") as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            print(row)
            break


if __name__ == "__main__":
    print("hoi")
    daan()

