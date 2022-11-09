
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


# 3. Buidling the model
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


# generate a random index to make a prediction on
import random
prediction_index = random.randint(0, len(X_test))

# make prediction
pred_input = np.array(list(X_test.iloc[prediction_index])).reshape(1, 11)
prediction = class_labels[model.predict( pred_input ).argmax()]
actual = class_labels[y_test.iloc[prediction_index]]

# compare prediction vs actual value
print(f'Predicted Value: {prediction}')
print(f'Actual Value: {actual}')

# The attack type is posted to MEC API 
url ='http://mec-api-latest:5000/'
if (prediction != 'normal'):
  myobj = {"user_name":"Diyo","email" :"diyo@gmail.com", "sub_type" : prediction} 
  response = requests.post(url,json=myobj)

