# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 14:45:08 2023

@author: syeda
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns


cancer_data=pd.read_csv('D:\\sakeena-desktop\\Research Paper\\cancer.csv')
cancer_data=cancer_data.drop(labels = ["index","Patient_Id"], axis = 1)
print(cancer_data.head(20))
df=pd.DataFrame(cancer_data)
labels1 = cancer_data['Age']
age = cancer_data['Age']

# Create a pie chart
plt.figure(figsize=(6, 6))
plt.pie(age, labels=labels1, autopct='%1.1f%%', startangle=90)
plt.title('Sample Pie Chart')

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Show the chart
plt.show()