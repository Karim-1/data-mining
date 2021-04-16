import csv
import nltk
import numpy as np
import string
import re

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split


def read_file(filename):
    '''
    reads file and separates label from texts
    '''
    labels, texts = [], []
    with open(filename) as file:
        csvreader = csv.reader(file, delimiter = '\n')
        next(csvreader)        
        for row in csvreader:
            row = row[0].split(';',1)
            labels.append(row[0])
            texts.append(row[1])

    return labels, texts


def transform_data(texts):
    '''
    prepares data for analysis
    '''
    for i in range(len(texts)):
        # make all texts lower
        texts[i] = texts[i].lower() 
        
        # remove punctuation
        texts[i] = re.sub(r'[^\w\s]', '', texts[i])

        # remove double space
        texts[i] = texts[i].replace('  ', ' ')

        # remove numbers
        texts[i] = ''.join([i for i in texts[i] if not i.isdigit()])
    
    return texts

# retrieve labels and texts from csv file
labels, raw_texts = read_file('SmsCollection.csv')

# clean up text messages
clean_texts = transform_data(raw_texts)

# create counts vectorizer with max 1500 bags of words, min of 5 word occurences, and filter words that are in > 70% of texts
tfidfconverter = TfidfVectorizer(max_features=1000, min_df=5, max_df=0.7)
bags_of_words = tfidfconverter.fit_transform(clean_texts).toarray()

# split into training and testing set
X_train, X_test, y_train, y_test = train_test_split(bags_of_words, labels, test_size=0.1, random_state=0)

# define classifier
classifier = RandomForestClassifier(n_estimators=1000, random_state=0)

# fit training data to classifier
classifier.fit(X_train, y_train) 

# predict values 
y_pred = classifier.predict(X_test)

print('Confusion matrix:')
print(confusion_matrix(y_test,y_pred))
print('\nClassification report:')
print(classification_report(y_test,y_pred))
print('\nAccuracy score:')
print(accuracy_score(y_test, y_pred))




