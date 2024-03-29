# -*- coding: utf-8 -*-
"""Copy of titanicpred.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zlWGUDjAI4Pcb9VQqJ6ue48BVAMh5emi
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("/content/test.csv")
df

df.info()

df.isnull().sum()

df=df.fillna(0)
df

sns.countplot(x='Survived', hue='Pclass', data=df)

df.drop("Cabin",inplace=True,axis=1)

df.drop("Name",inplace=True,axis=1)
df.drop("Sex",inplace=True,axis=1)
df.drop("Ticket",inplace=True,axis=1)
df.drop("Embarked",inplace=True,axis=1)

X = df.drop("Survived",axis=1)
y = df["Survived"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 101)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)
y_pred

y_test

# from sklearn.metrics import classification_report
# print(classification_report(y_test, y_pred))

from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)