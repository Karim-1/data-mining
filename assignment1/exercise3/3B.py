import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

from scipy.optimize import curve_fit
from statsmodels.formula.api import ols
from rdatasets import data
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.linear_model import LinearRegression


def MSE(residuals, n):
    return sum([x**2 for x in residuals]) / n
    
def MAE(residuals, n):
    return sum([abs(x) for x in residuals]) / n

def linear(df):
    def objective(x, a, b):
         return a * x + b 
    
    age = df['age']
    size = df['circumference']
    
    popt, _ = curve_fit(objective, age, size)
    a, b = popt
    
    n = len(age)
    
    x_line = np.linspace(min(age), max(age), n)
    y_line = np.linspace(min(size), max(size), n)

    # calculate residuals 
    residuals = []
    for i in range(n):
        # residuals.append(objective(age[i], a, b) - size[i])
        residuals.append(y_line[i] - size[i])
    
    # print mean square error and mean absolute error
    print('linear MSE:', MSE(residuals, n))
    print('linear MAE:', MAE(residuals, n))
    
    return x_line, y_line

    
def fitted(df):

    def objective(x, a, b, c, d, e):
         return a * x**4 + b * x**3 + c * x**2 + d * x + e
    
    age = df['age']
    size = df['circumference']
    
    popt, _ = curve_fit(objective, age, size)
    a, b, c, d, e = popt
    
    # define a sequence of inputs between the smallest and largest known inputs
    x_line = np.arange(min(age), max(age), 1)
    
    # calculate the output for the range
    y_line = objective(x_line, a, b, c, d, e)

    # calculate residuals 
    n = len(age)
    residuals = []
    for i in range(n):
        residuals.append(objective(age[i], a, b, c, d, e) - size[i])
    
    # print mean square error and mean absolute error
    print('\nfitted MSE:', MSE(residuals, n))
    print('fitted MAE:', MAE(residuals, n))
    
    return x_line, y_line

# load data
df = data("Orange")
age = df['age']
size = df['circumference']

# predict values with models
linear_x, linear_y = linear(df)
fitted_x, fitted_y = fitted(df)

# plot data + predicted lines
plt.scatter(age, size, color = 'orange', label='actual values')
plt.plot(fitted_x, fitted_y, '--b', label='good fit')
plt.plot(linear_x, linear_y, '--r', label='bad fit')
plt.xlabel('Age (days)')
plt.ylabel('Circumference')
plt.legend()
plt.show()