import csv

def karim(data):
    for line in data:
        # tranform programme names
        programme = line[1].upper()
        # remove words that are not needed
        stopwords = ['MSC', 'MASTERS', 'MASTER', 'OF', 'SCIENCE', 'IN']
        words = ' '.join(filter(lambda x: x.lower() not in stopwords, programme.split()))
        letters = [word[0].upper() for word in row[1].split()]
        print("".join(letters))

def daan(data):
    pass

# ODI_2021 = pd.read_csv("ODI-2021.csv", header=None, skiprows=1)

ODI_2021 = []
with open("ODI-2021.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        ODI_2021.append(row)

print(ODI_2021)
# karim(ODI_2021)
# daan(ODI_2021)