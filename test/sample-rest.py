from flask import Flask,jsonify,request
import json 

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])

def home():
 
    if(request.method == 'GET'):
        f= open ('subscribe.json','r')
        data = json.load(f)
        for i in data["subscription_details"]:
            return jsonify(data)
        f.close()
    
    if(request.method == 'POST'):
        name = request.json['user_name'] 
        email = request.json['email']
        sub_type = request.json['sub_type']
        
        row1 = {'user_name':str(name),'email':str(email),'sub_type':str(sub_type)}
        print(row1)
       
        # Writing to a file - getting issues since some extra char is added at the end 
        #str1 = json.dumps(row1)
        f = open ('subscribe.json','r')
        data = json.loads(f.read())
        f.close()
        data["subscription_details"].append(row1)
        f = open ('subscribe.json','w')
        f.write(json.dumps(data))
        f.close()
        #f= open ('subscribe.json','a')
        #data = json.loads(f)
        #data["subscription_details"].append(row1)
        #f.write(data)
        #f.close()
        return jsonify(row1)

    if(request.method == 'DELETE'):
       print ("Deleted")
    
    if(request.method == 'PUT'):
       print ("Updated")

if __name__ == "__main__":
    app.run(debug=True)

