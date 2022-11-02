import requests

url ='http://127.0.0.1:8000/'
myobj = {'data':'hi'}

x = requests.post(url,json=myobj)
print(x.text)
