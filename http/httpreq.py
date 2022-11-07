import requests
import json
url ='http://test-nov3:5000/'

x= requests.get(url)
print(x.text)


myobj = {"user_name":"Diyo","email" :"diyo@gmail.com", "sub_type" : "Probing"}

if( myobj['sub_type'] != 'normal'):
    response = requests.post(url,json=myobj)

myobj = {"user_name":"Eal","email" :"eal@gmail.com", "sub_type" : "normal"}

if( myobj['sub_type'] != 'normal'):
   response = requests.post(url,json=myobj)

myobj = {"user_name":"Xian","email" :"xian@gmail.com", "sub_type" : "DoS"}

if( myobj['sub_type'] != 'normal'):
    response = requests.post(url,json=myobj)

