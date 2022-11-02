from flask import Flask,jsonify,request
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    if(request.method == 'GET'):
       data = "hello"
       index =1
       return jsonify({'data':data},{index:index})
       #return jsonify({'data':data})
    if(request.method == 'POST'):
       return jsonify({'data':'this is a test'})
   
if __name__ == "__main__":
    app.run(debug=False)
