# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 22:08:56 2023

@author: syeda
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics


cancer_data=pd.read_csv('D:\\sakeena-desktop\\Research Paper\\cancer.csv')
cancer_data=cancer_data.drop(labels = ["index","Patient_Id"], axis = 1)


feature_col=cancer_data[['Age','Gender','Air_Pollution','Alcohol_use','Dust_Allergy',
                         'OccuPational_Hazards','Genetic_Risk','chronic_Lung Disease','Balanced_Diet',
                         'Obesity','Smoking','Passive_Smoker','Chest_Pain','Coughing_of_Blood','Fatigue',
                         'Weight_Loss','Shortness_of_Breath','Wheezing','Swallowing_Difficulty','Clubbing_of_Finger_Nails',
                         'Frequent_Cold','Dry_Cough','Snoring']]
x=feature_col
y=cancer_data['Level']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.50)
model=DecisionTreeClassifier()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
df=pd.DataFrame({'  Actual Value': y_test,'   Predicted Value':y_pred})

cnf=metrics.confusion_matrix(y_test, y_pred)
accuracy=metrics.accuracy_score(y_test, y_pred)
precision=metrics.precision_score(y_test, y_pred,average=None)
recall = metrics.recall_score(y_test, y_pred, average=None)
print()
print()
print("----------------------------------------------------------------------------")
print("                            WELCOME TO ONLINE HOSPITAL                      ")
print("----------------------------------------------------------------------------")
print()
print("                            Prediction Of Lung Cancer                       ")
print() 
print("Enter the following details to Ensure Whether there is a presence of cancer or not:")
age=int(input("Enter your Age: "))
name=input("Enter your Name: ")
gender=int(input("Specify your gender( if male enter 1, if female enter 2): - "))
print("For the Following details provide ratings from 1-10")
print("0 indicates no")
print("1-3 for begining level")
print("4-6 for Average level")
print("7-10 for worst level")
print()
print()
air=int(input("The level of air pollution exposure, rate from(0-10): "))
alcohol=int(input("Alcohol Usage in a month, rate from(0-10): "))
dust=int(input("The level of dust allergy, rate from(0-10): "))
occupation=int(input("Have you had long-term exposure to occupational hazards like asbestos, radon, or certain chemicals? rate from(0-10): "))
genetic=int(input("Does your family have a history of cancer,answer in this form(0-10): "))
chronic=int(input("The level of chronic lung disease, rate from(0-10): "))
balanced=int(input("The level of balanced diet, rate from(0-10): "))
obesity=int(input("Have you experienced unexplained weight loss or weight gain recently?, rate from( 0-10): "))
smoking=int(input("Have you ever smoked in the past, and if so, how many cigarettes per day?, answer in the from(0-10): "))
passive=int(input("Are you exposed to secondhand smoke regularly?, answer in the form(0-10): "))
chest=int(input("Are you experiencing chest pain or discomfort?, rate from(0-10): "))
cough=int(input("Have you coughed up blood or blood-tinged mucus? rate from(0-10): "))
fatigue=int(input("Do you feel persistently tired or fatigued, even after getting enough rest? rate from(1-10): "))
weight=int(input("Have you experienced unexplained weight loss recently? rate from(1-10): "))
short=int(input("Are you experiencing shortness of breath? rate from(1-10): "))
wheez=int(input("Are you experiencing wheezing? rate from(1-10): "))
swallow=int(input("Have you noticed changes in your appetite or difficulty swallowing? rate from(1-10): "))
club=int(input("Level of Clubbing of Finger Nails, rate from(1-10): "))
cold=int(input("Do you experience frequent cold symptoms, such as a runny or stuffy nose, sneezing, coughing, or sore throat?  rate from(1-10): "))
dcough=int(input("Level of Dry Cough, rate from(1-10): "))
snoring=int(input("Rate your Snoring from(1-10): "))
print()
print()


userInput =[[age,gender,air,alcohol,dust,occupation,genetic,chronic,balanced,obesity,smoking
             ,passive,chest,cough,fatigue,weight,short,wheez,swallow,
             club,cold,dcough,snoring]]
df_u = pd.DataFrame(userInput, columns=['Age','Gender','Air_Pollution','Alcohol_use','Dust_Allergy',
                         'OccuPational_Hazards','Genetic_Risk','chronic_Lung Disease','Balanced_Diet',
                         'Obesity','Smoking','Passive_Smoker','Chest_Pain','Coughing_of_Blood','Fatigue',
                         'Weight_Loss','Shortness_of_Breath','Wheezing','Swallowing_Difficulty','Clubbing_of_Finger_Nails',
                         'Frequent_Cold','Dry_Cough','Snoring'])
a=model.predict(df_u)

if(a=="Low"):
    print("No need to consult an doctor, You are Perfectly Fine.")
elif(a=="Medium"):
    print("First You need to reduce consumption of cigrattes and alcohol, and consult an doctor for getting the cancer in control.")
    print("The Risk Level is: ",a)
else:
    print("You are in the worst state need to consult an doctor immediately ")
    print("The Risk Level is: ",a)