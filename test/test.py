from flask import Flask  # From module flask import class Flask
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

#@app.route('/')   # URL '/' to be handled by main() route handler
#def main():
#    """Say hello"""
#    return 'Hello, world!'

@app.route('/',methods=['GET','POST'])
def home():
     if(request.method == 'GET'):        
            return 'I Am in get method'

if __name__ == '__main__':  # Script executed directly?
    print("Hello World! Built with a Docker file.")
    app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=True) 
  
