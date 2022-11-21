
#1. Import dependencies

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras.layers import Dense, Dropout
from keras.models import Sequential
import json
import requests
url =  "https://raw.githubusercontent.com/marags-web/marags-web/main/IDS/data/network_data_train.txt"

#2. Data Preprocessing
# data does not have column headers, so define them
headers = ["duration","protocol_type","service","flag","src_bytes",
           "dst_bytes","land","wrong_fragment","urgent","hot",
           "num_failed_logins","logged_in","num_compromised","root_shell",
           "su_attempted","num_root","num_file_creations","num_shells",
           "num_access_files","num_outbound_cmds","is_host_login",
           "is_guest_login","count","srv_count","serror_rate", 
           "srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate", 
           "diff_srv_rate", "srv_diff_host_rate","dst_host_count",
           "dst_host_srv_count","dst_host_same_srv_rate",
           "dst_host_diff_srv_rate","dst_host_same_src_port_rate",
           "dst_host_srv_diff_host_rate","dst_host_serror_rate",
           "dst_host_srv_serror_rate","dst_host_rerror_rate",
           "dst_host_srv_rerror_rate","attack", "last_flag"]

# read csv
data = pd.read_csv(url, names=headers)

# choose relevent features
features = ['duration','src_bytes','dst_bytes','num_file_creations', 
           'num_shells','num_failed_logins','wrong_fragment', 
           'urgent', 'is_guest_login', 'su_attempted', 'land', 'attack']
df = data[features]
pd.set_option('display.max_columns', None)
print(df.head())
   
# data has too many classes
# to simplify problem, categorize them generic network attack types : Probing, U2R, R2L, and DOS

class_labels = ['normal', 'dos', 'probing', 'u2r', 'r2l']

dos = ['neptune', 'apache2', 'processtable', 'smurf', 'back', 'snmpguess', 'mailbomb', 'snmpgetattack',
              'pod', 'multihop', 'teardrop', 'sqlattack', 'land']
probing = ['mscan', 'satan', 'saint', 'portsweep', 'ipsweep', 'nmap', 'spy']
u2r = ['buffer_overflow', 'ps', 'xterm', 'perl', 'loadmodule', 'imap']
r2l = ['guess_passwd', 'warezmaster', 'httptunnel', 'named', 'sendmail', 'xlock','xsnoop', 'rootkit', 
       'ftp_write', 'worm', 'phf', 'udpstorm', 'warezclient']

# replace all values in dataframe with corresponding int value

df['attack'].replace('normal', 0, inplace=True)
df['attack'].replace(dos, 1, inplace=True)
df['attack'].replace(probing, 2, inplace=True)
df['attack'].replace(u2r, 3, inplace=True)
df['attack'].replace(r2l, 4, inplace=True)

# shuffle the data
df['attack'].value_counts()

# split data into inputs/outputs
features = df[['duration','src_bytes','dst_bytes','num_file_creations', 
           'num_shells','num_failed_logins','wrong_fragment', 
           'urgent', 'is_guest_login', 'su_attempted', 'land']]
labels = df['attack']

X = np.array(features)
y = np.array(labels).reshape(-1, 1)

# make sure both arrays have correct dimensions
print(X.shape)
print(y.shape)
(125973, 11)
(125973, 1)


# 3. Buiding the model
import timeit
start = timeit.default_timer()

model = Sequential()

model.add(Dense(units=32, activation='relu', input_dim=(11)))

model.add(Dense(units=24, activation='relu'))
model.add(Dropout(.2))

model.add(Dense(units=11, activation='relu'))
model.add(Dropout(.2))

model.add(Dense(units=8, activation='relu'))

