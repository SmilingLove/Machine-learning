# -*- coding: utf-8 -*-
"""SDN_PROJECT_ML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14ugWHrST3Coi54x43RoAdsqP_WprKuqp
"""

import os
import sys
import tensorflow as tf
from tensorflow import keras
import numpy as np
from itertools import combinations
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

train_data=[]
train_labels=[]
test_data=[]
test_labels=[]

N=128

dataset_dir='./content/'
dataset_name=['xbee']

if len(sys.argv)>1:
    dataset_name[0]=sys.argv[1]

for dataset in dataset_name:
    lines=open('xbee_normal.txt','r').readlines()
    for i,line in enumerate(lines):
        strlist=np.array(line.split())
        if i%5==0:
            test_data.append(strlist.astype(np.float))
            test_labels.append(0)         
        else:
            train_data.append(strlist.astype(np.float))
            train_labels.append(0)

for dataset in dataset_name:
    lines=open('xbee_attack.txt','r').readlines()
    for i,line in enumerate(lines):
        strlist=np.array(line.split())
        if i%5==0:
            test_data.append(strlist.astype(np.float))
            test_labels.append(1)         
        else:
            train_data.append(strlist.astype(np.float))
            train_labels.append(1)


train_labels=np.array(train_labels)
train_data=np.array(train_data)

test_labels=np.array(test_labels)
test_data=np.array(test_data)

train_data = train_data/255
test_data = test_data/255

"""##**Logistic Regression**"""

from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

log = LogisticRegression ()
log.fit(train_data,train_labels)
predictions = log.predict(test_data)
accuracy_score(test_labels,predictions)

print(classification_report(test_labels,predictions))

import seaborn as sns
cf = confusion_matrix(test_labels,predictions)
sns.heatmap(cf,annot=True,fmt = 'd',cmap = 'Blues')
plt.title('Logistic Regression')
plt.xlabel('Predicted values')
plt.ylabel('True values')
plt.show()

"""##**KNN**"""

from sklearn.neighbors import KNeighborsClassifier

log = KNeighborsClassifier()
log.fit(train_data,train_labels)
predictions = log.predict(test_data)
print(accuracy_score(test_labels,predictions))

cf = confusion_matrix(test_labels,predictions)
sns.heatmap(cf,annot=True,fmt = 'd',cmap = 'Reds')
plt.title('KNN')
plt.xlabel('Predicted values')
plt.ylabel('True values')
plt.show()

print(classification_report(test_labels,predictions))

"""##**Decision Tree**"""

from sklearn.tree import DecisionTreeClassifier

log = DecisionTreeClassifier()
log.fit(train_data,train_labels)
predictions = log.predict(test_data)
print(accuracy_score(test_labels,predictions))

cf = confusion_matrix(test_labels,predictions)
sns.heatmap(cf,annot=True,fmt = 'd',cmap = 'Greens')
plt.title('Decision Tree')
plt.xlabel('Predicted values')
plt.ylabel('True values')
plt.show()

print(classification_report(test_labels,predictions))

"""##**SVM**"""

from sklearn.svm import SVC

log = SVC()
log.fit(train_data,train_labels)
predictions = log.predict(test_data)
print(accuracy_score(test_labels,predictions))

cf = confusion_matrix(test_labels,predictions)
sns.heatmap(cf,annot=True,fmt = 'd',cmap = 'copper')
plt.title('SVM')
plt.xlabel('Predicted values')
plt.ylabel('True values')
plt.show()

print(classification_report(test_labels,predictions))