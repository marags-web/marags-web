# -*- coding: utf-8 -*-
"""IDS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/marags-web/marags-web/blob/main/IDS.ipynb
"""

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

##---------Type the code below this line------------------##
# Downloading the csv file from your GitHub account
url =  "https://raw.githubusercontent.com/marags-web/marags-web/main/IDS/data/Train.txt"

#import os
#for dirname, _, filenames in os.walk('/IDS/data'):
 #   for filename in filenames:
  #      print(os.path.join(dirname, filename))
   #     print("inside for")

import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns
import time
import multiprocessing

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from collections import Counter
from sklearn.preprocessing import LabelEncoder, StandardScaler

from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE, ADASYN
from sklearn.metrics import confusion_matrix, r2_score, mean_squared_error
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, accuracy_score, classification_report, precision_recall_curve
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv(url,sep=",",names=["duration","protocoltype","service","flag","srcbytes","dstbytes","land", "wrongfragment","urgent","hot","numfailedlogins","loggedin", "numcompromised","rootshell","suattempted","numroot","numfilecreations", "numshells","numaccessfiles","numoutboundcmds","ishostlogin","isguestlogin","count","srvcount","serrorrate", "srvserrorrate","srerrorrate","srvrerrorrate","samesrvrate", "diffsrvrate", "srvdiffhostrate","dsthostcount","dsthostsrvcount","dsthostsamesrvrate", "dsthostdiffsrvrate","dsthostsamesrcportrate","dsthostsrvdiffhostrate","dsthostserrorrate","dsthostsrvserrorrate","dsthostrerrorrate","dsthostsrvrerrorrate","attack", "lastflag"])
df.head()

df.shape

df.describe()

df.drop(['land','urgent','numfailedlogins','numoutboundcmds'],axis=1,inplace=True)

df.isna().sum()

df.select_dtypes(exclude=[np.number])

df['attack'].loc[df['attack']!='normal']='attack'
le = LabelEncoder()

#df = pd.DataFrame(columns=["flag", "attack"])

#for i in range(2):
#    this_column = df.columns[i]
#    df[this_column] = [i, i+1]

#print(df)

#import zmq
#from time import sleep
#context = zmq.Context()
#socket = context.socket(zmq.PUB)
#socket.connect('tcp://demo:2000')
#while(True):
#    socket.send_pyobj({"attack"})

import socket
#HOST = socket.gethostbyname('ids-demo')# Standard loopback interface address (localhost)
HOST = 'ids-demo'
PORT = 9898        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(HOST, PORT)
    s.listen()
    conn, addr = s.accept()

#   with conn:
        #print('Connected by', addr)

    while True:
        data = (b'attack')
        #if not data:
        #   break
        conn.sendall(data)


df['protocoltype']=le.fit_transform(df['protocoltype'])
df['service']=le.fit_transform(df['service'])
df['flag']=le.fit_transform(df['flag'])
df['attack']=le.fit_transform(df['attack'])

plt.figure(figsize=(20,15))
sns.heatmap(df.corr())

X=df.drop(['attack'],axis=1)
y=df['attack']

sns.countplot(df['attack'])

print("Class distribution: {}".format(Counter(y)))

scaler = StandardScaler()
scaler.fit(X)
X_transformed = scaler.transform(X)

#Using Logistic Regression 
lr=LogisticRegression()
lr.fit(X_transformed,y)
lr_pred=lr.predict(X_transformed)
print(lr_pred)

lr_df=pd.DataFrame()
lr_df['actual']=y
lr_df['pred']=lr_pred

lr_df.head()

print(accuracy_score(y, lr_pred))

confusion_matrix(y, lr_pred)

print(classification_report(y, lr_pred))