model.add(Dense(units=5, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', optimizer="adam", metrics=['accuracy'],run_eagerly=True)

model.fit(X, y, epochs=10, batch_size=32)
stop = timeit.default_timer()
print('Time: ', stop - start)  

test_path = 'url =  "https://raw.githubusercontent.com/marags-web/marags-web/main/IDS/data/network_data_test.txt'

test = pd.read_csv(url, names=headers)

features = ['duration','src_bytes','dst_bytes','num_file_creations', 
           'num_shells','num_failed_logins','wrong_fragment', 
           'urgent', 'is_guest_login', 'su_attempted', 'land', 'attack']

test = test[features]

test['attack'].replace('normal', 0, inplace=True)
test['attack'].replace(dos, 1, inplace=True)
test['attack'].replace(probing, 2, inplace=True)
test['attack'].replace(u2r, 3, inplace=True)
test['attack'].replace(r2l, 4, inplace=True)

X_test, y_test = df.drop('attack', axis=1), df['attack']

val_loss, val_acc = model.evaluate(X_test, y_test) 

# printing confusion matrix
import random
import numpy 
import time 
import timeit
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
import matplotlib.pyplot as plt

predictions = model.predict(X_test)
predictions_labels = []
for row in predictions:
  predictions_labels.append(class_labels[row.argmax()])

actual_labels = []
for row in y_test:
  actual_labels.append(class_labels[row])

cm = confusion_matrix(actual_labels, predictions_labels, labels=class_labels)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_labels)
disp.plot()
plt.show()

# Accuracy score & Numerical scores for the normal packets
from sklearn import metrics

Accuracy = metrics.accuracy_score(actual_labels, predictions_labels)
print("Accuracy",Accuracy)

print("Numerical values for normal packets")
# TP for all classes
TP = cm[0,0]
print("True Positive",cm[0,0])

# FN for 'normal' 
FN = cm[0,1] + cm[0,2] 
print("False Negative" ,FN)

# FP for 'normal' 
FP = cm[1,0] + cm[1,2] 
print ("False Positive", FP)

# TN for 'normal'
TN = cm[1,1] + cm[1,2] + cm[2,1] +cm [2,2]
print("True Negative" ,TN)


#Precision = TruePositives / (TruePositives + FalsePositives)
Precision = TP/(TP+FP)
print("Precision" ,Precision)

#Recall = TruePositives / (TruePositives + FalseNegatives)
Recall =TP/(TP+FN)
print ("Recall"  , Recall)

#F1_score = metrics.f1_score(actual_labels, predictions_labels)
F1_score = (2 * Precision * Recall) / (Precision + Recall)
print ("F1_score" ,F1_score)

# Accuracy score & Numerical scores for the attack type 'DoS'

print("Numerical values for DoS packets")

TP = cm[1,1]
print("True Positive", TP)

# FN 
FN = cm[1,0] + cm[1,2] 
print("False Negative" ,FN)

# FP 
FP = cm[0,1] + cm[2,1] 
print ("False Positive", FP)

# TN 
TN = cm[0,0] + cm[0,2] + cm[2,0] +cm [2,2]
print("True Negative" ,TN)


#Precision = TruePositives / (TruePositives + FalsePositives)
Precision = TP/(TP+FP)
print("Precision" ,Precision)

#Recall = TruePositives / (TruePositives + FalseNegatives)
Recall =TP/(TP+FN)
print ("Recall"  , Recall)

#F1_score = metrics.f1_score(actual_labels, predictions_labels)
F1_score = (2 * Precision * Recall) / (Precision + Recall)
print ("F1_score" ,F1_score)

# Numerical values for 'Probing' Packets 
print("Numerical values for Probing packets")

TP = cm[2,2]
print("True Positive", TP)

# FN 
FN = cm[2,1] + cm[2,2] 
print("False Negative" ,FN)

# FP 
FP = cm[0,2] + cm[1,2] 
print ("False Positive", FP)

# TN 
TN = cm[0,0] + cm[0,1] + cm[1,0] +cm [1,1]
print("True Negative" ,TN)


#Precision = TruePositives / (TruePositives + FalsePositives)
Precision = TP/(TP+FP)
print("Precision" ,Precision)

#Recall = TruePositives / (TruePositives + FalseNegatives)
Recall =TP/(TP+FN)
print ("Recall"  , Recall)

#F1_score = metrics.f1_score(actual_labels, predictions_labels)
F1_score = (2 * Precision * Recall) / (Precision + Recall)
print ("F1_score" ,F1_score)


# Model Prediction 

# generate a random index to make a prediction on
import time
while True:
  import random
  start = timeit.default_timer()
  prediction_index = random.randint(0, len(X_test))
  
# make prediction
  pred_input = np.array(list(X_test.iloc[prediction_index])).reshape(1, 11)
  prediction = class_labels[model.predict( pred_input ).argmax()]
  actual = class_labels[y_test.iloc[prediction_index]]

  stop = timeit.default_timer()
  print('Time: ', stop - start)  
  
# compare prediction vs actual value
  print(f'Predicted Value: {prediction}')
  print(f'Actual Value: {actual}')

# The attack type is posted to MEC API 
  url ='http://mec-api-latest:5000/'
  if (prediction != 'normal'):        
    print(f'Predicted Value: {prediction}')
    print(f'Actual Value: {actual}')
    myobj = {"user_name":"Diyo","email" :"diyo@gmail.com", "sub_type" : prediction} 
    response = requests.post(url,json=myobj)
    myobj = {"user_name":"Hari","email" :"hari@gmail.com", "sub_type" : prediction} 
    response = requests.post(url,json=myobj)
  

  url ='http://mec-api-latest:5000/delete/'
  myobj = {"user_name":"Xian","email" :"xian@gmail.com", "sub_type" : prediction} 
  response = requests.delete(url,json=myobj)       
  # Prediction for every 10 secs
  time.sleep(10)
