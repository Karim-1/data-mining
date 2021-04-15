import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

from scipy.optimize import curve_fit
from statsmodels.formula.api import ols
from rdatasets import data
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.linear_model import LinearRegression


def lm(df):
    # split into two variables
    age = df['age']
    size = df['circumference']

    # calculate slope 
    slope, intercept = np.polyfit(age, size, 1)

    # define predicted values based on regression methods
    predicted_size_lm = slope*age + intercept

    print('MSE = ', mean_squared_error(size, predicted_size_lm))
    print('MAE = ', mean_absolute_error(size, predicted_size_lm))

    plt.scatter(age, size, color = 'orange', label='actual values')
    plt.vlines(age, predicted_size_lm, size, color='r', linewidth=.5, linestyle='dashed', label='residuals')
    # plt.scatter(age, size, color = 'orange', s=size/2)
    plt.plot(age, predicted_size_lm, linewidth=.5, color='black', label='predicted values')
    plt.xlabel('Age (days)')
    plt.ylabel('Circumference')
    plt.grid()
    plt.legend()
    plt.show()


def split_data(data):
    # shuffle data to prevent bias
    df = data.sample(frac=1)

    rowcount = len(df.index)
    train_data = df.head(30)
    test_data = df.tail(rowcount-30, columns=['age','circumference'])
    print(train_data)
    print(test_data)

    return train_data, test_data

def lg(df):
    train_data, test_data = split_data(df)

    regression = LinearRegression().fit(train_data, test_data)
    plt.plot(regression)
    plt.show()

# load data
df = data("Orange")
# lm(df)
lg(df)