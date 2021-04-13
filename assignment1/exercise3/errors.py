from rdatasets import data
import pandas as pd
import matplotlib.pyplot as plt


df = data("Orange")
age = df['age']
size = df['circumference']

plt.scatter(age, size, color = 'orange', s=size)
plt.xlabel('age of the orange (days)')
plt.ylabel('circumference of the orange')
plt.show()
